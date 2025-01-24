import re


def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            line = line.rstrip()
            entries.append(line)
            line = fp.readline()
        return entries


def part1(entries: list) -> int:
    total = 0
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    for e in entries:
        matches = re.findall(pattern, e)
        for m in matches:
            total += mul(m)
    return total


def part2(entries: list) -> int:
    pattern = r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"
    is_enabled = True
    total = 0
    for e in entries:
        matches = re.findall(pattern, e)
        for m in matches:
            if m == "do()":
                is_enabled = True
            elif m == "don't()":
                is_enabled = False
            else:
                if is_enabled:
                    total += mul(m)
    return total


def mul(m: str) -> int:
    m = m[4:-1]
    x, y = m.split(",")
    return int(x) * int(y)


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
