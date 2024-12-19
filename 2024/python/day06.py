import copy
from collections import deque
import dataclasses

CLEAR = "."
OBSTACLE = "#"
VISITED = "X"
GUARD_MAP = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^",
}


@dataclasses.dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


def get_next_coordinates(char: str, x: int, y: int) -> tuple[int, int]:
    match char:
        case "^":
            next_y, next_x = y - 1, x
        case ">":
            next_y, next_x = y, x + 1
        case "v":
            next_y, next_x = y + 1, x
        case "<":
            next_y, next_x = y, x - 1
        case _:
            raise ValueError("This shouldn't happen")

    return next_x, next_y


def part_1(the_map: list[list[str]]) -> int:
    num_rows = len(the_map)
    num_cols = len(the_map[0])
    x = 0
    y = 0

    count = 1

    while y < num_rows:
        char = the_map[y][x]
        if char not in GUARD_MAP:
            x += 1
            if x == num_cols:
                x = 0
                y += 1
            continue

        next_x, next_y = get_next_coordinates(char, x, y)

        try:
            next_char = the_map[next_y][next_x]
        except IndexError:
            break
        else:
            if next_x < 0 or next_y < 0:
                break

        if next_char in (CLEAR, VISITED):
            if next_char == CLEAR:
                count += 1
            the_map[next_y][next_x] = char
            the_map[y][x] = VISITED
            x = next_x
            y = next_y
        elif next_char == OBSTACLE:
            the_map[y][x] = GUARD_MAP[char]

    return count


def part_2(the_map: list[list[str]]) -> int:
    num_rows = len(the_map)
    num_cols = len(the_map[0])
    x = 0
    y = 0

    count = 0
    corners = deque([], 3)
    fourth_corner = None

    while y < num_rows:
        char = the_map[y][x]
        if char not in GUARD_MAP:
            x += 1
            if x == num_cols:
                x = 0
                y += 1
            continue

        next_x, next_y = get_next_coordinates(char, x, y)

        try:
            next_char = the_map[next_y][next_x]
        except IndexError:
            break
        else:
            if next_x < 0 or next_y < 0:
                break

        if next_char in (CLEAR, VISITED):
            the_map[next_y][next_x] = char
            the_map[y][x] = VISITED
            x = next_x
            y = next_y
            if Point(x, y) == fourth_corner:
                count += 1
                print("\n".join(["".join(line) for line in the_map]))
                print(count)
                print("\n")
        elif next_char == OBSTACLE:
            breakpoint()
            the_map[y][x] = GUARD_MAP[char]
            corners.append(Point(x, y))
            fourth_corner = get_fourth_corner(corners)

    return count


def get_fourth_corner(corners) -> Point | None:
    if len(corners) != 3:
        return None

    return corners[0] + corners[2] - corners[1]


if __name__ == "__main__":
    input_path = "../input/day06"
    with open(input_path, "r", encoding="utf-8") as f:
        lines = list(f)

    the_map = [list(line.rstrip()) for line in lines]

    print("Part 1:")
    print(part_1(copy.deepcopy(the_map)))

    print("Part 2:")
    print(part_2(copy.deepcopy(the_map)))
