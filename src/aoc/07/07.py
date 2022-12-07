def read_input(filename: str):
    with open(filename, "r") as f:
        return [x.rstrip() for x in f.readlines()]


def solve():
    filesystem = {}
    current_directory = "/"
    folder_contents = []
    processing_output = False
    lines = read_input("src/aoc/07/07.txt")[1:]
    for idx, line in enumerate(lines, start=1):
        # Processing output
        if (line.startswith("$") or idx == len(lines)) and processing_output:
            filesystem[current_directory] = folder_contents
            processing_output = False
        # Parse command
        if line.startswith("$ cd "):
            argument = line.split("$ cd ")[1]
            if argument == "..":
                current_directory = current_directory[0:current_directory[:-1].rfind("/")+1]
            else:
                current_directory += f"{argument}/"
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
    for folder, contents in filesystem.items():
        size = sum([int(i[0]) for i in contents])
        subfolders_size = 0
        for subfolder, subfolder_contents in filesystem.items():
            if subfolder.startswith(folder) and subfolder != folder:
                subfolders_size += sum([int(j[0]) for j in subfolder_contents])
        directory_sizes[folder] = (size + subfolders_size)
    print(f"[1]: {sum([s for _, s in directory_sizes.items() if s <= 100000])}")
    unused_space = 70000000 - directory_sizes["/"]
    print(f"[2]: {min([s for _, s in directory_sizes.items() if unused_space + s >= 30000000])}")


def main():
    solve()


if __name__ == "__main__":
    main()