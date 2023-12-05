# AOC 2023 day 5: 
#

import aoc_utils as aoc
import numpy as np
from collections import defaultdict

# IN_FILE = "AOC2023\\inputs\\202305.in"
# IN_FILE = "AOC2023\\inputs\\202305.sample.txt"

IN_FILE = "AOC2023/inputs/202305.in"
# IN_FILE = "AOC2023/inputs/202305.sample.txt"

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
                seeds = [int(i) for i in maps.strip().split(" ")]
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



    return (seeds,categories)

def get_ranges(data,src):
    _,categories = data
    for x in categories:
        if src == x[0]:
            return (x[1],categories[x])

def part1(data):            # => 
    """
    Solve part 1
    
    """
    seeds,_ = data

    min_location = -1

    for seed in seeds:
        tmp_seed = seed
        source = "seed"
        # destination = ""

        while source != "location":
            new_seed = tmp_seed
            destination,ranges = get_ranges(data,source)

            for r in ranges:
                d,s,l = r
                if tmp_seed in range(s,s+l):
                    new_seed = d + (tmp_seed-s)
                    break

            tmp_seed = new_seed
            source,destination = destination,""

        if min_location == -1 or min_location > new_seed:
            min_location = new_seed



    return min_location

def part2(data):            # => 
    """
    Solve part 2
    """
    seeds,_ = data

    min_location = -1

    seed_pairs = list(zip(*[iter(seeds)]*2)    )

    for i,j in seed_pairs:
        for seed in range(i,i+j):
            tmp_seed = seed
            source = "seed"
            # destination = ""

            while source != "location":
                new_seed = tmp_seed
                destination,ranges = get_ranges(data,source)

                for r in ranges:
                    d,s,l = r
                    if tmp_seed in range(s,s+l):
                        new_seed = d + (tmp_seed-s)
                        break

                tmp_seed = new_seed
                source,destination = destination,""

            if min_location == -1 or min_location > new_seed:
                min_location = new_seed



    return min_location


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)

    print(f"part 1: {str(part1(data))}")
    print(f"part 2: {str(part2(data))}")


if __name__ == "__main__":
    solve(IN_FILE)
        