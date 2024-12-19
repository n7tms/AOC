# AOC 2024 day 18: 
#

import aoc_utils as aoc
import time
import os
import re

DAY = '18'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sampleb.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()
    
    falling_bytes = [[int(x),int(y)] for x,y in [for line in data.split(',')]]


    return falling_bytes



def part1(pgm, regs):        # => 4,1,5,3,1,5,3,5,7
    """
    Solve part 1
    
    """
    
    return 



def part2(pgm, regs):       # => 
    """
    Solve part 2
    """
    return


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    p,r = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(p,r))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(p,r))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        