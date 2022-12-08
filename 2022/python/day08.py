from typing import Iterable


def get_lines(file_path: str) -> list[list[int]]:
    with open(file_path, "r", encoding="utf-8") as f:
        return [parse_line(line) for line in f.readlines()]


def parse_line(line: str) -> list[int]:
    return [int(num) for num in line.strip()]


def check_line(line: list[int]) -> Iterable[int]:
    """Return the indices of trees visible from the left in a line"""
    highest = -1
    for index, tree in enumerate(line):
        if tree > highest:
            highest = tree
            yield index
        else:
            continue


def part_1(file_path: str) -> int:
    lines = get_lines(file_path)
    width = len(lines[0])
    max_x = width - 1
    max_y = len(lines) - 1

    visible_coordinates = set()

    for y, line in enumerate(lines):
        # Visible from the left
        for x in check_line(line):
            visible_coordinates.add((x, y))
        # Visible from the right
        for x in check_line(line[::-1]):
            visible_coordinates.add((abs(x - max_x), y))

    for x in range(width):
        column = [line[x] for line in lines]
        # Visible from the top
        for y in check_line(column):
            visible_coordinates.add((x, y))
        # Visible from the bottom
        for y in check_line(column[::-1]):
            visible_coordinates.add((x, abs(y - max_y)))

    return len(visible_coordinates)


def scenic_score(line: list[int]) -> int:
    """Calculate the scenic score from the first item"""
    tree = line[0]
    score = 0
    for t in line[1:]:
        score += 1
        if t >= tree:
            break
    return score


def part_2(file_path: str) -> int:
    max_score = 0
    lines = get_lines(file_path)

    for y in range(1, len(lines) - 1):
        for x in range(1, len(lines[0]) - 1):
            right = scenic_score(lines[y][x:])
            left = scenic_score(lines[y][: x + 1][::-1])
            column = [line[x] for line in lines]
            down = scenic_score(column[y:])
            up = scenic_score(column[: y + 1][::-1])
            max_score = max(max_score, left * right * up * down)

    return max_score


if __name__ == "__main__":
    input_path = "../input/day08.txt"
    print(f"Part 1: {part_1(input_path)}")
    print(f"Part 2: {part_2(input_path)}")
