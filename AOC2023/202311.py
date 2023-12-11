# AOC 2023 day 11: Cosmic Expansion
#

import aoc_utils as aoc
import time
import os
import numpy as np


IN_FILE = os.path.join("AOC2023","inputs","202311.in")
# IN_FILE = os.path.join("AOC2023","inputs","202311.sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2023,11,False)

    with open(IN_FILE) as fp:
        data = fp.read().split("\n")
    
    return data



def part1(tiles):        # => 
    """
    Solve part 1
    
    """
    return


def part2(data):            # => 
    """
    Solve part 2
    """

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
        