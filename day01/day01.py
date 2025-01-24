from typing import Tuple


def read_file() -> Tuple[list, list]:
    with open("input.txt") as fp:
        line = fp.readline()

        list1 = []
        list2 = []
        while line:
            line = line.rstrip()
            a, b = line.split("   ")
            list1.append(int(a))
            list2.append(int(b))
            line = fp.readline()
        return list1, list2


def part1(lists: Tuple[list, list]) -> int:
    list1, list2 = lists

    list1.sort()
    list2.sort()

    total = 0
    for i in range(len(list1)):
        dis = abs(list1[i] - list2[i])
        total += dis
    return total


def part2(lists: Tuple[list, list]) -> int:
    list1, list2 = lists
    score = 0
    for x in list1:
        c = list2.count(x)
        score += x * c
    return score


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
