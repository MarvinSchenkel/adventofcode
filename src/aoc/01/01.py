def read_input(filename: str):
    with open(filename, "r") as f:
        return [x.rstrip() for x in f.readlines()]

def main():
    # Keep track of the calories of each elf
    elfs = []
    total_calories = 0
    for line in read_input("src/aoc/01/01.txt"):
        if not line:
            elfs.append(total_calories)
            total_calories = 0
            continue
        total_calories += int(line)
    print(f"[1]: {max(elfs)}")
    print(f"[2]: {sum(sorted(elfs, reverse=True)[:3])}")

if __name__ == "__main__":
    main()