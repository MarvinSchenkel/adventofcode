def read_input(filename: str):
    with open(filename, "r") as f:
        return [x.rstrip() for x in f.readlines()]


def parse_cave(lines):
    rocks = set()
    for line in lines:
        coords = [list(map(int, x.split(","))) for x in line.split(" -> ")]
        for (x, y), (x_next, y_next) in zip(coords, coords[1:]):
            # Expand X
            if y == y_next:
                for x_new in range(0, abs(x_next - x) + 1):
                    rocks.add((min(x, x_next) + x_new, y))
            # Expand Y
            elif x == x_next:
                for yNew in range(0, abs(y_next - y) + 1):
                    rocks.add((x, min(y, y_next) + yNew))
    return rocks


def one(rocks):
    fallen_sand = set()
    min_x = min(r[0] for r in rocks)
    max_y = max(r[1] for r in rocks)
    done = False
    fallen_sand = 0
    while not done:
        s = (500, 0)
        while True:
            # Check if we hit the abyss
            if s[0] < min_x or s[1] + 1 > max_y:
                print(f"[1]: {fallen_sand}")
                done = True
                break
            # Keep falling down
            if (s[0], s[1] + 1) not in rocks:
                s = (s[0], s[1] + 1)
                continue
            # Check if we can go left
            if (s[0] - 1, s[1] + 1) not in rocks:
                s = (s[0] - 1, s[1])
                continue
            # Check if we can go right
            if (s[0] + 1, s[1] + 1) not in rocks:
                s = (s[0] + 1, s[1])
                continue
            # Place sand
            rocks.add(s)
            fallen_sand += 1
            break


def two(rocks):
    fallen_sand = 0
    max_y = max(r[1] for r in rocks)
    floor = max_y + 2
    # Add the floor
    while (500, 0) not in rocks:
        s = (500, 0)
        while True:
            # Keep falling down
            if (s[0], s[1] + 1) not in rocks and s[1] + 1 != floor:
                s = (s[0], s[1] + 1)
                continue
            # Check if we can go left
            if (s[0] - 1, s[1] + 1) not in rocks and s[1] + 1 != floor:
                s = (s[0] - 1, s[1])
                continue
            # Check if we can go right
            if (s[0] + 1, s[1] + 1) not in rocks and s[1] + 1 != floor:
                s = (s[0] + 1, s[1])
                continue
            # Place sand
            rocks.add(s)
            fallen_sand += 1
            break
    print(f"[2]: {fallen_sand}")


def run():
    lines = read_input("src/aoc/14/14.txt")
    rocks = parse_cave(lines)
    one(rocks.copy())
    two(rocks)


def main():
    run()


if __name__ == "__main__":
    main()



