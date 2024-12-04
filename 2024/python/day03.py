import re


def part_1(instructions: list[str]) -> int:
    total = 0
    for line in instructions:
        for num_1, num_2 in re.findall(r"mul\((\d+),(\d+)\)", line):
            total += int(num_1) * int(num_2)

    return total


def part_2(instructions: list[str]) -> int:
    total = 0
    should_multiply = True
    for line in instructions:
        statements = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
        for statement in statements:
            if statement.startswith("don't"):
                should_multiply = False
            elif statement.startswith("do"):
                should_multiply = True
            elif should_multiply:
                num_1, num_2 = re.findall(r"\d+", statement)
                total += int(num_1) * int(num_2)

    return total


if __name__ == "__main__":
    input_path = "../input/day03"
    with open(input_path, "r", encoding="utf-8") as f:
        instructions = list(f)

    print("Part 1:")
    print(part_1(instructions))

    print("Part 2:")
    print(part_2(instructions))
