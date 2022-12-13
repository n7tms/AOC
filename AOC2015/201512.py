# AOC 2015 - Day 12

import time
import re

IN_FILE = "AOC2015\\201512.txt"
# IN_FILE = "AOC2015\\201512.sample.txt"

def parse():
    with open(IN_FILE) as f:
        out = [line for line in f.read().split('\n')]

    return out

def parse2():
    with open(IN_FILE) as f:
        out = f.read()

    return out


def part1(data):            # => 119433
    """Solve part 1."""
    # all_numbers = map(int,re.findall("\\d+",data))
    # return sum(all_numbers)

    all_numbers = map(int,re.findall("-?\d+\.?\d*",data))
    return sum(all_numbers)

def part2(data):            # => 
    """Solve part 2."""
    x = {"a":["red","red",46,"red"]}
    print(x)

if __name__ == "__main__":
    timestart = time.time()

    data = parse2()

    print("part 1:",part1(data))
    print("part 2:",part2(data))
    
    timeend = time.time()
    print("Execution time: ", f"{timeend-timestart:0.4f}")

