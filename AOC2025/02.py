# AOC 2025 day 02: 
#

import aoc_utils as aoc
import time
import os
import re

DAY = '02'
IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+"-sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    # aoc.get_input(2025,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().split(",")

    return data


def part1(x):        # => 18893502033
    """
    Solve part 1
    """

    pattern = re.compile(r'^(\d+)\1$')
    total = 0

    for data in x:
        ds, de = data.split("-")
        ds, de = int(ds), int(de)

        for x in range(ds,de+1):
            m = pattern.match(str(x))
            if m:
                total = total + x


    return total
        

def part2(x):        # => 26202168557
    """
    Solve part 2
    """
    pattern = re.compile(r'^(\d+)\1+$')
    total = 0

    for data in x:
        ds, de = data.split("-")
        ds, de = int(ds), int(de)

        for x in range(ds,de+1):
            m = pattern.match(str(x))
            if m:
                total = total + x


    return total


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
        