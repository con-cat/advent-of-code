import operator
import itertools

OPERATORS = (operator.add, operator.mul)


def get_input():
    input_path = "../input/day07"

    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            test_value, numbers_str = line.split(": ")
            numbers = [int(n) for n in numbers_str.split(" ")]
            yield (int(test_value), numbers)


def equation_can_be_true(test_value: int, numbers: list[int]) -> bool:
    # Get all possible combinations of operators
    operator_combinations = itertools.combinations_with_replacement(
        OPERATORS, len(numbers) - 1
    )
    for combination in operator_combinations:
        # Get all permutations of the combinations
        for permutation in itertools.permutations(combination):
            result = numbers[0]
            for op, number in zip(permutation, numbers[1:]):
                result = op(result, number)

            if result == test_value:
                return True

    return False


def part_1() -> int:
    test_value_sum = 0
    for test_value, numbers in get_input():
        if equation_can_be_true(test_value, numbers):
            test_value_sum += test_value

    return test_value_sum


if __name__ == "__main__":
    print("Part 1:")
    print(part_1())
