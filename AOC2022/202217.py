# AOC 2022 - Day 17

import time

IN_FILE = "AOC2022\\inputs\\202217.txt"
# IN_FILE = "AOC2022\\inputs\\202216.sample.txt"
# IN_FILE = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"


def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        out = f.read()
    return out
    


def part1(data):            # => 
    """Solve part 1."""


def part2(data):            # => 
    """Solve part 2."""

if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    print(data)

    print("part 1:",part1(data))
    print("part 2:",part2(data))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))