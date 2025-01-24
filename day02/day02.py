def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            line = line.rstrip()
            line = [int(x) for x in line.split(" ")]
            entries.append(line)
            line = fp.readline()
        return entries


def part1(entries: list) -> int:
    count = 0
    for e in entries:
        if is_safe(e):
            count += 1
    return count


def part2(entries: list) -> int:
    count = 0
    for e in entries:
        if is_safe(e):
            count += 1
        else:
            for i in range(len(e)):
                copy = e.copy()
                copy.pop(i)
                if is_safe(copy):
                    count += 1
                    break
    return count


def is_safe(e):
    sorted_asc = e == sorted(e)
    sorted_desc = e == sorted(e, reverse=True)

    if sorted_asc or sorted_desc:
        for i in range(len(e) - 1):
            d = abs(e[i] - e[i + 1])
            if d < 1 or d > 3:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
