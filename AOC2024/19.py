# AOC 2024 day 19: 
#

import aoc_utils as aoc
import time
import os
from collections import Counter

DAY = '19'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().split('\n\n')
    
    towels = [t.strip() for t in data[0].split(',')]
    designs = [d for d in data[1].splitlines()]
    
    return towels, designs


# FYI: design_count will certainly come in handy in other AOC problems.
# I've added it to the AOC library.
def design_count(towels, design):
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: one way to generate an empty design

    for i in range(1, n + 1):
        for towel in towels:
            if i >= len(towel) and design[i - len(towel):i] == towel:
                dp[i] += dp[i - len(towel)]

    return dp[n]


def part1(towels, designs):        # => 350
    possible = sum([1 for design in designs if design_count(towels,design) > 0])
    return possible


def part2(towels, designs):       # => 769668867512623
    possible_count = sum([design_count(towels,design) for design in designs])
    return possible_count
    


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    t,d = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(t,d))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(t,d))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        