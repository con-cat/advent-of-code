DIRECTIONS_MAP = {
    # X and Y directions for each string
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, 1),
    "D": (0, -1),
}


class Day9:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.head = [0, 0]
        self.tail = [0, 0]
        self.visited: set[tuple[int, int]] = {(0, 0)}

    def parse_line(self, line: str) -> tuple[str, int]:
        split = line.strip().split()
        return (split[0], int(split[1]))

    def update_visited(self) -> None:
        self.visited.add(tuple(self.tail))

    def move_tail(self, x_direction: int, y_direction: int) -> None:
        if self.head == self.tail:
            return
        x_too_far = abs(self.head[0] - self.tail[0]) > 1
        y_too_far = abs(self.head[1] - self.tail[1]) > 1
        if x_too_far or y_too_far:
            # The tail needs to move
            if self.head[0] != self.tail[0] and self.head[1] != self.tail[1]:
                # Move diagonally!
                if x_too_far:
                    self.tail[1] = self.head[1]
                elif y_too_far:
                    self.tail[0] = self.head[0]
            if x_direction:
                self.tail[0] += x_direction
                self.update_visited()
            elif y_direction:
                self.tail[1] += y_direction
                self.update_visited()

    def move_head(self, steps: int, x_direction: int, y_direction: int) -> None:
        for _ in range(steps):
            if x_direction:
                self.head[0] += x_direction
            elif y_direction:
                self.head[1] += y_direction
            self.move_tail(x_direction, y_direction)

    def part_1(self) -> int:
        with open(self.file_path, "r", encoding="utf-8") as f:
            for line in f:
                direction, steps = self.parse_line(line)
                self.move_head(steps, *DIRECTIONS_MAP[direction])

        return len(self.visited)


if __name__ == "__main__":
    input_path = "../input/day09.txt"
    test_path = "../input/day09_test.txt"
    assert Day9(test_path).part_1() == 13
    print(f"Part 1: {Day9(input_path).part_1()}")
