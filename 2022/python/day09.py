import sys
import time
from dataclasses import dataclass

DIRECTIONS_MAP = {
    # X and Y directions for each string
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, 1),
    "D": (0, -1),
}


@dataclass
class Point:
    x: int
    y: int


class Day9:
    def __init__(self, file_path: str, rope_length: int) -> None:
        self.file_path = file_path
        self.tail_index = rope_length - 1
        self.rope = []
        for _ in range(rope_length):
            self.rope.append(Point(0, 0))

        self.visited: set[tuple[int, int]] = {(0, 0)}

    def parse_line(self, line: str) -> tuple[str, int]:
        split = line.strip().split()
        return (split[0], int(split[1]))

    def move_next(self, point_1: Point, point_2: Point) -> None:
        x_difference = point_1.x - point_2.x
        y_difference = point_1.y - point_2.y
        x_too_far = abs(point_1.x - point_2.x) > 1
        y_too_far = abs(point_1.y - point_2.y) > 1
        if x_too_far or y_too_far:
            # point_2 needs to move
            if point_1.x != point_2.x and point_1.y != point_2.y:
                # Move diagonally!
                if x_too_far:
                    point_2.y = point_1.y
                elif y_too_far:
                    point_2.x = point_1.x
            if x_too_far:
                point_2.x += int(x_difference / 2)
            elif y_too_far:
                point_2.y += int(y_difference / 2)

            tail = self.rope[self.tail_index]
            self.visited.add((tail.x, tail.y))

    def move(self, steps: int, x_direction: int, y_direction: int) -> None:
        head = self.rope[0]
        for _ in range(steps):
            head.x += x_direction
            head.y += y_direction
            for i in range(self.tail_index):
                # Move the rest of the rope
                if self.rope[i] == self.rope[i + 1]:
                    break
                self.move_next(self.rope[i], self.rope[i + 1])
            self.display()

    def display(self):
        lines = []
        for y in range(5):
            line = ""
            for x in range(6):
                point = Point(x, y)
                try:
                    s = self.rope.index(point)
                    if s == 0:
                        s = "H"
                except ValueError:
                    s = "."
                line += str(s)
            lines.append(line)
        sys.stdout.flush()
        for line in lines[::-1]:
            sys.stdout.write(line + "\n")
        sys.stdout.write("\n")

    def solve(self) -> int:
        with open(self.file_path, "r", encoding="utf-8") as f:
            for line in f:
                direction, steps = self.parse_line(line)
                sys.stdout.write(f"==={direction}{steps}===\n")
                self.move(steps, *DIRECTIONS_MAP[direction])

        return len(self.visited)


if __name__ == "__main__":
    input_path = "../input/day09.txt"
    test_path = "../input/day09_test.txt"
    # assert Day9(test_path, 2).solve() == 13
    # assert Day9(input_path, 2).solve() == 6181
    # print(f"Part 1: {Day9(input_path, 2).solve()}")
    # test_1 = Day9("../input/day09_test.txt", 10).solve()
    # assert test_1 == 1, test_1
    # test_2 = Day9("../input/day09_test2.txt", 10).solve()
    test_2 = Day9("../input/day09_test.txt", 10).solve()
    # assert test_2 == 36, test_2
    # part_2 = Day9(input_path, 10).solve()
    # assert part_2 < 2408, part_2
    # print(f"Part 2: {Day9(input_path, 10).solve()}")
