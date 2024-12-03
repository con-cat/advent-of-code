import io


def get_lists(input_file: io.TextIOWrapper) -> tuple[list[int], list[int]]:
    left_list = []
    right_list = []
    for line in input_file:
        left, right = line.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))

    return left_list, right_list


def part_1(left_list: list[int], right_list: list[int]) -> int:
    total = 0
    for left, right in zip(sorted(left_list), sorted(right_list)):
        total += abs(left - right)

    return total


def part_2(left_list: list[int], right_list: list[int]) -> int:
    similarity_score = 0
    for left_number in left_list:
        times_seen = 0
        for right_number in right_list:
            if right_number == left_number:
                times_seen += 1

        similarity_score += left_number * times_seen

    return similarity_score


if __name__ == "__main__":
    input_path = "../input/day01"
    with open(input_path, "r", encoding="utf-8") as f:
        left_list, right_list = get_lists(f)

    print("Part 1:")
    print(part_1(left_list, right_list))

    print("Part 2:")
    print(part_2(left_list, right_list))
