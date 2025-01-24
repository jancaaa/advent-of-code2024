def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        grid = []
        while line:
            line = line.rstrip()
            line = [x for x in line]
            grid.append(line)
            line = fp.readline()
        return grid


def find_start_position(grid: list):
    for row_index, row in enumerate(grid):
        for col_index, value in enumerate(row):
            if value == "^":
                return row_index, col_index
    return None


def part1(grid: list) -> int:
    start = find_start_position(grid)
    r, c = start
    dr = -1
    dc = 0
    grid[r][c] = "X"

    len_r = len(grid)
    len_c = len(grid[0])

    while 0 < r < len_r - 1 and 0 < c < len_c - 1:
        if grid[r + dr][c + dc] == "#":
            ndr = dc
            ndc = -dr
            dr = ndr
            dc = ndc

        c = c + dc
        r = r + dr
        grid[r][c] = "X"

    count = 0
    for c in range(len(grid)):
        for r in range(len(grid[0])):
            if grid[c][r] == "X":
                count += 1
    return count


def part2(grid: list) -> int:
    return


if __name__ == "__main__":
    grid = read_file()
    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")
