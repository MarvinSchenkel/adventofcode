def read_input(filename: str):
    with open(filename, "r") as f:
        return [x.rstrip() for x in f.readlines()]


def get_input():
    return read_input("src/aoc/13/13.txt")


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    if isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    if isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    for l, r in zip(left, right):
        if comp := compare(l, r):
            return comp
    return len(left) - len(right)


def run():
    lines = get_input()
    pairs = {}
    for idx in range(0, (len(lines) + 1) // 3):
        pair_idx = idx * 3
        left, right = lines[pair_idx], lines[pair_idx + 1]
        pairs[idx + 1] = (list(eval(left)), list(eval(right))) # I know, I don't like eval either
    # Part 1
    right_order_pairs = [k for k, v in pairs.items() if compare(v[0], v[1]) < 0]
    print(f"[1]: {sum(right_order_pairs)}")
    # Part 2, just compare fixed values and keep track of how many values come before the desired indexes
    idx = [1, 2]
    for (l, r) in pairs.values():
        if compare(l, [[2]]) < 0:
            idx[0] += 1
            idx[1] += 1
        elif compare(l, [[6]]) < 0:
            idx[1] += 1
        if compare(r, [[2]]) < 0:
            idx[0] += 1
            idx[1] += 1
        elif compare(r, [[6]]) < 0:
            idx[1] += 1
    print(f"[2]: {idx[0] * idx[1]}")


def main():
    run()


if __name__ == "__main__":
    main()