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


def part_2(rules: list[tuple[str, str]], updates: list[list[str]]) -> int:
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

        if not is_in_order:
            ordered = order_indices(indices, rules)
            index = int(len(pages) / 2)
            sorted_pages = [
                page for page, _ in sorted(ordered.items(), key=lambda item: item[1])
            ]
            total += int(sorted_pages[index])

    return total


def order_indices(
    indices: dict[str, int], rules: list[tuple[str, str]]
) -> dict[str, int]:
    for rule in rules:
        try:
            first_rule_index = indices[rule[0]]
            second_rule_index = indices[rule[1]]
            is_in_order = first_rule_index < second_rule_index
        except KeyError:
            continue

        if not is_in_order:
            indices[rule[0]] = second_rule_index
            indices[rule[1]] = first_rule_index
            return order_indices(indices, rules)

    return indices


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

    print("Part 2:")
    print(part_2(rules, updates))
