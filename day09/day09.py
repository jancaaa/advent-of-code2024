def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        id = 0
        for x in line:
            x = int(x)
            if id % 1 == 0:
                a = int(id)
            else:
                a = "."
            for i in range(x):
                entries.append(a)
            id += 0.5

        return entries


def part1(entries: list) -> int:
    while '.' in entries:
        first_dot_index = entries.index('.')
        last_number = entries.pop(-1)
        entries[first_dot_index] = last_number

    sum = 0
    for e, i in enumerate(entries):
        sum += e * i
    return sum


def part2(entries: list) -> int:
    return


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    # print(f"Part 2: {part2(entries)}")
