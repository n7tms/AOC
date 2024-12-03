# AOC 2024 day 03: 
#

import aoc_utils as aoc
import time
import os
# import numpy as np
import re

DAY = '03'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip()

    return data



def part1(results):        # => 174336360
    """
    Solve part 1
    
    """
    result = re.findall(r"mul\(\d+,\d+\)", results)
    sums = []
    for x in result:
        nums = re.findall(r"\d+,\d+",x)
        n,m = nums[0].split(",")
        sums.append(int(n) * int(m))

    return sum(sums)
        


def part2(results):       # => 88802350
    """
    Solve part 2
    """
    result = re.findall(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)", results)
    sums = []
    enabled = True
    for x in result:
        if enabled and x[0] == 'm':
            nums = re.findall(r"\d+,\d+",x)
            n,m = nums[0].split(",")
            sums.append(int(n) * int(m))
        elif x == "do()":
            enabled = True
        elif x == "don't()":
            enabled = False

    return sum(sums)


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
        