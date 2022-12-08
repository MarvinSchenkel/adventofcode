def read_input(filename: str):
    with open(filename, "r") as f:
        return [x.rstrip() for x in f.readlines()]


def solve():
    fs = {}
    cwd = "/"
    folder_contents = []
    processing_output = False
    lines = read_input("src/aoc/07/07.txt")[1:]
    for idx, line in enumerate(lines, start=1):
        # Processing output
        if (line.startswith("$") or idx == len(lines)) and processing_output:
            fs[cwd] = folder_contents
            processing_output = False
        # Parse command
        if line.startswith("$ cd "):
            argument = line.split("$ cd ")[1]
            if argument == "..":
                cwd = cwd[0:cwd[:-1].rfind("/")+1]
            else:
                cwd += f"{argument}/"
        # Parse ls
        elif line == "$ ls":
            folder_contents = []
            processing_output = True
        elif line.startswith("dir"):
            pass
        # Parse output
        else:
            folder_contents.append(tuple(line.split(" ")))
    directory_sizes = {}
    for folder, contents in fs.items():
        size = sum([int(i[0]) for i in contents])
        subfolders_size = 0
        for subfolder, subfolder_contents in fs.items():
            if subfolder.startswith(folder) and subfolder != folder:
                subfolders_size += sum([int(j[0]) for j in subfolder_contents])
        directory_sizes[folder] = (size + subfolders_size)
    print(f"[1]: {sum([s for _, s in directory_sizes.items() if s <= 100_000])}")
    unused_space = 70_000_000 - directory_sizes["/"]
    print(f"[2]: {min([s for _, s in directory_sizes.items() if unused_space + s >= 30_000_000])}")


def main():
    solve()


if __name__ == "__main__":
    main()