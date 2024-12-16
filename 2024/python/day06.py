CLEAR = "."
OBSTACLE = "#"
VISITED = "X"
GUARD_MAP = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^",
}


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


if __name__ == "__main__":
    input_path = "../input/day06"
    with open(input_path, "r", encoding="utf-8") as f:
        the_map = [list(line.rstrip()) for line in f]

    print("Part 1:")
    print(part_1(the_map))
