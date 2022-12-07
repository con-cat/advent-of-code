import dataclasses
from functools import cached_property
from typing import Optional

MAX_DIRECTORY_SIZE = 100000
TOTAL_SPACE = 70000000
SPACE_FOR_UPDATE = 30000000


@dataclasses.dataclass
class Directory:
    name: str
    parent: Optional["Directory"]
    file_size: int = 0
    subdirectories: list["Directory"] = dataclasses.field(default_factory=list)

    @cached_property
    def total_file_size(self) -> int:
        size = self.file_size
        for directory in self.subdirectories:
            size += directory.total_file_size
        return size


class Day7:
    root: Directory
    current_dir: Directory

    def __init__(self, file_path: str) -> None:
        """Read and parse the file into a tree structure of Directory"""
        self.root = self.current_dir = Directory(name="/", parent=None)
        with open(file_path, "r", encoding="utf-8") as f:
            next(f)
            for line in f:
                line_list = line.split()
                if line_list[0] == "$":
                    self.parse_command_line(line_list)
                else:
                    self.parse_output_line(line_list)

    def parse_command_line(self, line: list[str]) -> None:
        """Parse line starting with '$'"""
        if line[1] == "cd":
            if line[2] == "..":
                assert self.current_dir.parent
                self.current_dir = self.current_dir.parent
            else:
                subdirectory = Directory(name=line[2], parent=self.current_dir)
                self.current_dir.subdirectories.append(subdirectory)
                self.current_dir = subdirectory

    def parse_output_line(self, line: list[str]) -> None:
        """Parse output from a command"""
        if line[0] != "dir":
            self.current_dir.file_size += int(line[0])

    def get_sizes_in_range(
        self, directory: Directory, min_size: int, max_size: int | None
    ) -> list[int]:
        """Traverse the directories, get all file sizes between min and max"""
        sizes = []
        total_file_size = directory.total_file_size
        if total_file_size >= min_size and (
            max_size is None or total_file_size <= max_size
        ):
            sizes.append(total_file_size)
        for subdirectory in directory.subdirectories:
            sizes.extend(self.get_sizes_in_range(subdirectory, min_size, max_size))
        return sizes

    def part_1(self) -> int:
        return sum(
            self.get_sizes_in_range(self.root, min_size=0, max_size=MAX_DIRECTORY_SIZE)
        )

    def part_2(self) -> int:
        space_needed = SPACE_FOR_UPDATE - (TOTAL_SPACE - self.root.total_file_size)
        candidates = self.get_sizes_in_range(
            self.root, min_size=space_needed, max_size=None
        )
        return min(candidates)


if __name__ == "__main__":
    input_path = "../input/day07.txt"
    day_7 = Day7(input_path)
    print(f"Part 1: {day_7.part_1()}")
    print(f"Part 2: {day_7.part_2()}")
