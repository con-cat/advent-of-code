import operator
from collections import deque
from dataclasses import dataclass
from typing import Callable

OPERATORS = {"+": operator.add, "-": operator.sub, "*": operator.mul}


@dataclass
class Monkey:
    items: deque
    operation: Callable
    test: int
    if_true: int
    if_false: int
    items_inspected: int = 0


class Day11:
    def __init__(self, input_path: str, part_1: bool = False) -> None:
        self.part_1 = part_1
        with open(input_path, "r", encoding="utf-8") as f:
            input_str = f.read()
            monkeys = input_str.split("\n\n")
            self.monkeys = [self._parse_monkey(monkey) for monkey in monkeys]
            self.all_tests = 1
            for monkey in self.monkeys:
                self.all_tests *= monkey.test

    def solve(self, num_rounds: int) -> int:
        for _ in range(num_rounds):
            self.monkey_round()

        inspected = sorted([m.items_inspected for m in self.monkeys], reverse=True)
        return inspected[0] * inspected[1]

    def monkey_round(self) -> None:
        for monkey in self.monkeys:
            if not monkey.items:
                continue
            for _ in range(len(monkey.items)):
                item = monkey.items.popleft()
                item = monkey.operation(item)
                if self.part_1:
                    item = item // 3
                else:
                    item = item % self.all_tests
                if item % monkey.test == 0:
                    self.monkeys[monkey.if_true].items.append(item)
                else:
                    self.monkeys[monkey.if_false].items.append(item)
                monkey.items_inspected += 1

    def _parse_monkey(self, monkey: str) -> Monkey:
        lines = monkey.split("\n")
        starting_items = [
            int(n) for n in lines[1].removeprefix("  Starting items: ").split(", ")
        ]
        return Monkey(
            items=deque(starting_items),
            operation=self._parse_operation(lines[2]),
            test=int(lines[3].removeprefix("  Test: divisible by ")),
            if_true=int(lines[4].removeprefix("    If true: throw to monkey ")),
            if_false=int(lines[5].removeprefix("    If false: throw to monkey ")),
        )

    def _parse_operation(self, operation: str) -> Callable:
        operation = operation.removeprefix("  Operation: new = old ")
        op_str, x = operation.split(" ", 2)
        op = OPERATORS[op_str]
        if x == "old":
            return lambda item: op(item, item)
        else:
            return lambda item: op(item, int(x))


if __name__ == "__main__":
    input_path = "../input/day11.txt"
    part_1 = Day11(input_path, part_1=True).solve(20)
    print(part_1)
    part_2 = Day11(input_path).solve(10000)
    print(part_2)
