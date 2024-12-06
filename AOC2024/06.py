# AOC 2024 day 06: 
#

import aoc_utils as aoc
import time
import os

DAY = '06'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")

directions = [(-1,0),(0,1),(1,0),(0,-1)]

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip()
    data = data.splitlines()
    map = [list(d) for d in data]
    return map


def part1(map):        # => 5208
    # find the start
    start = ()
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == "^":
                start = (r,c)
                break
    

    positions = set()
    dir = 0
    here = '.'
    posr, posc = start
    # pos = start
    # while posr >= 0 and posr < len(map) and posc >= 0 and posc < len(map[0]):
    while True:
        positions.add((posr,posc))
        posr, posc = posr + directions[dir][0], posc + directions[dir][1]
        if posr < 0 or posr >= len(map) or posc < 0 or posc >= len(map[0]):
            return len(positions)
        elif map[posr][posc] == "#":
            posr, posc = posr - directions[dir][0], posc - directions[dir][1]
            dir = (dir + 1) % len(directions)

        # posr, posc = posr + directions[dir][0], posc + directions[dir][1]



def part2(map):       # => 
    return

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(data))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(data))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        