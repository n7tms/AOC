# AOC 2018 day 07: 
#

import aoc_utils as aoc
import time
import os
import re


DAY = '07'
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".in")
IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2018,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()
    
    instructions = []
    for line in data:
        instr = list(re.match(r"Step (.+) must be finished before step (.+) can begin.", line).groups())
        instructions.append(instr)
        
    return instructions


def fix(rules, pages):
    sorted = False
    while not sorted:
        sorted = True
        for f,s in rules:
            if f in pages and s in pages:
                idx_f = pages.index(f)
                idx_s = pages.index(s)
                if idx_f > idx_s:
                    pages[idx_f], pages[idx_s] = pages[idx_s], pages[idx_f]
                    sorted = False

    return pages


def part1(data):        # => 
    correct_order = []

    for f,s in data:
        if s not in correct_order:
            correct_order.append(s)
        if f not in correct_order:
            correct_order.insert(0,f)
    
    fixed = fix(data,correct_order)



    return ''.join(fixed)


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

