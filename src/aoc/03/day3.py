from code import interact
from functools import reduce

def read_input(filename: str):
    with open(filename, "r") as f:
        return [x.rstrip() for x in f.readlines()]


def get_priority(character: str):
    return ord(character) - 96 if character.islower() else ord(character) - 38


def one():
    priorities = []
    for rucksack in read_input("src/aoc/03/day3.txt"):
        half = len(rucksack) // 2
        comp1 = rucksack[:half]
        comp2 = rucksack[half:]
        double_item = list(set(comp1).intersection(set(comp2)))[0]
        priorities.append(get_priority(double_item))
    print(f"[1]: {sum(priorities)}")


def two():
    rucksacks = read_input("src/aoc/03/day3.txt")
    groups = zip(*[rucksacks[i::3] for i in range(3)])
    common_items = [
        list(reduce(set.intersection, [set(r) for r in group_rucksacks]))[0]
        for group_rucksacks in groups
    ]
    priorities = [get_priority(i) for i in common_items]
    print(f"[2]: {sum(priorities)}")


def main():
    one()
    two()

if __name__ == "__main__":
    main()