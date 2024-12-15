INPUT = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

XMAS = ["X", "M", "A", "S"]

MAS_MAP = {"M": "S", "S": "M"}


def count_xmas(matrix: list[list[str]]) -> int:
    count = 0
    for row in matrix:
        for i, char in enumerate(row):
            if row[i : i + 4] == XMAS:
                count += 1

    return count


def rotate_45(matrix: list[list[str]]) -> list[list[str]]:
    # https://algocademy.com/blog/matrix-traversal-mastering-spiral-diagonal-and-zigzag-patterns/
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    # Traverse the top-right half of the matrix
    for i in range(cols):
        row, col = 0, i
        current = []
        while row < rows and col >= 0:
            current.append(matrix[row][col])
            row += 1
            col -= 1
        result.append(current)

    # Traverse the bottom-left half of the matrix
    for i in range(1, rows):
        row, col = i, cols - 1
        current = []
        while row < rows and col >= 0:
            current.append(matrix[row][col])
            row += 1
            col -= 1
        result.append(current)

    return result


def part_1(matrix: list[list[str]]) -> int:
    count = count_xmas(matrix)
    count += count_xmas(rotate_45(matrix))
    current_array = matrix
    for _ in range(3):
        # Rotate 45 degrees
        # Rotate 90 degrees
        # https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
        rotated = [list(elem) for elem in zip(*current_array[::-1])]
        current_array = rotated
        count += count_xmas(current_array)
        count += count_xmas(rotate_45(current_array))

    return count


def part_2(matrix: list[list[str]]) -> int:
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for y in range(1, rows - 1):
        for x in range(1, cols - 1):
            if matrix[y][x] != "A":
                continue

            top_left = matrix[y - 1][x - 1]
            top_right = matrix[y - 1][x + 1]
            bottom_left = matrix[y + 1][x - 1]
            bottom_right = matrix[y + 1][x + 1]

            if (
                MAS_MAP.get(top_left) != bottom_right
                or MAS_MAP.get(bottom_left) != top_right
            ):
                continue

            count += 1

    return count


if __name__ == "__main__":
    input_path = "../input/day04"
    with open(input_path, "r", encoding="utf-8") as f:
        input_ = list(f)

    matrix = [list(line) for line in input_]
    # matrix = [list(line) for line in INPUT.split("\n")]

    print("Part 1:")
    print(part_1(matrix))

    print("Part 2:")
    print(part_2(matrix))
