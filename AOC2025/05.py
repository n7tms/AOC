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



def part1(id_ranges: list, fruits: list):        # => 712

    fresh = []
    for fruit in fruits:
        for s,e in id_ranges:
            if fruit >= s and fruit <= e and fruit not in fresh:
                fresh.append(fruit)
    return len(fresh)



def part2(id_ranges: list):        # => 332998283036769

    # merge ranges
    id_ranges.sort(key=lambda x: x[0])

    # Merge overlapping or adjacent ranges
    merged = []
    for current_start, current_end in id_ranges:
        if not merged:
            merged.append([current_start, current_end])
        else:
            last_start, last_end = merged[-1]
            if current_start <= last_end + 1:  # Overlaps or touches
                merged[-1][1] = max(last_end, current_end)
            else:
                merged.append([current_start, current_end])

    # Calculate total count
    total = 0
    for s, e in merged:
        total += e - s + 1
    
    return total


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    r,f = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(r,f))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(r))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve(IN_FILE)
        