import itertools
from typing import Tuple
from operator import sub
import numpy as np

def read_input(filename: str):
    with open(filename, "r") as f:
        return [x.rstrip() for x in f.readlines()]


def get_instructions():
    return list(line.split(" ") for line in read_input("src/aoc/10/10.txt"))


def run():
    instructions = get_instructions()
    X = 1
    cycles = 0
    signal_strenghts = []
    CRT = []
    for ins in instructions:
        for tick in range(2) if ins[0] == "addx" else range(1):
            cycles += 1
            signal_strenghts.append(cycles * X if cycles % 40 == 20 else 0)
            CRT += "#" if (cycles - 1) % 40 in (X-1, X, X+1) else "."
            if tick == 1:
                X += int(ins[1])
    print(f"[1]: {sum(signal_strenghts)}")
    print("[2]:")
    for idx in range(0, 240, 40):
        print("".join(CRT[idx:idx+40]))


def main():
    run()


if __name__ == "__main__":
    main()