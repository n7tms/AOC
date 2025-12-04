# AOC 2025 day 04: 
#

import aoc_utils as aoc
import time
import os
import re

DAY = '04'
# IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+"-sample.txt")
IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+".in")

def parse(puzzle_input):
    """
    Parse
    """
    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()

    map = [[c for c in line] for line in data]
    return map


def neighbors(r, c, grid):
    rows, cols = len(grid), len(grid[0])
    for dr, dc in [(-1,0), (0,1), (1,0), (0,-1), (-1,-1), (-1,1), (1,-1), (1,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc



def part1(x):        # => 1372
    """
    Solve part 1
    """
    total_papers = 0
    for r, line in enumerate(x):
        for c, ch in enumerate(line):
            if ch == "@":
                papers = 0
                for nr, nc in neighbors(r, c, x):
                    if x[nr][nc] == "@":
                        papers += 1
                if papers < 4:
                    total_papers += 1

    return total_papers


def find_removables(x: list) -> list:

    removable = []
    for r, line in enumerate(x):
        for c, ch in enumerate(line):
            if ch == "@":
                papers = 0
                for nr, nc in neighbors(r, c, x):
                    if x[nr][nc] == "@":
                        papers += 1
                if papers < 4:
                    removable.append([r,c])
    return removable


def part2(x):        # => 7922
    """
    Solve part 2
    """
    removed_papers = 0
    new_map = x[:]

    removable = True
    while removable:
        rs = find_removables(new_map)
        removed_papers += len(rs)
        for loc in rs:
            new_map[loc[0]][loc[1]] = "."
        
        if part1(new_map) == 0:
            removable = False

    return removed_papers


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    x = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(x))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(x))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve(IN_FILE)
        