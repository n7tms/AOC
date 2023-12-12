# AOC 2023 day 11: Cosmic Expansion
#

import aoc_utils as aoc
import time
import os
import numpy as np
from itertools import combinations


IN_FILE = os.path.join("AOC2023","inputs","202311.in")
# IN_FILE = os.path.join("AOC2023","inputs","202311.sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2023,11,False)

    with open(IN_FILE) as fp:
        data = fp.read().split("\n")
    
    return data


# def part1(data):        # => 9312968

def adjust_coord(coord, er, ec, mult):
    r,c = coord
    e_rows = sum(i<r for i in er)
    e_cols = sum(j<c for j in ec)

    r += (e_rows * mult) - e_rows
    c += (e_cols * mult) - e_cols
    return (r,c)


def part12(data, mult):            # => 597714117556
    """
    Solve parts 1 & 2
    """

    # create a list of all of the rows without any galaxies
    empty_rows = []
    for i,row in enumerate(data):
        if '#' not in row:
            empty_rows.append(i)

    # rotate the data and create a list of all of the "columns" without galaxies
    tmp = []
    for r in data:
        new_row = []
        for c in r:
            new_row.append(c)
        tmp.append(new_row)
    tmp2 = list(np.rot90(tmp,k=-1))

    empty_cols = []
    for j,col in enumerate(tmp2):
        if '#' not in col:
            empty_cols.append(j)
    
    # get the coordinates for each galaxy; compensate for empty rows/cols
    new_coords = []
    for r,row in enumerate(data):
        for c,col in enumerate(row):
            if col == "#":
                new_coords.append(adjust_coord((r,c), empty_rows, empty_cols, mult))
    
    # create a collection of each pair of galaxies
    unique_pairs = list(combinations(new_coords,2))

    # measure the (manhattan) distance between each galaxy
    # and keep track of the total.
    total_distance = []
    for pair in unique_pairs:
        distance = aoc.manhattan_distance(pair[0], pair[1])
        total_distance.append(distance)

    return sum(total_distance)



def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part12(data,2))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part12(data,1000000))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        