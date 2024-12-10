# AOC 2024 day 10: 
#

import aoc_utils as aoc
import time
import os

DAY = '10'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")


def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()
    
    map = []
    starts = []

    for r,line in enumerate(data):
        map_line = []
        for c,ch in enumerate(line):
            map_line.append(int(ch))
            if ch == '0':
                starts.append((r,c))
        map.append(map_line)


    return map, starts

DIRS = [(-1,0), (0,1), (1,0), (0,-1)]


def explore(map, start, allow_duplicates=True):
    score = 0
    branches = [start]
    visited = set()

    while branches:
        r0,c0 = branches.pop(0)
        value = map[r0][c0]
        if value == 9:
            score += 1
        else:
            for dr, dc in DIRS:
                r,c = dr+r0, dc+c0
                if 0<=r<len(map) and 0<=c<len(map[0]) and map[r][c] == value+1:
                    if not allow_duplicates or (r,c) not in visited: 
                            branches.append((r,c))
                            visited.add((r,c))
    return score



def part1(map, starts):        # => 574
    trails = 0
    for trailhead in starts:
        trails += explore(map, trailhead, True)

    return trails

def part2(map, starts):        # => 1238
    trails = 0
    for trailhead in starts:
        trails += explore(map, trailhead, False)

    return trails


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    m,s = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(m,s))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(m,s))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        