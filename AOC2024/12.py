# AOC 2024 day 12: 
#

import aoc_utils as aoc
import time
import os
from collections import defaultdict

DAY = '12'
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")


def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()
    
    field = {}
    for r,line in enumerate(data):
        for c,ch in enumerate(line):
            field[(r,c)] = {'val':ch,'perimeter':0}

    return field

DIRS = [(-1,0), (0,1), (1,0), (0,-1)]




def part1(field):        # => 

    # find the perimeter
    for (r,c),data in field.items():
        # for adjoining cells where value does not match, add perimeter
        for r1,c1 in DIRS:
            if (r+r1,c+c1) in field:
                if field[(r+r1,c+c1)]['val'] != data['val']: 
                    field[(r,c)]['perimeter'] += 1
            else:
                field[(r,c)]['perimeter'] += 1
        pass

    # The total number of cells in a group is the area
    # The sum of the perimeters is the total perimeter of that group
    results = defaultdict(lambda: {'area':0, 'perimeter':0})
    for cell, info in field.items():
        val = info['val']
        results[val]['area'] += 1
        results[val]['perimeter'] += info['perimeter']

    # calculate results
    total_price = 0
    for val, stats in results.items():
        print(f"Value: {val}, Area: {stats['area']}, Perimeter: {stats['perimeter']}")
        total_price += (stats['area'] * stats['perimeter'])


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
        