import operator
from collections.abc import Callable
import functools

TEST_INPUT_PATH = "../input/test_day06.txt"
INPUT_PATH = "../input/day06.txt"

OPERATIONS = {
    "+": operator.add,
    "*": operator.mul,
}


def part_1(input_path: str) -> int:
    grand_total = 0

    problems = parse_input_file(input_path)
    for problem in problems:
        operation = problem[0]
        numbers = problem[1]
        subtotal = functools.reduce(lambda x, y: operation(x, y), numbers)
        grand_total += subtotal

    return grand_total


def parse_input_file(input_path: str) -> list[tuple[Callable, list[int]]]:
    split_lines = []
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f.readlines():
            # Strip double spaces
            line = " ".join(line.split())
            split_lines.append(line.split(" "))

    num_columns = len(split_lines[0])

    problems = []

    for i in range(num_columns):
        rotated_line = []
        for line in split_lines:
            rotated_line.append(line[i])

        operation = OPERATIONS[rotated_line.pop()]
        numbers = [int(number) for number in rotated_line]
        problems.append((operation, numbers))

    return problems


if __name__ == "__main__":
    print(part_1(INPUT_PATH))
