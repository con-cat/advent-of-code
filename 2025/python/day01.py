import operator

INPUT_PATH = "../input/day01.txt"

DIAL_START = 50


def part_1(instructions: list[str]) -> int:
    current_number = DIAL_START
    zero_count = 0

    for instruction in instructions:
        direction = instruction[0]
        num_clicks = int(instruction[1:])

        current_number = rotate(current_number, num_clicks, direction)

        if current_number == 0:
            zero_count += 1

    return zero_count


def rotate(current_number: int, num_clicks: int, direction: str) -> int:
    operation = {"L": operator.sub, "R": operator.add}[direction]
    difference = num_clicks % 100  # Ignore full circles
    new_number = operation(current_number, difference)

    # Adjust if we've gone past 0 or 99
    if new_number < 0:
        new_number += 100

    elif new_number > 99:
        new_number -= 100

    assert 0 <= new_number <= 99

    return new_number


if __name__ == "__main__":
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        instructions = f.readlines()

    print("Part 1:")
    print(part_1(instructions))
