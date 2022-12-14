import itertools
import numpy as np

def read_input(filename: str):
    with open(filename, "r") as f:
        return [x.rstrip() for x in f.readlines()]

def get_visible_trees(grid):
    visible_grid = np.empty_like(grid)
    for (x, y), value in np.ndenumerate(grid):
        if y == 0 or y + 1 == grid.shape[1] or value > max(grid[x, :y]) or value > max(grid[x, y+1:]):
            visible_grid[x][y] = True
        else:
            visible_grid[x][y] = False
    return visible_grid

def get_viewing_distances(grid):
    distance_grid = np.empty_like(grid)
    for (x, y), value in np.ndenumerate(grid):
        left_trees = list(reversed(grid[x, :y]))
        left_distance = (np.argmax(left_trees >= value) + 1 if np.max(left_trees) >= value else len(left_trees)) if len(left_trees) > 0 else 0
        right_trees = grid[x, y+1:]
        right_distance = (np.argmax(right_trees >= value) + 1 if np.max(right_trees) >= value else len(right_trees)) if len(right_trees) > 0 else 0
        distance_grid[x, y] = left_distance * right_distance
    return distance_grid

def one():
    grid = np.array([[int(i) for i in line] for line in read_input("src/aoc/08/08.txt")])
    horizontal_grid = get_visible_trees(grid)
    vertical_grid = np.transpose(get_visible_trees(np.transpose(grid)))
    visible_trees = horizontal_grid | vertical_grid
    print(f"[1]: {visible_trees.sum()}")

def two():
    grid = np.array([[int(i) for i in line] for line in read_input("src/aoc/08/08.txt")])
    horizontal_grid = get_viewing_distances(grid)
    vertical_grid = np.transpose(get_viewing_distances(np.transpose(grid)))
    viewing_distance_grid = np.multiply(horizontal_grid, vertical_grid)
    print(f"[2]: {viewing_distance_grid.max()}")

def main():
    one()
    two()


if __name__ == "__main__":
    main()