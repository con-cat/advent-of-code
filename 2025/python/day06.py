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

    problems = parse_input_part_1(input_path)
    for problem in problems:
        operation = problem[0]
        numbers = problem[1]
        subtotal = functools.reduce(lambda x, y: operation(x, y), numbers)
        grand_total += subtotal

    return grand_total


def parse_input_part_1(input_path: str) -> list[tuple[Callable, list[int]]]:
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


def part_2(input_path: str) -> list[list[Callable, list[int]]]:
    with open(input_path, "r", encoding="utf-8") as f:
        # Reverse the characters in each line
        lines = f.readlines()

    operations = lines.pop()

    problem_map = _build_problem_map(operations)

    grand_total = 0
    for (start, end), operation in problem_map.items():
        problem_lines = [line[start:end] for line in lines]
        numbers = _parse_problem(problem_lines)
        subtotal = functools.reduce(lambda x, y: operation(x, y), numbers)
        grand_total += subtotal

    return grand_total


def _build_problem_map(operations: list[str]) -> dict[tuple[int], Callable]:
    """Build a dictionary of start and end indices of problems and their operations."""
    problem_map: dict[tuple[int, int], Callable] = {}
    previous_problem_start_index = 0
    previous_operation = None
    for i, char in enumerate(operations):
        try:
            operation = OPERATIONS[char]
        except KeyError:
            continue
        else:
            problem_start_index = i
            if previous_operation is not None:
                problem_map[(previous_problem_start_index, problem_start_index)] = (
                    previous_operation
                )
            previous_operation = operation
            previous_problem_start_index = problem_start_index

    problem_map[(problem_start_index, len(operations) + 1)] = operation

    return problem_map


def _parse_problem(problem: list[str]) -> list[str]:
    numbers = []
    # Rotate the lines of the problem 90 degrees
    transposed = [list(row) for row in zip(*problem)]

    for row in transposed:
        number_str = "".join(row)
        try:
            number = int(number_str)
        except ValueError:
            continue

        numbers.append(number)

    return numbers


if __name__ == "__main__":
    assert part_2(TEST_INPUT_PATH) == 3263827

    print(part_2(INPUT_PATH))
