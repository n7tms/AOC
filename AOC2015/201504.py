# AOC 2015 - Day 4

import time
import hashlib

# IN_FILE = "d:\\Dev\AOC2015\\201504.txt"
# IN_FILE = "d:\\Dev\AOC2015\\201504.sample.txt"
# IN_FILE = "abcdef"
IN_FILE = "bgvyzdsv"


def parse():
    """Parse input."""
    # pi = [line for line in puzzle_input.split("\n")]
    with open(IN_FILE) as f:
        out = [(line) for line in f.read().split('\n')]
    return out
        

def part1(data):            # => 254575
    """Solve part 1."""
    for i in range(1000000):
        tmp = data + str(i)
        hashed = hashlib.md5(tmp.encode())
        # print(str(hashed.hexdigest())[:5])
        if str(hashed.hexdigest())[:5] == "00000":
            return i
    return "Not found!"


def part2(data):            # => 1038736
    """Solve part 2."""
    for i in range(10000000):
        tmp = data + str(i)
        hashed = hashlib.md5(tmp.encode())
        # print(str(hashed.hexdigest())[:5])
        if str(hashed.hexdigest())[:6] == "000000":
            return i
    return "Not found!"


if __name__ == "__main__":
    timestart = time.time()
    
    puzzle_input = IN_FILE
    # print(puzzle_input)
    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))
