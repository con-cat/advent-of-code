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


def count_xmas(matrix: list[list[str]]) -> int:
    count = 0
    for row in matrix:
        for i, char in enumerate(row):
            if row[i : i + 4] == XMAS:
                count += 1

    return count


def rotate_45(matrix: list[list[str]]) -> list[list[str]]:
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


if __name__ == "__main__":
    input_path = "../input/day04"
    with open(input_path, "r", encoding="utf-8") as f:
        input_ = list(f)

    matrix = [list(line) for line in input_]

    print("Part 1:")
    print(part_1(matrix))
