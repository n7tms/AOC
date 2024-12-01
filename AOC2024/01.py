# AOC 2024 day 01: 
#

import aoc_utils as aoc
import time
import os
# import numpy as np

DAY = '01'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2023","inputs","2023"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    # aoc.get_input(2023,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().split("\n")

    left = []
    right = []
    for line in data:
        l,r = line.split('   ')
        left.append(int(l))
        right.append(int(r))
    
    return left,right




def part1(l,r):        # => 1646452
    """
    Solve part 1
    
    """
    # total = []
    l.sort()
    r.sort()
    # for idx in range(len(l)):
    #     total.append(abs(l[idx] - r[idx]))
    # # return sum(total)

    return sum([abs(l[idx] - r[idx]) for idx in range(len(l))])
        


def part2(l,r):            # => 23609874
    """
    Solve part 2
    """
    # total = []
    # for num in l:
    #     total.append(num * r.count(num))
    # total = [num*r.count(num) for num in l]

    return sum([num*r.count(num) for num in l])

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    l,r = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(l,r))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(l,r))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        