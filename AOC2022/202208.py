# AOC 2022 - Day 8

import time

IN_FILE = "AOC2022/202208.txt"
# IN_FILE = "AOC2022/202208.sample.txt"


def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        out = [(line) for line in f.read().split('\n')]
    return out

x_size = 0
y_size = 0
visible = []

def sum_trees(vis):
    total = 0
    for x in vis:
        total += sum(x)
    return total

def look_for_trees(p_i,vis):
    # left to right
    for x in range(x_size):
        previous = -1
        for y in range(y_size):
            if int(p_i[x][y]) > previous:
                vis[x][y] = 1
                previous = int(p_i[x][y])

    # top to bottom
    for y in range(y_size):
        previous = -1
        for x in range(x_size):
            if int(p_i[x][y]) > previous:
                vis[x][y] = 1
                previous = int(p_i[x][y])

    # right to left
    for x in range(x_size):
        previous = -1
        for y in range(y_size-1,0,-1):
            if int(p_i[x][y]) > previous:
                vis[x][y] = 1
                previous = int(p_i[x][y])

    # bottom to top
    for y in range(y_size):
        previous = -1
        for x in range(x_size-1,0,-1):
            if int(p_i[x][y]) > previous:
                vis[x][y] = 1
                previous = int(p_i[x][y])
    
    return vis

def view_score(x,y,p_i):
    if x == 0 or x == x_size - 1:
        return 0
    if y == 0 or y == y_size - 1:
        return 0

    score = 1
    my_height = int(p_i[x][y])

    # right from tree
    count = 0
    i = y + 1
    while i < y_size:
        count += 1
        if int(p_i[x][i]) >= my_height:
            break
        else:
            i += 1
    score *= count

    # down from tree
    count = 0
    i = x + 1
    while i < x_size:
        count += 1
        if int(p_i[i][y]) >= my_height:
            break
        else:
            i += 1
    score *= count

    # left from tree
    count = 0
    i = y - 1
    while i >= 0:
        count += 1
        if int(p_i[x][i]) >= my_height:
            break
        else:
            i -= 1
    score *= count

    # up from tree
    count = 0
    i = x - 1
    while i >= 0:
        count += 1
        if int(p_i[i][y]) >= my_height:
            break
        else:
            i -= 1
    score *= count

    return score


def part1(data):            # => 1782
    """Solve part 1."""
    look_for_trees(data,visible)
    return sum_trees(visible)

def part2(data):            # => 474606
    """Solve part 2."""
    high_score = 0
    for x in range(x_size):
        for y in range(y_size):
            this_score = view_score(x,y,data)
            if this_score > high_score:
                high_score = this_score
    return high_score

def create_empty_visible(x,y):
    return [[0] * x for _ in range(y)]

if __name__ == "__main__":
    timestart = time.time()
    
    puzzle_input = parse()
    # print(puzzle_input)
    y_size = len(puzzle_input)
    x_size = len(puzzle_input[0])
    # print("size: ",x_size,y_size)
    visible = create_empty_visible(x_size,y_size)
    # print(visible)

    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))

