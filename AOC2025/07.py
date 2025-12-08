# AOC 2025 day 07: 
#

import aoc_utils as aoc
import time
import os

DAY = '07'
# IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+"-sample.txt")
IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+".in")

def parse(puzzle_input):
    """
    Parse
    """
    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()
    
    splitters = []
    for r, line in enumerate(data):
        for c, ch in enumerate(line):
            if ch == "S": start = [r,c]
            elif ch == "^":
                splitters.append([r,c])

    return start, splitters, [len(data), len(data[0])]


def part1(start: list, splitters: list, size: list):        # => 1642
    rows, cols = size

    beams = [0] * cols
    beams[start[1]] = 1

    splits = 0
    for row in range(1,rows):
        for sr, sc in splitters:
            if sr == row:
                if beams[sc] == 1:
                    beams[sc-1], beams[sc], beams[sc+1] = 1,0,1
                    splits += 1

    return splits


def part2(start: list, splitters: list, size: list):        # => 47274292756692
    rows, cols = size

    beams = [0] * cols
    beams[start[1]] = 1

    for row in range(1,rows):
        for sr, sc in splitters:
            if sr == row:
                if beams[sc] > 0:
                    beams[sc-1] += beams[sc]
                    beams[sc+1] += beams[sc]
                    beams[sc] = 0

    return sum(beams)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    st,sp,si = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(st, sp, si))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(st,sp,si))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve(IN_FILE)
        