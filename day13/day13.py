import re
from typing import List, Tuple, Optional


class Button:

    def __init__(self, button_config) -> None:
        super().__init__()
        pattern = r"X\+(\d+), Y\+(\d+)"
        match = re.search(pattern, button_config)
        self.x = int(match.group(1))
        self.y = int(match.group(2))

    def __str__(self):
        return f"Button({self.x},{self.y})"


class Prize:

    def __init__(self, prize_config) -> None:
        super().__init__()
        pattern = r"X=(\d+),\s*Y=(\d+)"
        match = re.search(pattern, prize_config)
        self.x = int(match.group(1))
        self.y = int(match.group(2))

    def __str__(self):
        return f"Prize({self.x},{self.y})"


class Machine:

    def __init__(self, button_a, button_b, prize) -> None:
        super().__init__()
        self.button_a = Button(button_a)
        self.button_b = Button(button_b)
        self.prize = Prize(prize)

    def __str__(self) -> str:
        return f"Machine({self.button_a}, {self.button_b}, {self.prize})"


def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        entries = []

        while line:
            button_a = line.rstrip()
            line = fp.readline()

            button_b = line.rstrip()
            line = fp.readline()

            prize = line.rstrip()
            line = fp.readline()  # nl divider

            machine = Machine(button_a, button_b, prize)

            entries.append(machine)
            line = fp.readline()
        return entries


def find_solution_bf(machine: Machine) -> Optional[Tuple[int, int]]:
    for y in range(100):
        for x in range(100):
            if machine.button_a.x * x + machine.button_b.x * y == machine.prize.x and machine.button_a.y * x + machine.button_b.y * y == machine.prize.y:
                return x, y
    return None


def find_solution(m: Machine) -> Optional[Tuple[int, int]]:
    d = m.button_a.x * m.button_b.y - m.button_a.y * m.button_b.x
    dx = m.prize.x * m.button_b.y - m.prize.y * m.button_b.x
    dy = m.button_a.x * m.prize.y - m.button_a.y * m.prize.x
    if not d == 0:
        x = dx / d
        y = dy / d
        if dx % d == 0 and dy % d == 0:
            return int(x), int(y)
    return None


def part1(machines: List[Machine]) -> int:
    tokens = 0
    for m in machines:
        solution = find_solution_bf(m)
        if solution:
            a, b = solution
            tokens += 3 * a
            tokens += b

    return tokens


def part2(machines: List[Machine]) -> int:
    tokens = 0
    for m in machines:
        m.prize.x += 10000000000000
        m.prize.y += 10000000000000
        solution = find_solution(m)

        if solution:
            x, y = solution
            tokens += 3 * x
            tokens += y

    return tokens


if __name__ == "__main__":
    entries = read_file()
    print(f"Part 1: {part1(entries)}")
    print(f"Part 2: {part2(entries)}")
