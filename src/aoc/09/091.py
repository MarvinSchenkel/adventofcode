import numpy as np

def read_input_file(path, output_type='string'):
    with open(path, 'r') as f:
        input_str = f.read()
    if output_type == 'string':

        input_content = input_str[:-1]  # drop \n
    elif output_type == 'list':
        input_content = input_str.split('\n')[:-1]  # drop empty last line
    else:
        raise ValueError('Unknown output_type {}. Expected string or list.'.format(output_type))
    return input_content

input_list = read_input_file(path='src/aoc/09/09.txt', output_type='list')

instruction_list = [(line[0], int(line[2:])) for line in input_list]

DIRECTION_MAP = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}


def print_visited(visited, minx=0, miny=0, maxx=6, maxy=5):
    for y in reversed(range(miny, maxy)):
        for x in range(minx, maxx):
            print(' ', end='')
            if (x, y) in visited:
                print('#', end='')
            else:
                print('.', end='')
        print('')


def print_knots(knots, minx=0, miny=0, maxx=6, maxy=5):
    for y in reversed(range(miny, maxy)):
        for x in range(minx, maxx):
            print(' ', end='')
            printed = False
            for i, knot in enumerate(knots):
                if (x, y) == tuple(knot):
                    print(i, end='')
                    printed = True
                    break
            if not printed:
                print('.', end='')
        print('')
    print('\n')


def part_one(instructions):
    head = np.array((0., 0.))
    tail = np.array((0., 0.))
    visited = set()
    for direction, n_steps in instructions:
        step = DIRECTION_MAP[direction]
        for i in range(n_steps):
            head += step
            tail = get_tail(head, tail)
            visited.add(tuple(tail))
    print(head)
    print(tail)
    print(len(visited))


def get_tail(head, tail):
    if np.linalg.norm(head - tail) > np.sqrt(2):
        dx, dy = head - tail
        if abs(dx) > 1 or (abs(dx) == 1 and abs(dy) > 1):
            tail[0] += np.sign(dx)
        if abs(dy) or (abs(dy) == 1 and abs(dx) > 1):
            tail[1] += np.sign(dy)
    return tail


def part_two(instructions):
    knots = [np.array((0., 0.)) for _ in range(10)]  # init 9 knots on 0,0
    visited = set()
    for direction, n_steps in instructions:
        step = DIRECTION_MAP[direction]
        for i in range(n_steps):
            new_knots = []
            head = knots[0]
            head += step
            for tail in knots[1:]:
                tail = get_tail(head, tail)
                new_knots.append(head)
                head = tail  # set the current knot to the next head
            visited.add(tuple(head))
            new_knots.append(head)
            knots = new_knots
    print(len(visited))


part_one(instructions=instruction_list)
#part_two(instructions=instruction_list)