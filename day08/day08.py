from typing import Tuple


class Grid:

    def __init__(self, antennas: dict, size_x: int, size_y: int) -> None:
        super().__init__()
        self.antennas = antennas
        self.size_x = size_x
        self.size_y = size_y


def read_file():
    with open("input.txt") as fp:
        line = fp.readline()
        antennas = dict()
        y = 0

        while line:
            line = line.rstrip()
            line = [x for x in line]
            size_x = len(line)  # row length
            for x, a in enumerate(line):
                if a not in antennas.keys():
                    antennas[a] = list()

                p = (x, y)
                antennas[a].append(p)
            line = fp.readline()
            y += 1

        antennas.pop(".")  # space representation
        size_y = y  # row count
        return Grid(antennas, size_x, size_y)


def get_antinodes(g, grid):
    x_max = len(grid)
    y_max = len(grid[0])
    antinodes = set()
    for k, vi in g.items():
        print(k, vi)
        for ix, x in enumerate(vi):
            for y in vi[ix + 1:]:
                xx, yx = x
                xy, yy = y
                v = (xx - xy, yx - yy)
                dx, dy = v
                a1x = xx + dx
                a1y = yx + dy
                a2x = xy - dx
                a2y = yy - dy
                print(x, y, v, (a1x, a1y), (a2x, a2y))
                if a1x >= 0 and a1x < x_max and a1y >= 0 and a1y < y_max:
                    antinodes.add((a1x, a1y))
                if a2x >= 0 and a2x < x_max and a2y >= 0 and a2y < y_max:
                    antinodes.add((a2x, a2y))


def get_v(x: Tuple[int, int], y: Tuple[int, int]) -> Tuple[int, int]:
    xx, yx = x
    xy, yy = y
    dx = xx - xy
    dy = yx - yy
    return dx, dy


def get_antinode(antenna: Tuple[int, int], v: Tuple[int, int], coef: int) -> Tuple[int, int]:
    x, y = antenna
    dx, dy = v
    dx *= coef
    dy *= coef

    return x + dx, y + dy


def is_valid(antinode: Tuple[int, int], grid: Grid) -> bool:
    x, y = antinode
    return 0 <= x < grid.size_x and 0 <= y < grid.size_y


def part1(grid: Grid) -> int:
    antinodes = set()
    for k, antennas in grid.antennas.items():
        for i, x in enumerate(antennas):
            for y in antennas[i + 1:]:
                # calculate v for each couple of antennas
                v = get_v(x, y)
                a1 = get_antinode(x, v, 1)
                a2 = get_antinode(y, v, -1)

                if is_valid(a1, grid):
                    antinodes.add(a1)
                if is_valid(a2, grid):
                    antinodes.add(a2)

    return len(antinodes)


def part2(grid: Grid) -> int:
    antinodes = set()
    for k, antennas in grid.antennas.items():
        for i, x in enumerate(antennas):
            for y in antennas[i + 1:]:
                # antennas are also antinodes
                antinodes.add(x)
                antinodes.add(y)

                # calculate v for each couple of antennas
                v = get_v(x, y)
                a1 = get_antinode(x, v, 1)
                a2 = get_antinode(y, v, -1)

                while is_valid(a1, grid):
                    antinodes.add(a1)
                    a1 = get_antinode(a1, v, 1)

                while is_valid(a2, grid):
                    antinodes.add(a2)
                    a2 = get_antinode(a2, v, -1)

    return len(antinodes)


if __name__ == "__main__":
    grid = read_file()
    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")
