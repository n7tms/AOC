# AOC 2025 day 08: 
#

##############################################################################################
# I COULD NOT WRAP MY HEAD AROUND WHAT THIS PROBLEM WAS EVEN ASKING ME TO DO. 
# EVEN AFTER READING many REDDIT POSTS, I STILL HAVE NO IDEA.
#
# The solution was found using 08b.py from "jasonwallestad" (https://github.com/jasonwallestad/aoc2025/blob/main/day08.py)
##############################################################################################


import time
import os
import math

DAY = '08'
IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+"-sample.txt")
# IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+".in")

def parse(puzzle_input):
    """
    Parse
    """
    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()

    boxes = []
    for line in data:
        x,y,z = line.split(",")
        boxes.append([int(x),int(y),int(z)])
    
    
    return boxes


def distance(a: list, b: list) -> int:
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

def part1(x):        # => 63920
    circuits = []

    x2 = x[:]
    for a in x:
        d = 999999999999
        pair = []
        for b in x2:
            if a==b: continue
            dst = distance(a,b)
            if dst < d:
                d = dst
                pair = [a,b]
        pair.sort()
        # see if either of the members of this pair are part of a circuit already
        found = False
        for c, circuit in enumerate(circuits):
            if pair[0] in circuit or pair[1] in circuit:
                circuits[c].append(a)
                circuits[c].append(b)
                found = True
                break
        if not found:
            circuits.append(pair)


    return 0


def part2(x):        # => 1026594680

    return 0


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    x = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(x))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(x))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve(IN_FILE)
        