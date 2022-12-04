from typing import Callable


class Day4:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def parse_line(self, line: str) -> list[set]:
        return [self.sections_to_set(sections) for sections in line.split(",")]

    def sections_to_set(self, sections: str) -> set:
        numbers = [int(num) for num in sections.split("-", 2)]
        return set(range(numbers[0], numbers[1] + 1))

    def solve(self, solving_func: Callable[[set, set], bool]) -> int:
        count = 0
        with open(self.file_path, "r", encoding="utf-8") as f:
            for line in f:
                count += int(solving_func(*self.parse_line(line)))

        return count


def check_part_1(set_1: set[int], set_2: set[int]) -> bool:
    return set_1 <= set_2 or set_1 >= set_2


def check_part_2(set_1: set[int], set_2: set[int]) -> bool:
    return bool(set_1 & set_2)


if __name__ == "__main__":
    input_path = "../input/day04.txt"
    print("Part 1")
    print(Day4(input_path).solve(check_part_1))
    print("Part 2")
    print(Day4(input_path).solve(check_part_2))
