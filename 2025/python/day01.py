import operator

INPUT_PATH = "../input/day01.txt"

DIAL_START = 50


class Solution:
    def __init__(self) -> None:
        self.current_number = DIAL_START
        self.zero_count = 0
        with open(INPUT_PATH, "r", encoding="utf-8") as f:
            self.instructions = f.readlines()

    def part_1(self) -> int:
        for instruction in self.instructions:
            direction = instruction[0]
            num_clicks = int(instruction[1:])

            self.current_number, _ = self.rotate(num_clicks, direction)

            if self.current_number == 0:
                self.zero_count += 1

        return self.zero_count

    def part_2(self) -> int:
        for instruction in self.instructions:
            direction = instruction[0]
            num_clicks = int(instruction[1:])

            self.current_number, zero_count = self.rotate(num_clicks, direction)
            self.zero_count += zero_count

        return self.zero_count

    def rotate(self, num_clicks: int, direction: str) -> tuple[int, int]:
        zero_count = int(num_clicks / 100)
        difference = num_clicks % 100

        operation = {"L": operator.sub, "R": operator.add}[direction]
        new_number = operation(self.current_number, difference)

        # Adjust if we've gone past 0 or 99
        if new_number == 0:
            zero_count += 1

        elif new_number < 0:
            if self.current_number != 0:
                zero_count += 1
            new_number += 100

        elif new_number > 99:
            if self.current_number != 0:
                zero_count += 1
            new_number -= 100

        assert 0 <= new_number <= 99

        return new_number, zero_count


if __name__ == "__main__":
    print("Part 1:")
    print(Solution().part_1())

    print("Part 2:")
    print(Solution().part_2())
