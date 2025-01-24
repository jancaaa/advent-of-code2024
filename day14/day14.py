class Robot:

    def __init__(self, x: str, y: str, vx: str, vy: str) -> None:
        self.x = int(x)
        self.y = int(y)
        self.vx = int(vx)
        self.vy = int(vy)

    def __str__(self) -> str:
        attrs = vars(self)
        return ', '.join("%s: %s" % item for item in attrs.items())


def read_file() -> list:
    with open("input.txt") as fp:
        line = fp.readline()
        robots = []
        while line:
            line = line.rstrip()
            p, v = line.split(" ")
            px, py = p[2:].split(",")
            vx, vy = v[2:].split(",")
            robots.append(Robot(px, py, vx, vy))
            line = fp.readline()
        return robots


def part1(robots: list) -> int:
    x_max = 100
    y_max = 102

    for i in range(100):
        for e in robots:
            new_x = e.x + e.vx
            new_y = e.y + e.vy
            if new_x < 0:
                e.x = new_x + x_max + 1
            elif new_x > x_max:
                e.x = new_x - x_max - 1
            else:
                e.x = new_x
            if new_y < 0:
                e.y = new_y + y_max + 1
            elif new_y > y_max:
                e.y = new_y - y_max - 1
            else:
                e.y = new_y

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    x_div = x_max // 2
    y_div = y_max // 2
    for e in robots:
        if e.x < x_div and e.y < y_div:
            q1 += 1
        elif e.x > x_div and e.y < y_div:
            q2 += 1
        elif e.x < x_div and e.y > y_div:
            q3 += 1
        elif e.x > x_div and e.y > y_div:
            q4 += 1
    return q1 * q2 * q3 * q4


def part2(robots: list) -> int:
    return


if __name__ == "__main__":
    robots = read_file()
    print(f"Part 1: {part1(robots)}")
    print(f"Part 2: {part2(robots)}")
