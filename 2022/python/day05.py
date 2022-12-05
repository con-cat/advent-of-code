import re
from collections import defaultdict, deque


class DoneWithStacks(Exception):
    pass


class Day5:
    stacks: defaultdict[int, deque[str]]
    directions: list[tuple[int, int, int]]

    def __init__(self, file_path: str) -> None:
        """Read and parse the file into structures we can use"""
        self.stacks = defaultdict(deque)
        self.directions = []
        with open(file_path, "r", encoding="utf-8") as f:
            stacks_initialised = False
            for line in f:
                # Initialise the stacks
                if not stacks_initialised:
                    try:
                        self.parse_stack_line(line)
                    except DoneWithStacks:
                        next(f)
                        stacks_initialised = True
                # Initialise the directions
                else:
                    self.parse_directions_line(line)

    def parse_stack_line(self, line: str) -> None:
        """Parse a line, add container data to self.stacks"""
        # Split the line into a list of substrings the length of 1 stack
        # e.g. ["    ", "[A] ", "[B]\n"]
        n = 4
        stack_strings = [line[i : i + n] for i in range(0, len(line), n)]
        for index, item in enumerate(stack_strings):
            # If they contain a letter, add them to the appropriate queue
            char = item[1]
            if char.isnumeric():
                raise DoneWithStacks
            elif char.isspace():
                continue
            else:
                self.stacks[index + 1].appendleft(char)

    def parse_directions_line(self, line: str) -> None:
        """Parse a line, add the numbers to self.directions"""
        p = re.compile(r"^move (\d+) from (\d+) to (\d+)")
        self.directions.append(tuple(int(num) for num in p.findall(line).pop()))

    def solve(self) -> str:
        for direction in self.directions:
            num_crates, from_stack, to_stack = direction
            for _ in range(num_crates):
                self.stacks[to_stack].append(self.stacks[from_stack].pop())

        result = ""
        for _, stack in sorted(self.stacks.items(), key=lambda s: s[0]):
            result += stack[-1]
        return result


if __name__ == "__main__":
    input_path = "../input/day05.txt"
    print("Part 1")
    part1 = Day5(input_path)
    print(part1.solve())
