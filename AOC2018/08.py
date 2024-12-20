# AOC 2018 day 08: 
#

import aoc_utils as aoc
import time
import os


DAY = '08'
IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2018,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()


    
    return list(map(int, data[0].split(' ')))


def find_nodes(data):
    meta_sum = 0
    child_nodes = data.pop(0)
    metadata_entries = data.pop(0)
    for _ in range(child_nodes):
        meta_sum = meta_sum + find_nodes(data)
    
    meta_sum = meta_sum + sum(data[:metadata_entries])
    for _ in range(metadata_entries): 
        data.pop(0)
    return meta_sum



def part1(data):        # => 42146

    meta_sum = find_nodes(data)
    return meta_sum


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

