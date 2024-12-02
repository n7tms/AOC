# AOC 2024 day 02: 
#

import aoc_utils as aoc
import time
import os
# import numpy as np

DAY = '02'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().split("\n")

    reports = [[int(x) for x in line.split(" ")] for line in data]
    return reports


def is_safe(report):
    if all(report[i] < report[i+1] and (report[i+1] - report[i] <= 3) for i in range(len(report)-1)) or \
    all(report[i] > report[i+1] and (report[i] - report[i+1] <= 3) for i in range(len(report)-1)):
        return True
    else:
        return False


def part1(reports):        # => 326
    """
    Solve part 1
    
    """
    # safe = 0
    # for report in reports:
    #     if is_safe(report):
    #         safe += 1
    safe = sum(1 for report in reports if is_safe(report))
    return safe
        

def made_safe(rpt):
    for idx in range(len(rpt)):
        r = rpt.copy()
        popped = r.pop(idx)
        if is_safe(r):
            return True
    return False


def part2(reports):       # => 381
    """
    Solve part 2
    """
    # safe = 0
    # for report in reports:
    #     if is_safe(report) or made_safe(report):
    #         safe += 1
    safe = sum(1 for report in reports if is_safe(report) or made_safe(report))

    return safe


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
        