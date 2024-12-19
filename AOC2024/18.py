# AOC 2024 day 18: 
#

import aoc_utils as aoc
import time
import os

DAY = '18'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()
    
    falling_bytes = [list(map(int,line.split(','))) for line in data]
    return falling_bytes



def part1(falling_bytes):        # => 438
    """
    Solve part 1
    
    """
    width = 71
    height = 71

    # build the blank memory
    memory = []
    for r in range(height):
        for c in range(width):
            memory.append((r,c))
    
    # remove corrupted memory
    for c,r in falling_bytes[:1024]:
        memory.remove((r,c))

    # find the shortest path to the end
    result = aoc.bfs_shortest_path(memory,(0,0),(70,70))
    return len(result) - 1



def part2(falling_bytes):       # => 26,22
    """
    Solve part 2
    """
    width = 71
    height = 71

    # build the blank memory
    memory = []
    for r in range(height):
        for c in range(width):
            memory.append((r,c))
    
    # remove corrupted memory
    for c,r in falling_bytes[:1024]:
        memory.remove((r,c))

    # we already know there is a valid path through block 1024.
    # continue dropping blocks and checking the path until there is no solution.
    for c,r in falling_bytes[1024:]:
        memory.remove((r,c))
        if not aoc.bfs_shortest_path(memory,(0,0),(70,70)):
            return (c,r)
    
    return 'path never blocked'



def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    fb = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(fb))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(fb))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        