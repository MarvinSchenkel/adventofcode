import collections
import sys
import numpy as np


def read_input(filename: str):
    with open(filename, "r") as f:
        return [x.rstrip() for x in f.readlines()]


def get_input():
    lines = read_input("src/aoc/12/12.txt")
    return [[i for i in l] for l in lines]


def print_grid(height, width, path):
    np.set_printoptions(suppress=True,linewidth=sys.maxsize,threshold=sys.maxsize)
    pgrid = np.full((height, width), "...")
    for idx, (x, y) in enumerate(path):
        pgrid[y][x] = (f"...{idx}")[-3:]
        if idx==421:
            print(f"{x}. {y}")
    # Transpose because the grid is pretty wide
    print(pgrid.transpose())


def bfs(grid, start):
    queue = collections.deque([[start]])
    height, width = len(grid), len(grid[0])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        cur_val = ord("a") if grid[y][x] == "S" else ord(grid[y][x])
        if grid[y][x] == "E":
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and (x2, y2) and (x2, y2) not in seen:
                targ_val = ord("z") if grid[y2][x2] == "E" else ord(grid[y2][x2])
                if (cur_val >= targ_val or cur_val + 1 == targ_val):
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))


def run():
    grid = get_input()
    y, x = np.where(np.array(grid) == "S")
    route = bfs(grid, start=(x[0], y[0]))
    print(f"[1]: {len(route) - 1}")
    # Include part 1 route in all possible routes for part 2
    all_routes = [route]
    # Part 2
    y2, x2 = np.where(np.array(grid) == "a")
    for (x3, y3) in zip(x2, y2):
        new_route = bfs(grid, start=(x3, y3))
        if new_route:
            all_routes.append(new_route) 
    p2 = min([len(r) for r in all_routes]) - 1
    print(f"[2]: {p2}")


def main():
    run()


if __name__ == "__main__":
    main()