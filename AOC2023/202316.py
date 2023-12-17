# AOC 2023 day 16: The Floor Will Be Lava 
#

import aoc_utils as aoc
import time
import os
import numpy as np

DAY = 16
IN_FILE = os.path.join("AOC2023","inputs","2023"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2023","inputs","2023"+str(DAY)+".sample.txt")
DIRS = [[0,1],[1,0],[0,-1],[-1,0]]

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2023,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().split("\n")

    data = [[c for c in row] for row in data]
    return data




def trace_beam(position, direction,data,beam_path,beams):
    r,c = position

    while True:
        # out of bounds?
        if not (0<=r<len(data)) or not (0<=c<len(data[0])):
            break

        here = data[r][c]

        # record the beam
        beam_path[r][c] = 1

        if [r,c,direction] in beams:
            break
        else: 
            beams.append([r,c,direction])

        # 0=right, 1=down, 2=left, 3=up
            
        # what do we have here...?
        if here == ".":
            r += DIRS[direction][0]
            c += DIRS[direction][1]
        elif here == "|":
            if direction == 1 or direction == 3:
                r += DIRS[direction][0]
                c += DIRS[direction][1]
            else:
                r1 = r + DIRS[1][0]
                c1 = c + DIRS[1][1]
                r2 = r + DIRS[3][0]
                c2 = c + DIRS[3][1]
                beam_path, beams = trace_beam([r1,c1],1,data,beam_path,beams)
                beam_path, beams = trace_beam([r2,c2],3,data,beam_path,beams)              

        elif here == "-":
            if direction == 0 or direction == 2:
                r += DIRS[direction][0]
                c += DIRS[direction][1]
            else:
                r1 = r + DIRS[0][0]
                c1 = c + DIRS[0][1]
                r2 = r + DIRS[2][0]
                c2 = c + DIRS[2][1]
                beam_path, beams = trace_beam([r1,c1],0,data,beam_path,beams)
                beam_path, beams = trace_beam([r2,c2],2,data,beam_path,beams)              

        elif here == "\\":
            if direction == 0 or direction == 2:
                direction = (direction + 1) % 4
                r += DIRS[direction][0]
                c += DIRS[direction][1]
            else:
                direction = (direction - 1) % 4
                r += DIRS[direction][0]
                c += DIRS[direction][1]
                        
        elif here == "/":
            if direction == 0 or direction == 2:
                direction = (direction - 1) % 4
                r += DIRS[direction][0]
                c += DIRS[direction][1]
            else:
                direction = (direction + 1) % 4
                r += DIRS[direction][0]
                c += DIRS[direction][1]

    return beam_path, beams


def part1(data):        # => 7199
    """
    Solve part 1
    
    """
    # create an array the same size as data to store the coords touched by the beam
    # Trace the beam, storing {(coords): [beam_directions]} in array
    # how to deal with splitters .... ??   recursion??
    # if recursion, what is the exit trigger?
    # count the number of unique keys
    beam_path = aoc.empty_matrix(len(data[0]), len(data))
    beams = []

    # 0=right, 1=down, 2=left, 3=up
    direction = 0
    pos = [0,0]

    beam_path, beams = trace_beam(pos,direction,data,beam_path,beams)

    energized = sum(sum(x) for x in beam_path)
    return energized


def part2(data):            # => 7438
    """
    Solve part 2
    """
    energized = []
    # from the top
    for c in range(len(data[0])):
        beam_path = aoc.empty_matrix(len(data[0]), len(data))
        beams = []
        beam_path,beams= trace_beam([0,c],1,data,beam_path,beams)
        energized.append(sum(sum(x) for x in beam_path))

    # from the bottom
    for c in range(len(data[0])-1,-1,-1):
        beam_path = aoc.empty_matrix(len(data[0]), len(data))
        beams = []
        beam_path,beams = trace_beam([len(data)-1,c],3,data,beam_path,beams)
        energized.append(sum(sum(x) for x in beam_path))

    # from the left
    for r in range(len(data)):
        beam_path = aoc.empty_matrix(len(data[0]), len(data))
        beams = []
        beam_path,beams = trace_beam([r,0],0,data,beam_path,beams)
        energized.append(sum(sum(x) for x in beam_path))

    # from the right
    for r in range(len(data)-1,-1,-1):
        beam_path = aoc.empty_matrix(len(data[0]), len(data))
        beams = []
        beam_path,beams = trace_beam([r,len(data[0])-1],2,data,beam_path,beams)
        energized.append(sum(sum(x) for x in beam_path))

    return max(energized)

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
        