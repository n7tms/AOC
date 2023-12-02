# AOC 2023 day 3: 
#

import numpy as np

IN_FILE = "AOC2023\\inputs\\202303.in"
# IN_FILE = "AOC2023\\inputs\\202303.sample.in"

# IN_FILE = "./inputs/202303.in"
# IN_FILE = "./inputs/202303.sample.in"


def parse(puzzle_input):
    """
    Part Parse
    """
    with open(IN_FILE) as fp:
        out = []
        data = fp.read().splitlines()
    return data
           

def part1(data):            # => 
    """
    Solve part 1
    
    """
    
    return 


def part2(data):            # => 
    """
    Solve part 2
    
    """
    

    return


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)

    print(f"part 1: {str(part1(data))}")
    print(f"part 2: {str(part2(data))}")


if __name__ == "__main__":
    solve(IN_FILE)
        