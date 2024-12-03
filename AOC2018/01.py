# AOC 2018 day 01: 
#

import aoc_utils as aoc
import time
import os
from itertools import cycle

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
    # freq = 0
    # for d in data:
    #     change = int(d)
    #     freq += change
    
    freq = sum([int(d) for d in data])

    return freq
        


def part2(data):       # => 55250
    # convert the list of data to integers
    data1 = list(map(int, data))

    # tracking the frequencies in a set rather than a list shaved 98 seconds off the run time!!!
    freqs = set()
    freq = 0
    
    # while True:
    #     for d in data1:
    #         freq += d
    #         if freq in freqs:
    #             return freq
    #         else:
    #             freqs.add(freq)

    # This is the most pythonic way to execute this code.
    for d in cycle(data1):
        freq += d
        if freq in freqs:
            return freq
        else:
            freqs.add(freq)

    # cycled_data = cycle(data1)
    # while True:
    #     freq += next(cycled_data)
    #     if freq in freqs:
    #         return freq
    #     else:
    #         freqs.add(freq)

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
        