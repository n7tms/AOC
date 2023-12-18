# AOC 2023 day 18: Lavaduct Lagoon
#

import aoc_utils as aoc
import time
import os
import numpy as np
import re

DAY = 18
IN_FILE = os.path.join("AOC2023","inputs","2023"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2023","inputs","2023"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2023,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().split("\n")
    
    # Create array of vertices (and colors)
    # R 6 (#70c710) => [(0,0),(0,6),"#70c710"]
    vertices = []
    x1,y1 = 0,0
    for line in data:
        results = re.match(r"([LURD]) (\d+) \((#[0-9a-f]{6})\)", line)
        dir,mag,color = results.groups()

        x2,y2 = x1,y1        
        match dir:
            case 'R':
                y2 = y1 + int(mag)
            case 'D':
                x2 = x1 + int(mag)
            case 'L':
                y2 = y1 - int(mag)
            case 'U':
                x2 = x1 - int(mag)
        vertices.append([(x1,y1),(x2,y2),color])
        x1,y1 = x2,y2

    return vertices



def part1(data):        # => 62573
    """
    Solve part 1
    
    """
    area = aoc.shoelace_formula(data,True)
    return int(area)


def part2(data):        # => 54662804037719
    """
    Solve part 2
    """
    vertices = []
    x1,y1 = 0,0

    # recreate the vertices based on the coding in the color
    for line in data:
        color = line[2]
        mag = int(color[1:6],16)
        dir = color[-1]

        x2,y2 = x1,y1        
        match dir:
            case '0': # R
                y2 = y1 + int(mag)
            case '1': # D
                x2 = x1 + int(mag)
            case '2': # 
                y2 = y1 - int(mag)
            case '3':
                x2 = x1 - int(mag)
        vertices.append([(x1,y1),(x2,y2),color])
        x1,y1 = x2,y2

    area = aoc.shoelace_formula(vertices,True)
    return int(area)


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
        