import io


def part_1(input_file: io.TextIOWrapper) -> int:
    left_list = []
    right_list = []
    for line in input_file:
        left, right = line.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))

    total = 0
    for left, right in zip(sorted(left_list), sorted(right_list)):
        total += abs(left - right)

    return total


if __name__ == "__main__":
    input_path = "../input/day01"
    with open(input_path, "r", encoding="utf-8") as f:
        print("Part 1:")
        print(part_1(f))
