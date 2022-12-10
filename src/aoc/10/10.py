import itertools
from typing import Tuple
from operator import sub
import numpy as np

def read_input(filename: str):
    with open(filename, "r") as f:
        return [x.rstrip() for x in f.readlines()]

def parse_instructions(instructions: list[str]):
    return list(line.split(" ") for line in read_input())


def check_signal_strength(cycle, X):
    return cycle * X if cycle in [20, 60, 100, 140, 180, 220] else 0


def one():
    instructions = list(line.split(" ") for line in read_input("src/aoc/10/10.txt"))
    X = 1
    cycles = 0
    signal_strenghts = []
    for ins in instructions:
        if ins[0] == "noop":
            cycles += 1
            signal_strenghts.append(check_signal_strength(cycles, X))
        elif ins[0] == "addx":
            cycles += 1
            signal_strenghts.append(check_signal_strength(cycles, X))
            cycles += 1
            signal_strenghts.append(check_signal_strength(cycles, X))
            X += int(ins[1])
    print(f"[1]: {sum(signal_strenghts)}")
    

def draw(pos, X):
    return "#" if pos % 40 in [X-1, X, X+1] else "."


def two():
    instructions = list(line.split(" ") for line in read_input("src/aoc/10/10.txt"))
    X = 1
    cycles = 0
    CRT = []
    for ins in instructions:
        if ins[0] == "noop":
            cycles += 1
            CRT += draw(cycles - 1, X)
        elif ins[0] == "addx":
            cycles += 1
            CRT += draw(cycles - 1, X)
            cycles += 1
            CRT += draw(cycles - 1, X)
            X += int(ins[1])
    print("[2]:")
    for idx in range(0, 240, 40):
        print("".join(CRT[idx:idx+40]))

def main():
    one()
    two()


if __name__ == "__main__":
    main()