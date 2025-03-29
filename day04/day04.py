def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            line = line.rstrip()
            entries.append(list(line))
            line = fp.readline()
        return entries


def part1(matrix: list) -> int:
    count = 0
    # rows
    for e in matrix:
        count += get_xmas_count(e)

    # columns
    for e in [list(column) for column in zip(*matrix)]:
        count += get_xmas_count(e)

    # diagonals
    for e in get_all_diagonals(matrix):
        count += get_xmas_count(e)

    return count


def part2(matrix: list) -> int:
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):

            if matrix[r][c] == "A":
                x1 = matrix[r - 1][c - 1] + matrix[r][c] + matrix[r + 1][c + 1]
                x2 = matrix[r + 1][c - 1] + matrix[r][c] + matrix[r - 1][c + 1]

                if is_mas(x1) and is_mas(x2):
                    count += 1

    return count


def get_all_diagonals(matrix: list) -> list:
    rows = len(matrix)
    cols = len(matrix[0])
    diagonals = []

    # diagonals from top row - right
    for col in range(cols):
        diagonal = []
        i, j = 0, col

        while i < rows and j < cols:
            diagonal.append(matrix[i][j])
            i += 1
            j += 1
        diagonals.append(diagonal)

    # diagonals from top row - left
    for col in range(cols):
        diagonal = []
        i, j = 0, col
        while i < rows and j >= 0:
            diagonal.append(matrix[i][j])
            i += 1
            j -= 1
        diagonals.append(diagonal)

    # diagonals from left column (except corner) - down
    for start_row in range(1, rows):
        diagonal = []
        row, col = start_row, 0
        while row < rows and col < cols:
            diagonal.append(matrix[row][col])
            row += 1
            col += 1
        diagonals.append(diagonal)

    # diagonals from right column (except corner) - down
    for start_row in range(1, rows):
        diagonal = []
        row, col = start_row, cols - 1
        while row < rows and col < cols:
            diagonal.append(matrix[row][col])
            row += 1
            col -= 1
        diagonals.append(diagonal)

    return diagonals


def get_xmas_count(e: list) -> int:
    count = 0
    row = ''.join(e)
    count += row.count("XMAS")
    count += row.count("SAMX")
    return count


def is_mas(x: str) -> bool:
    return x == "MAS" or x == "SAM"


def print2d(matrix):
    for e in matrix:
        print(e)
    print()


if __name__ == "__main__":
    matrix = read_file()
    # print2d(matrix)

    print(f"Part 1: {part1(matrix)}")
    print(f"Part 2: {part2(matrix)}")
