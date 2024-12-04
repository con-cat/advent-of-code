import re
from collections.abc import Sequence


def part_1(instructions: Sequence[str]) -> int:
    total = 0
    for line in instructions:
        for num_1, num_2 in re.findall(r"mul\((\d+),(\d+)\)", line):
            total += int(num_1) * int(num_2)

    return total


if __name__ == "__main__":
    input_path = "../input/day03"
    with open(input_path, "r", encoding="utf-8") as f:
        print("Part 1:")
        print(part_1(f))
