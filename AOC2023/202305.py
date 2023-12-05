# AOC 2023 day 5: 
#

import aoc_utils as aoc
import numpy as np
from collections import defaultdict

# IN_FILE = "AOC2023\\inputs\\202305.in"
IN_FILE = "AOC2023\\inputs\\202305.sample.in"

# IN_FILE = "AOC2023/inputs/202305.in"
# IN_FILE = "AOC2023/inputs/202305.sample.in"

def parse(puzzle_input):
    """
    Parse

    """
    with open(IN_FILE) as fp:
        out = []
        # data = fp.read().splitlines()
        data = fp.read().split("\n\n")

        seeds = []
        categories = defaultdict() # "category": [(dst, src, lng),(dst, src, lng),...]

        for idx,line in enumerate(data):
            cat,maps = line.split(":")

            if cat == "seeds":
                seeds = maps.strip().split(" ")
            else:
                cat_name,_ = cat.split(" ")
                name_from,_,name_to = cat_name.strip().split("-")
                locations = maps.strip().split("\n")
                for loc in locations:
                    dst,src,lng = loc.strip().split(" ")
                    
                    if (name_from,name_to) in categories:
                        categories[(name_from,name_to)].append((int(dst),int(src),int(lng)))
                    else:
                        categories[(name_from,name_to)] = [(int(dst),int(src),int(lng))]



    return seeds,categories


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
        