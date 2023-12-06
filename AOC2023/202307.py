# AOC 2023 day 7: 
#

import aoc_utils as aoc
import time

# IN_FILE = "AOC2023\\inputs\\202307.in"
# IN_FILE = "AOC2023\\inputs\\202307.sample.txt"

IN_FILE = "AOC2023/inputs/202307.in"
# IN_FILE = "AOC2023/inputs/202307.sample.txt"

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2023,7,False)

    with open(IN_FILE) as fp:
        out = []
        # data = fp.read().splitlines()
        data = fp.read().split("\n")

        # times = [x for x in data[0].split(":")[1].split(" ") if x]
        # distances = [x for x in data[1].split(":")[1].split(" ") if x]


    return data


def part1(data):        # => 
    """
    Solve part 1
    
    """
    
    return 

def part2():            # => 
    """
    Solve part 2
    """

    return 


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
        