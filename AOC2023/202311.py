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


def rotate90Clockwise(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp
    return A

def part1(data):        # => 9312968
    """
    Solve part 1
    
    """
    # add a row for the empty rows
    # rotate the galaxy
    # add a row for the empty rows
    tmp = data.copy()
    number_of_inserts = 0
    for i,row in enumerate(data):
        if '#' not in row:
            tmp.insert(i+number_of_inserts,row)
            number_of_inserts += 1
    
    tmp3 = []
    for r in tmp:
        new_row = []
        for c in r:
            new_row.append(c)
        tmp3.append(new_row)

    tmp2 = list(np.rot90(tmp3,k=-1))

    galaxy = tmp2.copy()
    number_of_inserts = 0
    for i,row in enumerate(tmp2):
        if '#' not in row:
            galaxy.insert(i+number_of_inserts,row)
            number_of_inserts += 1

    # Map the Galaxy
    galaxies = []
    for i,row in enumerate(galaxy):
        this_row = [ind for ind, ele in enumerate(row) if ele == '#']
        for j in this_row:
            galaxies.append((i,j))
    

    unique_pairs = list(combinations(galaxies,2))

    total_distance = []
    for pair in unique_pairs:
        distance = aoc.manhattan_distance(pair[0], pair[1])
        total_distance.append(distance)

    return sum(total_distance)


def part2(data):            # => 
    """
    Solve part 2
    """

# https://imgur.com/a/p6QcTbY#7YLs0yw
# create a dictionary of all of the galaxyies coordinates (r,c)
# iterate through the data
# if there is a galaxy,
#   update the coordinates, (r*blank_rows*multiplier) (part 1 mult = 1; part 2 mult = 1M)
# if there is a blank row, 
#   increase the r in all subsquent galaxies
#
# rotate the data
# iterate through the data again
# if there is a galaxy,
#   update the coordinates, (c*blank_cols*multiplier)
# if there is a blank [column],
#   increase the c in all subsequent galaxies


    tmp = data.copy()
    blank_rows = 0
    for i,row in enumerate(data):
        if '#' not in row:
            for _ in range(1000000):
                tmp.insert(i+number_of_inserts,row)
            number_of_inserts += 1000000
    
    tmp3 = []
    for r in tmp:
        new_row = []
        for c in r:
            new_row.append(c)
        tmp3.append(new_row)

    tmp2 = list(np.rot90(tmp3,k=-1))

    galaxy = tmp2.copy()
    number_of_inserts = 0
    for i,row in enumerate(tmp2):
        if '#' not in row:
            for _ in range(1000000):
                galaxy.insert(i+number_of_inserts,row)
            number_of_inserts += 1000000

    # Map the Galaxy
    galaxies = []
    for i,row in enumerate(galaxy):
        this_row = [ind for ind, ele in enumerate(row) if ele == '#']
        for j in this_row:
            galaxies.append((i,j))
    

    unique_pairs = list(combinations(galaxies,2))

    total_distance = []
    for pair in unique_pairs:
        distance = aoc.manhattan_distance(pair[0], pair[1])
        total_distance.append(distance)

    return sum(total_distance)

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
        