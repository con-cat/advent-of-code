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

    def solve(self) -> int:
        with open(self.file_path, "r", encoding="utf-8") as f:
            for line in f:
                direction, steps = self.parse_line(line)
                self.move(steps, *DIRECTIONS_MAP[direction])

        return len(self.visited)

    def parse_line(self, line: str) -> tuple[str, int]:
        split = line.strip().split()
        return (split[0], int(split[1]))

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
                tail = self.rope[self.tail_index]
                self.visited.add((tail.x, tail.y))

    def move_next(self, point_1: Point, point_2: Point) -> None:
        x_difference = point_1.x - point_2.x
        y_difference = point_1.y - point_2.y
        x_too_far = abs(point_1.x - point_2.x) > 1
        y_too_far = abs(point_1.y - point_2.y) > 1
        if x_too_far or y_too_far:
            # point_2 needs to move
            if point_1.x != point_2.x and point_1.y != point_2.y:
                # Move diagonally!
                if x_too_far and y_too_far:
                    point_2.x += int(x_difference / 2)
                    point_2.y += int(y_difference / 2)
                    return
                elif x_too_far:
                    point_2.y = point_1.y
                elif y_too_far:
                    point_2.x = point_1.x
            if x_too_far:
                point_2.x += int(x_difference / 2)
            elif y_too_far:
                point_2.y += int(y_difference / 2)


if __name__ == "__main__":
    input_path = "../input/day09.txt"
    print(f"Part 1: {Day9(input_path, 2).solve()}")
    print(f"Part 2: {Day9(input_path, 10).solve()}")
