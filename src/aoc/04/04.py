def read_input(filename: str):
    with open(filename, "r") as f:
        return [x.rstrip() for x in f.readlines()]

def get_range(input: str):
    start, end = input.split("-")
    return set(range(int(start), int(end) + 1))

def one():
    overlaps = 0
    for elf_pair in read_input("src/aoc/04/04.txt"):
        first_elf = get_range(elf_pair.split(",")[0])
        second_elf = get_range(elf_pair.split(",")[1])
        overlaps = overlaps + 1 if first_elf <= second_elf or second_elf <= first_elf else overlaps
    print(f"[1]: {overlaps}")

def two():
    overlaps = 0
    for elf_pair in read_input("src/aoc/04/04.txt"):
        first_elf = get_range(elf_pair.split(",")[0])
        second_elf = get_range(elf_pair.split(",")[1])
        overlaps = overlaps + 1 if len(first_elf.intersection(second_elf)) > 0 or len(second_elf.intersection(first_elf)) > 0 else overlaps
    print(f"[2]: {overlaps}")


def main():
    one()
    two()

if __name__ == "__main__":
    main()