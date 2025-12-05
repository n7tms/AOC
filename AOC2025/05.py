# AOC 2025 day 05: 
#

import aoc_utils as aoc
import time
import os
import re

DAY = '05'
# IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+"-sample.txt")
IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+".in")

def parse(puzzle_input):
    """
    Parse
    """
    with open(IN_FILE) as fp:
        data = fp.read().strip().split("\n\n")

    id_ranges = []
    for i in data[0].splitlines():
        a,b = i.split("-")
        id_ranges.append([int(a),int(b)])
    
    fruit = [int(x) for x in data[1].splitlines()]
    return id_ranges, fruit



def part1(id_ranges: list, fruits: list):        # => 

    fresh = []
    for fruit in fruits:
        for s,e in id_ranges:
            if fruit >= s and fruit <= e and fruit not in fresh:
                fresh.append(fruit)
    return len(fresh)



def part2(id_ranges: list, fruits: list):        # => 
    # s1 and e1 both fall inside some other s0 and e0
    # s1 is outside some other s0 and e1, but e0 is inside 
    # s1 is inside some other s0 and e1, but e0 is outside


    total_fresh = 0
    for s,e in id_ranges:
        total_fresh += (e-s+1)
    return 0


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    r,f = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(r,f))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(r,f))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve(IN_FILE)
        