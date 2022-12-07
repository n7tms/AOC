# AOC 2022 - Day 7

import time

IN_FILE = "AOC2022\\202207.txt"
# IN_FILE = "AOC2022\\202207.sample.txt"

def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        out = [(line) for line in f.read().split('\n')]
    return out[0]
        

def part1(data):            # => 
    """Solve part 1."""


def part2(data):            # => 
    """Solve part 2."""
    

if __name__ == "__main__":
    timestart = time.time()
    
    puzzle_input = parse()
    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))
