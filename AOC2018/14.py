# AOC 2018 day 14: 
#

import aoc_utils as aoc
import time
import os
from collections import deque


DAY = '14'
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".sample.txt")

def parse():
    """
    Parse
    """
    aoc.get_input(2018,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()
    
    return 



def part1(data):        # => 
    recipes = [3,7]
    elf1 = 0
    elf2 = 1

    round = 0
    while round < data:
        new_recipe = recipes[elf1] + recipes[elf2]
        if new_recipe > 9:
            recipes.append(1)
            recipes.append(new_recipe-10)
        else:
            recipes.append(new_recipe)
        elf1 = (recipes[elf1] + 1) % len(recipes) + elf1
        elf2 = (recipes[elf2] + 1) % len(recipes) + elf2



    return 


def part2():        # => 
    return

def solve():
    """Solve the puzzle for the given input."""
    # data = parse()
    data = 765071

    start_time = time.time()
    p1 = str(part1(data))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(data))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve()

