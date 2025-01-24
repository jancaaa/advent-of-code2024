from collections import deque


def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        grid = []
        while line:
            line = line.rstrip()
            grid.append([int(x) for x in list(line)])
            line = fp.readline()
        return grid


def count_reachable(grid, x: int, y: int):
    queue = deque([(x, y, 0)])  # (row, col, current_value)
    visited = set()
    reachable_nines = set()

    while queue:
        row, col, value = queue.popleft()

        if (row, col) in visited:
            continue
        visited.add((row, col))

        if value == 9:
            reachable_nines.add((row, col))
            continue

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                if grid[new_row][new_col] == value + 1:
                    queue.append((new_row, new_col, value + 1))

    return len(reachable_nines)


def count_paths(grid, x: int, y: int):
    if grid[x][y] == 9:
        return 1

    total_paths = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # up, down, left, right
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == grid[x][y] + 1:
            total_paths += count_paths(grid, nx, ny)

    return total_paths


def part1(grid: list) -> int:
    score = 0
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                score += count_reachable(grid, r, c)
    return score


def part2(grid: list) -> int:
    score = 0
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                score += count_paths(grid, r, c)
    return score


if __name__ == "__main__":
    grid = read_file()
    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")
