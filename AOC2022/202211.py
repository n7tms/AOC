# AOC 2022 - Day 11

import time

# IN_FILE = "AOC2022\\202211.txt"
IN_FILE = "AOC2022\\202211.sample.txt"


def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        # return [[int(c) for c in line.strip()] for line in f]     # integers
        # return [(line.strip()) for line in f.read().split('\n')]    # strings
        # return [([dir,mag] for dir,mag in line.split()) for line in f.read().split('\n')]
        out = [line for line in f.read().split('\n')]
    return [line.split() for line in out]


def part1(data):            # => 
    """Solve part 1."""


def part2(data):            # => 
    """Solve part 2."""


if __name__ == "__main__":
    timestart = time.time()
    tm = [[0] * 600] * 600  # initialize tail map

    puzzle_input = parse()
    # print(puzzle_input)

    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))

