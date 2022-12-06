def read_input(filename: str):
    with open(filename, "r") as f:
        return [x.rstrip() for x in f.readlines()]

def find_message_marker(message: str, no_chars: int):
    for i, char in enumerate(message):
        if i > no_chars - 1 and len(set(message[i-no_chars:i])) == no_chars:
            return i


def one():
    line = read_input("src/aoc/06/06.txt")
    marker = find_message_marker(line[0], 4)
    print(f"[1]: Processed {marker} chars")


def two():
    line = read_input("src/aoc/06/06.txt")
    marker = find_message_marker(line[0], 14)
    print(f"[2]: Processed {marker} chars")


def main():
    one()
    two()


if __name__ == "__main__":
    main()