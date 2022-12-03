from helpers.utils import read_input

def main():
    # Keep track of the calories of each elf
    elfs = []
    total_calories = 0
    for line in read_input("day1.txt"):
        if not line:
            elfs.append(total_calories)
            total_calories = 0
            continue
        total_calories += int(line)
    print(f"[1]: {max(elfs)}")
    print(f"[2]: {sum(sorted(elfs, reverse=True)[:3])}")

if __name__ == "__main__":
    main()