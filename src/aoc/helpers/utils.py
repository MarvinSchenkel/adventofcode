def read_input(filename: str):
    with open(filename, "r") as f:
        return [x.rstrip() for x in f.readlines()]


