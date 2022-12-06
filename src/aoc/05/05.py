def read_input(filename: str):
    with open(filename, "r") as f:
        return [x.rstrip() for x in f.readlines()]

def parse_input(lines: list[str]):
    # Parse the stacks first
    stack_lines = []
    for stack_line in lines:
        if stack_line in ["\n", "\r\n", ""]:
            break
        stack_lines.append(stack_line)
    # Read stack lines in reverse to build the stacks
    stacks = {}
    for idx, stack_line in enumerate(reversed(stack_lines)):
        if idx == 0:
            stack_indexes = [int(stack_line[i:i+3]) for i in range(0, len(stack_line), 4)]
            stacks = {s : [] for s in stack_indexes}
        else:
            crates = [stack_line[i:i+3] for i in range(0, len(stack_line), 4)]
            for idx, crate in enumerate(crates, start=1):
                clean_crate = str(crate).replace("[", "").replace("]", "").strip()
                if clean_crate:
                    stacks[idx].append(clean_crate)
    # Parse the instructions after
    instructions = [(int(i.split(" ")[1]), int(i.split(" ")[3]), int(i.split(" ")[5])) for i in lines[len(stack_lines)+1:] if i]
    return stacks, instructions

def execute_instructions(stacks, instructions):
    for inst in instructions:
        for _ in range(0, inst[0]):
            stacks[inst[2]].append(stacks[inst[1]].pop())
    return stacks

def execute_instructions_multi(stacks, instructions):
    for inst in instructions:
        crates = []
        for _ in range(0, inst[0]):
            crates.append(stacks[inst[1]].pop())
        stacks[inst[2]].extend(list(reversed(crates)))
    return stacks

def one():
    lines = read_input("src/aoc/05/05.txt")
    stacks, instructions = parse_input(lines)
    end_stacks = execute_instructions(stacks, instructions)
    top_crates = "".join([x.pop() for k, x in end_stacks.items()])
    print(f"[1] {top_crates}")


def two():
    lines = read_input("src/aoc/05/05.txt")
    stacks, instructions = parse_input(lines)
    end_stacks = execute_instructions_multi(stacks, instructions)
    top_crates = "".join([x.pop() for k, x in end_stacks.items()])
    print(f"[1] {top_crates}")


def main():
    one()
    two()


if __name__ == "__main__":
    main()