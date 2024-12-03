import io
import itertools


def get_reports(input_file: io.TextIOWrapper) -> list[list[int]]:
    reports = []
    for line in input_file:
        levels = [int(number) for number in line.split(" ")]
        reports.append(levels)

    return reports


def part_1(reports: list[list[int]]) -> int:
    num_safe = 0
    for report in reports:
        is_increasing = False
        is_decreasing = False
        is_safe = True
        for num_1, num_2 in itertools.pairwise(report):
            difference = num_1 - num_2
            if difference == 0:
                is_safe = False
                break

            elif abs(difference) > 3:
                is_safe = False
                break

            elif difference < 0:
                is_increasing = True
                if is_decreasing:
                    is_safe = False
                    break

            else:
                is_decreasing = True
                if is_increasing:
                    is_safe = False
                    break

        if is_safe:
            num_safe += 1

    return num_safe


if __name__ == "__main__":
    input_path = "../input/day02"
    with open(input_path, "r", encoding="utf-8") as f:
        reports = get_reports(f)

    print("Part 1:")
    print(part_1(reports))
