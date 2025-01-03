# AOC 2018 day 02: 
#

import aoc_utils as aoc
import time
import os
from collections import Counter

DAY = '02'
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



def part1(data):        # => 8715

    # twos = 0
    # threes = 0
    # for line in data:
    #     freq = Counter(line)
    #     f = set()
    #     for _,v in freq.items():
    #         f.add(v)
    #     if 2 in f:
    #         twos += 1
    #     if 3 in f:
    #         threes += 1
    
    twos = sum(2 in Counter(line).values() for line in data)
    threes = sum(3 in Counter(line).values() for line in data)
    return twos * threes
        

def compare_strings(x,y):
    # differences = 0
    # z = list(zip(x,y))
    # output = ''
    # for a,b in z:
    #     if a != b: 
    #         differences += 1
    #     else:
    #         output = output + a

    # if differences == 1: 
    #     return output
    # else:
    #     return False

    # differences = sum(1 for a,b in zip(x,y) if a != b)
    if 1 == sum(1 for a,b in zip(x,y) if a != b):
        return ''.join(a for a, b in zip(x,y) if a == b)

def part2(data):       # => fvstwblgqkhpuixdrnevmaycd

    for idx, x in enumerate(data):
        for y in data[idx+1:]:
            # Walrus operator ( := ) -- assigns the value of the function to diff and then tests diff in the if statement
            if diff := compare_strings(x,y):
                return diff
    return 0


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

