# AOC 2023 day 10: Pipe Maze
#

import aoc_utils as aoc
import time
import os
import numpy as np


IN_FILE = os.path.join("AOC2023","inputs","202310.in")
# IN_FILE = os.path.join("AOC2023","inputs","202310.sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2023,10,False)

    with open(IN_FILE) as fp:
        data = fp.read().split("\n")
    
    return data

DIRS = [(-1,0),(1,0),(0,1),(0,-1)]


def part1(tiles):        # => 
    """
    Solve part 1
    
    """
    height = len(tiles)
    width = len(tiles[0])

    # find start (S)
    start = (0,0)
    c = 0
    for r, row in enumerate(tiles):
        try:
            if row.index("S"):
                c = row.index("S")
                
        except ValueError:
            continue
        if c:
            start = (r,c)
            break
    
    # find the next pipe off of S
    # n,s,e,w = 0,1,2,3
    # I could add code to determine where the next pipe next to S is, but
    # I visually (manually) found it going north (facing=0)
    facing = 0
    next_tile = np.add(np.array(start),np.array(DIRS[facing]))
    next_pipe = tiles[next_tile[0]][next_tile[1]]
    steps = 0

    while next_pipe != "S":
        steps += 1
        match facing:           # TODO change this into a dictionary
            case 0: # n
                if next_pipe == "F":
                    facing = 2
                if next_pipe == "|":
                    facing = 0
                if next_pipe == "7":
                    facing = 3
            case 1: # s
                if next_pipe == "|":
                    facing = 1
                if next_pipe == "J":
                    facing = 3
                if next_pipe == "L":
                    facing = 2
            case 2: # e
                if next_pipe == "7":
                    facing = 1
                if next_pipe == "-":
                    facing = 2
                if next_pipe == "J":
                    facing = 0
            case 3: # w
                if next_pipe == "F":
                    facing = 1
                if next_pipe == "-":
                    facing = 3
                if next_pipe == "L":
                    facing = 0

        next_tile = np.add(np.array(next_tile),np.array(DIRS[facing]))
        next_pipe = tiles[next_tile[0]][next_tile[1]]

    furthest_point = (steps // 2) + 1
    return furthest_point



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
        