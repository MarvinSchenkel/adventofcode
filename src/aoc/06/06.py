def read_input(filename: str):
    with open(filename, "r") as f:
        return [x.rstrip() for x in f.readlines()]

def find_message_marker(line: str, no_chars: int):
    processed_chars = []
    for char in line:
        processed_chars.append(char)
        if len(processed_chars) > no_chars - 1 and len(set(processed_chars[-no_chars:])) == len(processed_chars[-no_chars:]):
            print(f"Found: {processed_chars[-no_chars:]}")
            break
    return len(processed_chars)


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