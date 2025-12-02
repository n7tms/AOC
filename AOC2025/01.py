# AOC 2025 day 01: 
#

import aoc_utils as aoc
import time
import os

DAY = '01'
IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+"-sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    # aoc.get_input(2025,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().split("\n")

    # We don't need the R and L; just change the magnitude to a negative if the direction is L
    directions = [int(d[1:]) * (-1 if d[0] == "L" else 1) for d in data]
    return directions


def part1(x):        # => 1168
    """
    Solve part 1
    
    """
    index = 50
    zeros = 0

    for mag in x:
        index = (index + mag) % 100

        if index == 0:
            zeros += 1

    return zeros
        

def part2(x):        # => 7199
    """
    Solve part 2
    """

    # I tried a couple of things and kept coming up short. I decided to brute-force this thing.
    # This literally rotates the dial tick by tick by incrementing (or decrementing) the index.
    # If at any time the index is 0 (index % 100), then increment the zero counter.
    dial = 50
    zeros = 0

    for mag in x:
        for _ in range(abs(mag)):
            if mag < 0:
                dial += -1
            else:
                dial += 1
            dial = dial % 100 # this keeps the index between 0 and 99, inclusive.
            if dial == 0:
                zeros += 1

    return zeros


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
        