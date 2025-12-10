# AOC 2025 day 09: 
#

import time
import os
from itertools import combinations

DAY = '09'
# IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+"-sample.txt")
IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+".in")

def parse(puzzle_input):
    """
    Parse
    """
    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()

    red_tiles = []
    for line in data:
        x,y = line.split(",")
        red_tiles.append([int(y), int(x)])

    return red_tiles



def part1old(x):        # => 
    ul = []
    lr = []
    ur = []
    ll = []

    for a,b in x:
        if not ul:
            ul = [a,b]
            lr = [a,b]
            ur = [a,b]
            ll = [a,b]
            continue

        if a <= ul[0] and b <= ul[1]:
            ul = [a,b]
        
        if a >= lr[0] and b >= lr[1]:
            lr = [a,b]
      
        if a <= ur[0] and b >= ur[1]:
            ur = [a,b]

        if a >= ll[0] and b <= ll[1]:
            ll = [a,b]


    # ul and lr
    area1 = (abs(ul[0] - lr[0]) + 1) * (abs(ul[1] - lr[1]) + 1)

    # ur and ll
    area2 = (abs(ur[0] - ll[0]) + 1) * (abs(ur[1] - ll[1]) + 1)

    return max(area1, area2)


def part1(x):   # => 4773451098
    pairs = [list(pair) for pair in combinations(x,2)]

    max_area = 0
    for p in pairs:
        x0, y0, x1, y1 = p[0][0], p[0][1], p[1][0], p[1][1]
        new_area = (abs(x0 - x1) + 1) * (abs(y0 - y1) + 1)
        max_area = max(max_area, new_area)

    return max_area

def part2(x):        # => 

    return 0


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    x = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(x))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(x))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve(IN_FILE)
        