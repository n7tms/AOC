# AOC 2024 day 16: 
#

import aoc_utils as aoc
import time
import os

DAY = '16'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()
    
    start = None 
    exit = None
    map = []
    for r,line in enumerate(data):
        for c, ch in enumerate((line)):
            if ch == 'S':
                start = (r,c)
                map.append((r,c))
            elif ch == 'E':
                exit = (r,c)
                map.append((r,c))
            elif ch == '.':
                # rather than form a little map, I'm just going to store the valid path locations
                map.append((r,c))
    # print(map)
    return map, start, exit

DIRS = [(-1,0),(0,1),(1,0),(0,-1)]


def part1(map, start, exit):        # => 92405 < x < 93405
    # path = aoc.dfs_shortest_path(map,start,exit)
    path = aoc.bfs_shortest_path(map,start,exit)
    print(path)

    # find all the turns
    turns = aoc.count_direction_changes(path)
    
    total_cost = (turns * 1000) + len(path)
    return total_cost

    # paths = aoc.bfs_all_paths(map,start, exit)
    # scores = []
    # for path in paths:
    #     scores.append(len(path) + (1000*aoc.count_direction_changes(path)))
    
    # return min(scores)





def part2(m,s,e):       # => 
    return

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    m,s,e = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(m,s,e))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(m,s,e))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        