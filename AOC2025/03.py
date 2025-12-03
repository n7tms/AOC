# AOC 2025 day 03: 
#

import aoc_utils as aoc
import time
import os
import re

DAY = '03'
# IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+"-sample.txt")
IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+".in")

def parse(puzzle_input):
    """
    Parse
    """

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()

    digits = [[int(c) for c in line] for line in data]
    return digits


def part1(x):        # => 17535
    """
    Solve part 1
    """
    total_joltage = 0

    for bank in x:
        dig1 = max(bank[:-1])
        idx = bank.index(dig1)
        dig2 = max(bank[idx+1:])

        total_joltage += int(str(dig1) + str(dig2))


    return total_joltage


def part2(x):        # => 173577199527257
    """
    Solve part 2
    """
    total_joltage = 0

    for bank in x:
        on_batts = []
        idx = -1
        for i in range(1,13):
            if i<12:
                digit = max(bank[idx+1:i-12])
                idx = idx + 1 + bank[idx+1:i-12].index(digit)
            else:
                digit = max(bank[idx+1:])
                idx = idx + 1 + bank[idx+1:].index(digit)
                
            on_batts.append(str(digit))
        total_joltage += int("".join(on_batts))

    return total_joltage


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
        