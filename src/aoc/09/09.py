import itertools
from typing import Tuple
from operator import sub
import numpy as np

def read_input(filename: str):
    with open(filename, "r") as f:
        return [x.rstrip() for x in f.readlines()]

def get_new_head(head: Tuple[int, int], direction: str):
    match direction:
        case "R":
            return (head[0] + 1, head[1])
        case "L":
            return (head[0] - 1, head[1])
        case "U":
            return (head[0], head[1] + 1)
        case "D":
            return (head[0], head[1] - 1)


def sign(x):
    return (x > 0) - (x < 0)


def move(new_head: Tuple[int, int], tail: Tuple[int, int]):
    dx, dy = tuple(map(sub, new_head, tail))
    if np.linalg.norm(np.array(new_head) - np.array(tail)) > np.sqrt(2):
        if abs(dx) > 1 or (abs(dx) == 1 and abs(dy) > 1):
            tail = (tail[0] + sign(dx), tail[1])
        if abs(dy) or (abs(dy) == 1 and abs(dx) > 1):
            tail = (tail[0], tail[1] + sign(dy))
    return (new_head, tail)


def parse_instructions(instructions: list[str]):
    return list(itertools.chain.from_iterable([[*line[0] * int(line[2:])] for line in instructions]))


def one():
    inp = read_input("src/aoc/09/09.txt")
    instructions = parse_instructions(inp)
    head, tail = ((0, 0), (0, 0))
    tail_instructions = [tail]
    for ins in instructions:
        head = get_new_head(head, ins)
        head, tail = move(head, tail)
        tail_instructions.append(tail)
    print(f"[1]: {len(set(tail_instructions))}")


def two():
    inp = read_input("src/aoc/09/09.txt")
    instructions = parse_instructions(inp)
    knots = [(0, 0) for _ in range(10)]
    tail_instructions = [(0, 0)]
    for ins in instructions:
        knots[0] = get_new_head(knots[0], ins)
        for idx in range(len(knots[1:])):
            _, tail = move(knots[idx], knots[idx + 1])
            knots[idx + 1] = tail
        tail_instructions.append(knots[-1])
    print(f"[2]: {len(set(tail_instructions))}")


def main():
    one()
    two()


if __name__ == "__main__":
    main()