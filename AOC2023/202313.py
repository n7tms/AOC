# AOC 2023 day 13: Point of Incidence
#

import aoc_utils as aoc
import time
import os
import numpy as np

IN_FILE = os.path.join("AOC2023","inputs","202313.in")
# IN_FILE = os.path.join("AOC2023","inputs","202313.sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2023,13,False)

    with open(IN_FILE) as fp:
        data = fp.read().split("\n\n")
    
    return data


def is_mirror(data, rp: int) -> bool:
    """ rp is the reflection point ... the line below the line of reflection """
    refl_size = 0
    if rp > len(data) / 2:
        # there are fewer rows below the line
        refl_size = len(data) - rp
    else: 
        refl_size = rp

    # flip the other side for comparison
    otherside = list(np.flipud(data[rp:rp+refl_size]))
    if data[rp-refl_size:rp] == otherside:
        return True
    
    return False

def search_for_reflection(field,mult=1):
    previous_row = []
    for i,row in enumerate(field):
        if row == previous_row:
            if is_mirror(field,i):
                found = True
                return i * mult
        previous_row = row
    return 0



def part1(data):        # => 30705
    """
    Solve part 1
    
    """
    # Iterate through data
    # split on \n
    # iterate through rows looking for one that matches the previous
    # if found, mulitply 100 by rows above and store in summarize
    # if not found, rotate 90 degrees
    # iterate through the "columns" looking for one that matches the previous
    # if found, add the number of "columns" to summarize

    summarize = 0
    for mirrors in data:
        field = mirrors.split("\n")

        score = search_for_reflection(field,100)

        if score == 0: # no horizontal reflection found
            field = aoc.rotate90(field)
            score = search_for_reflection(field,1)
        
        summarize += score

    return summarize

def part2(data):            # => 
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
        