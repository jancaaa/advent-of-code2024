def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []
        while line:
            line = line.rstrip()
            sum, numbers = line.split(": ")
            sum = int(sum)
            numbers = [int(n) for n in numbers.split(" ")]
            entries.append((sum, numbers))
            line = fp.readline()
        return entries


def evaluate1(result, numbers: list) -> bool:
    sum = numbers[0] + numbers[1]
    multiply = numbers[0] * numbers[1]
    if len(numbers) == 2:
        return sum == result or multiply == result
    else:
        return evaluate1(result, [sum] + numbers[2:]) or evaluate1(result, [multiply] + numbers[2:])


def evaluate2(result, numbers: list) -> bool:
    sum = numbers[0] + numbers[1]
    multiply = numbers[0] * numbers[1]
    concat = int(str(numbers[0]) + str(numbers[1]))
    if len(numbers) == 2:
        return sum == result or multiply == result or concat == result
    else:
        return evaluate2(result, [sum] + numbers[2:]) or evaluate2(result, [multiply] + numbers[2:]) or evaluate2(result, [concat] + numbers[2:])


def part1(entries: list) -> int:
    total = 0
    for e in entries:
        sum, numbers = e
        if evaluate1(sum, numbers):
            total += sum
    return total


def part2(entries: list) -> int:
    total = 0
    for e in entries:
        sum, numbers = e
        if evaluate2(sum, numbers):
            total += sum
    return total


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
