# AOC 2023 day 15: Lens Library
#

import aoc_utils as aoc
import time
import os
import numpy as np
from collections import defaultdict
import re

DAY = 15
IN_FILE = os.path.join("AOC2023","inputs","2023"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2023","inputs","2023"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2023,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().split("\n")
    
    return data

def calc_hash(data) -> int:
    cv = 0
    for ch in data:
        cv += ord(ch)
        cv *= 17
        cv = cv % 256
    return cv


def part1(data):        # => 516657
    """
    Solve part 1
    
    """
    # data = ["rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"]
    return sum([calc_hash(c) for c in data[0].split(',')])


def part2(data):        # => 210906
    """
    Solve part 2
    """
    # create a dictionary of 256 lens boxes (a dictionary of lists)
    # {boxno: [(label,focal), (label,focal), ...]
    boxes = defaultdict()
    for i in range(256):
        boxes[i] = []
   

    # data = ["rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"]
    cmds = data[0].split(',')

    for cmd in cmds:
        # use re to parse p
        #    [label] [op] [focal]
        # get hash of label
        # if op == '-', remove it from the box (hash) if it's there
        # if op == '=', 
        #   check if a lens with that label already exists in the box (hash)
        #   if so, remove it (and/or) put this (label, focal) in its place.
        #   if not, append (label, focal) to this box (hash)

        c = [x for x in re.split('^(\w+)([-|=])([0-9]*)', cmd) if x != '']
        c_hash = calc_hash(c[0])

        if len(c) == 2 and c[1] == '-':
            # remove label if it exists
            new_t = []
            for lens in boxes[c_hash]:
                if lens[0] != c[0]:
                    new_t.append(lens)
            boxes[c_hash] = new_t
        elif len(c) == 3 and c[1] == '=':
            # replace if exists; append if it doesn't
            lens = (c[0],int(c[2]))
            found = False
            new_lenses = []
            for k,v in boxes[c_hash]:
                if k == lens[0]:
                    new_lenses.append(lens)
                    found = True
                else:
                    new_lenses.append((k,v))
            if not found:
                new_lenses.append(lens)

            boxes[c_hash] = new_lenses


    # iterate through the boxes; calculate the total focusing power; return the sum
    total_focusing_power = 0
    for k,lenses in boxes.items():
        for m,l in enumerate(lenses,1):
            total_focusing_power += (k+1) * m * l[1]
            
    return total_focusing_power

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
        