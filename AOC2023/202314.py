# AOC 2023 day 14: Parabolic Reflector Dish
#

import aoc_utils as aoc
import time
import os
import numpy as np
from collections import defaultdict
from copy import deepcopy

DAY = 14
# IN_FILE = os.path.join("AOC2023","inputs","2023"+str(DAY)+".in")
IN_FILE = os.path.join("AOC2023","inputs","2023"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2023,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().split("\n")
    
    data = [[c for c in row] for row in data]
    return data



def part1(data):        # => 113424 (18 mins!)
    """
    Solve part 1
    
    """
    # move all the rocks north
    moved = True
    while moved:
        moved = False
        for col in range(len(data)):
            for row in range(1,len(data[0])):
                if data[row][col] == 'O' and data[row-1][col] not in ['O','#']:
                    data[row][col] = '.'
                    data[row-1][col] = 'O'
                    moved = True
    
    # sum the positions
    total_load = 0
    for r, row in enumerate(data):
        stones = row.count('O')
        total_load += (len(data)-r) * stones

    return total_load


def spin(data):
    # north
    moved = True
    while moved:
        moved = False
        for col in range(len(data)):
            for row in range(1,len(data[0])):
                if data[row][col] == 'O' and data[row-1][col] not in ['O','#']:
                    data[row][col] = '.'
                    data[row-1][col] = 'O'
                    moved = True

    # west
    moved = True
    while moved:
        moved = False
        for row in range(len(data)):
            for col in range(1,len(data[0])):
                if data[row][col] == 'O' and data[row][col-1] not in ['O','#']:
                    data[row][col] = '.'
                    data[row][col-1] = 'O'
                    moved = True

    # south
    moved = True
    while moved:
        moved = False
        for col in range(len(data)):
            for row in range(len(data[0])-1):
                if data[row][col] == 'O' and data[row+1][col] not in ['O','#']:
                    data[row][col] = '.'
                    data[row+1][col] = 'O'
                    moved = True

    # east
    moved = True
    while moved:
        moved = False
        for row in range(len(data)):
            for col in range(len(data[0])-1):
                if data[row][col] == 'O' and data[row][col+1] not in ['O','#']:
                    data[row][col] = '.'
                    data[row][col+1] = 'O'
                    moved = True

    return data

def calc_load(data) -> int:
    total_load = 0
    for r, row in enumerate(data):
        stones = row.count('O')
        total_load += (len(data)-r) * stones
    return total_load

def part2(data):            # => <104345
    """
    Solve part 2
    """
    history = defaultdict(list)
    # spin everything, store the outcome in history
    # when we get to a duplicate, use mod to calc the state after 1000000000 cycles
    # calc the total_load of that instance
    cycles = 0
    this_load = 0
    while not (data in history.values()):
        prev_load = this_load
        history[cycles] = deepcopy(data)

        data = spin(data)
        # this_load = calc_load(data)
        # if this_load == prev_load:
        #     print(f'{cycles}')

        cycles += 1

    # get index of first occurence of data in history
    index = 0
    for k,v in history.items():
        if v == data:
            index = k
            break
    
    # target_cycle = (1000000000 % (cycles - index)) - 1
    target_cycle = 1000000000 % len(history)

    # sum the positions
    total_load = calc_load(history[target_cycle])

    return total_load

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    part2_data = deepcopy(data)

    start_time = time.time()
    p1 = str(part1(data))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(part2_data))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        