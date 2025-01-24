def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        line = line.rstrip()
        line = line.split(" ")
        stones = [int(x) for x in line]
        return stones


def part1(stones: list) -> int:
    for i in range(25):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                stone = str(stone)
                mid = len(stone) // 2
                new_stones.append(int(stone[:mid]))
                new_stones.append(int(stone[mid:]))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)


def add_occurrence(stone: int, count: int, occurrences: dict) -> dict:
    if stone in occurrences:
        occurrences[stone] += count
    else:
        occurrences[stone] = count
    return occurrences


def part2(stones: list) -> int:
    occurrences = {}
    for stone in stones:
        occurrences = add_occurrence(stone, 1, occurrences)

    for i in range(75):
        new_occurrences = {}
        for stone, count in occurrences.items():
            if stone == 0:
                new_occurrences = add_occurrence(1, count, new_occurrences)
            elif len(str(stone)) % 2 == 0:
                stone = str(stone)
                mid = len(stone) // 2
                new_occurrences = add_occurrence(int(stone[:mid]), count, new_occurrences)
                new_occurrences = add_occurrence(int(stone[mid:]), count, new_occurrences)
            else:
                new_occurrences = add_occurrence(stone * 2024, count, new_occurrences)
        occurrences = new_occurrences

    return sum(occurrences.values())


if __name__ == "__main__":
    stones = read_file()
    print(f"Part 1: {part1(stones)}")
    print(f"Part 2: {part2(stones)}")
