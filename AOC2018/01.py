# AOC 2018 day 01: 
#

import aoc_utils as aoc
import time
import os

DAY = '01'
IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2018,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()

    return data



def part1(data):        # => 408
    """
    Solve part 1
    """
    freq = 0
    for d in data:
        change = int(d)
        freq += change
    

    return freq
        


def part2(data):       # => 55250
    """
    Solve part 2
    """
    freqs = []
    freq = 0
    while True:
        for d in data:
            change = int(d)
            freq += change
            if freq in freqs:
                return freq
            else:
                freqs.append(freq)


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
        