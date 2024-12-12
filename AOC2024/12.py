# AOC 2024 day 12: 
#

import aoc_utils as aoc
import time
import os
from collections import defaultdict
import copy

DAY = '12'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")


def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()
    
    # field = {}
    # for r,line in enumerate(data):
    #     for c,ch in enumerate(line):
    #         field[(r,c)] = {'val':ch,'perimeter':0}

    # field = [ch for ch in line for line in data]
    field = []
    for line in data:
        tf = []
        for ch in line:
            tf.append(ch)
        field.append(tf)
            

    return field

DIRS = [(-1,0), (0,1), (1,0), (0,-1)]


def part1(field):       # => 1477762
    tmp_field = copy.deepcopy(field)
    total_price = 0

    # flood fill
    for r, line in enumerate(field):
        for c, ch in enumerate(line):
            if tmp_field[r][c] != '.':
                _, area = aoc.flood_fill(tmp_field,(r,c),ch,'.',[])
                perimeter = 0
                for r1,c1 in area:
                    for rd,cd in DIRS:
                        if 0 <= r1+rd < len(line) and 0 <= c1+cd < len(field):
                            if field[r1+rd][c1+cd] != ch: 
                                perimeter += 1
                        else:
                            perimeter += 1
                total_price += len(area) * perimeter                    
    return total_price

def part2(data):        # => 
    
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
        