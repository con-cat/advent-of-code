import copy
import io
import itertools


def get_reports(input_file: io.TextIOWrapper) -> list[list[int]]:
    reports = []
    for line in input_file:
        levels = [int(number) for number in line.split(" ")]
        reports.append(levels)

    return reports


def check_report(report: list[int]) -> tuple[bool, int]:
    is_increasing = False
    is_decreasing = False
    for i, (num_1, num_2) in enumerate(itertools.pairwise(report)):
        difference = num_1 - num_2
        if difference == 0:
            return False, i

        elif abs(difference) > 3:
            return False, i

        elif difference < 0:
            is_increasing = True
            if is_decreasing:
                return False, i

        else:
            is_decreasing = True
            if is_increasing:
                return False, i

    return True, i


def part_2(reports: list[list[int]]) -> int:
    num_safe = 0
    for report in reports:
        current_report = copy.deepcopy(report)
        is_safe, index_to_skip = check_report(current_report)
        if not is_safe:
            del current_report[index_to_skip]
            is_safe, _ = check_report(current_report)
        if not is_safe:
            current_report = copy.deepcopy(report)
            del current_report[index_to_skip + 1]
            is_safe, _ = check_report(current_report)
        if is_safe:
            num_safe += 1

    return num_safe


def part_1(reports: list[list[int]]) -> int:
    num_safe = 0
    for report in reports:
        is_safe, _ = check_report(report)

        if is_safe:
            num_safe += 1

    return num_safe


if __name__ == "__main__":
    input_path = "../input/day02"
    with open(input_path, "r", encoding="utf-8") as f:
        reports = get_reports(f)

    print("Part 1:")
    print(part_1(reports))

    print("Part 2:")
    print(part_2(reports))
