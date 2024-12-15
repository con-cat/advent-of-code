def part_1(rules: list[tuple[str, str]], updates: list[list[str]]) -> int:
    total = 0
    for pages in updates:
        indices = {page: i for i, page in enumerate(pages)}
        for rule in rules:
            try:
                is_in_order = indices[rule[0]] < indices[rule[1]]
            except KeyError:
                continue

            if not is_in_order:
                break

        if is_in_order:
            index = int(len(pages) / 2)
            total += int(pages[index])

    return total


if __name__ == "__main__":
    rules = []
    updates = []
    input_path = "../input/day05"
    with open(input_path, "r", encoding="utf-8") as f:
        parsing_rules = True
        for line in f:
            if line == "\n":
                parsing_rules = False
                continue

            if parsing_rules:
                rules.append(tuple(line.rstrip().split("|")))

            else:
                updates.append(line.rstrip().split(","))

    print("Part 1:")
    print(part_1(rules, updates))
