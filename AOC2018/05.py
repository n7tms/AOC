# AOC 2018 day 05: 
#

import aoc_utils as aoc
import time
import os
# import string


DAY = '05'
IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2018,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()
            
    return data[0]


def opposites(p1,p2):
    return abs(ord(p1) - ord(p2)) == 32


def reduce_polymer(p):
    idx = 0
    while idx < len(p)-1:
        if not opposites(p[idx], p[idx+1]):
            idx += 1
        else:
            p = p[:idx] + p[idx+2:]
            if idx > 0:
                idx -= 1

    return len(p)     


def part1(polymer):        # => 9296
    return reduce_polymer(polymer)

def part2(data):           # => 5534
    uLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lLetters = 'abcdefghijklmnopqrstuvwxyz'
    
    reaction_size = len(data)

    # Create a set of (uppercase, lowercase) pairs
    letter_pairs = zip(uLetters,lLetters)

    # Iterate through each letter pair and compute the minimum reaction size
    reaction_size = min(reduce_polymer(data.translate(str.maketrans('', '', uc + lc))) for uc, lc in letter_pairs)
    return reaction_size

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

