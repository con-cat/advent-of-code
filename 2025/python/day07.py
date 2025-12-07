TEST_INPUT_PATH = "../input/test_day07.txt"
INPUT_PATH = "../input/day07.txt"

START_LOCATION = "S"
SPLITTER = "^"
BEAM = "|"


def part_1(input_path: str) -> int:
    with open(input_path, "r", encoding="utf-8") as f:
        lines = [list(line) for line in f.readlines()]

    start_index = lines[0].index(START_LOCATION)
    lines[0][start_index] = BEAM

    split_count = 0
    for prev_index, line in enumerate(lines[1:]):
        previous_line = lines[prev_index]
        for i, char in enumerate(previous_line):
            if char != BEAM:
                continue

            current_char = line[i]

            if current_char == SPLITTER:
                split_count += 1
                line[i - 1] = BEAM
                line[i + 1] = BEAM

            else:
                line[i] = BEAM

    return split_count


if __name__ == "__main__":
    assert part_1(TEST_INPUT_PATH) == 21

    print(part_1(INPUT_PATH))
