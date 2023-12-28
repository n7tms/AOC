# AOC 2023 day xx: 
#

import aoc_utils as aoc
import time
import os
import numpy as np

DAY = 21
IN_FILE = os.path.join("AOC2023","inputs","2023"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2023","inputs","2023"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2023,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().split("\n")
    
    return data




def part1(data):        # => 
    """
    Solve part 1
    
    """

    import itertools as it
    c = it.cycle([[0,1],[1,0],[0,-1],[-1,0]])
    for i,x in enumerate(c):
        if i<6:
            print(x)
        else:
            break

    return


def part2(data):            # => 
    """
    Solve part 2
    """

    input = "11 45 4"
    a,b = [int(x) for x in input.split()]
    print(a+b)

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
        