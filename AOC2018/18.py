# AOC 2018 day 18: 
#


import aoc_utils as aoc
import time
import os
import copy
from collections import Counter


DAY = '18'
IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".sample.txt")


aoc.get_input(2018,DAY,False)
with open(IN_FILE) as fp:
    data = fp.read().strip()

forest = [[ch for ch in line] for line in data.splitlines()]
forest2 = [[ch for ch in line] for line in data.splitlines()]
maxr = len(forest)
maxc = len(forest[0])

DIRS = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

# Solution for Part 1 here vvvvvvvvvvvvvvvvvvvvvvvvv     # => 514944
start_time = time.time()
for _ in range(10):
    tmp_forest = aoc.empty_matrix(maxr,maxc,'.')
    for r, line in enumerate(forest):
        for c,ch in enumerate(line):
            # an open acre "." surrounded by 3+ trees becomes a tree "|"; othewise nothing
            if ch == '.':
                    dirs = [1 for r1,c1 in DIRS if 0 <= r+r1 < maxr and 0 <= c+c1 < maxc and forest[r+r1][c+c1] == '|']
                    if sum([1 for r1,c1 in DIRS if 0 <= r+r1 < maxr and 0 <= c+c1 < maxc and forest[r+r1][c+c1] == '|']) > 2:
                        tmp_forest[r][c] = '|'
                    else:
                        tmp_forest[r][c] = ch

            # "|" tree becomes a lumberyard "#" if adjacent to 1+ lumberyard and 1+ tree; otherwise nothing
            elif ch == '|':
                if sum([1 for r1,c1 in DIRS if 0 <= r+r1 < maxr and 0 <= c+c1 < maxc and forest[r+r1][c+c1] == '#']) > 2:
                    tmp_forest[r][c] = '#'
                else:
                    tmp_forest[r][c] = ch

            # a lumberyard "#" remains a "#" if adjacent to 1+ "#" and 1+ "|"; otherwise turns to open "."
            elif ch == '#':
                if sum([1 for r1,c1 in DIRS if 0 <= r+r1 < maxr and 0 <= c+c1 < maxc and forest[r+r1][c+c1] == '#']) > 0 and sum([1 for r1,c1 in DIRS if 0 <= r+r1 < maxr and 0 <= c+c1 < maxc and forest[r+r1][c+c1] == '|']) > 0:
                    tmp_forest[r][c] = '#'
                else:
                    tmp_forest[r][c] = '.'
            else:
                tmp_forest[r][c] = ch
    forest = copy.deepcopy(tmp_forest)

resources = sum(row.count('#') for row in tmp_forest) * sum(row.count('|') for row in tmp_forest)
exec_time = time.time() - start_time
print(f'Part 1: {resources} ({exec_time:.3f} sec)')



# Solution for Part 2 here vvvvvvvvvvvvvvvvvvvvvvvvv    # => 193050
# A little bit different for 1000000000 iterations......
start_time = time.time()

def get_adjacent(x, y, grid):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    adjacent = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            adjacent.append(grid[nx][ny])
    return adjacent

def next_state(grid):
    new_grid = [row[:] for row in grid]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            adjacent = get_adjacent(x, y, grid)
            if grid[x][y] == ".":
                new_grid[x][y] = "|" if adjacent.count("|") >= 3 else "."
            elif grid[x][y] == "|":
                new_grid[x][y] = "#" if adjacent.count("#") >= 3 else "|"
            elif grid[x][y] == "#":
                new_grid[x][y] = "#" if "#" in adjacent and "|" in adjacent else "."
    return new_grid

def grid_to_string(grid):
    return "\n".join("".join(row) for row in grid)

def resource_value(grid):
    flat = [cell for row in grid for cell in row]
    counts = Counter(flat)
    return counts["|"] * counts["#"]

def simulate_until(input_str, target_minutes):
    grid = input_str
    seen_states = {}
    cycle_detected = False

    for minute in range(target_minutes):
        grid_str = grid_to_string(grid)

        if grid_str in seen_states and not cycle_detected:
            start_of_cycle = seen_states[grid_str]
            cycle_length = minute - start_of_cycle
            remaining_minutes = (target_minutes - minute) % cycle_length

            for _ in range(remaining_minutes):
                grid = next_state(grid)
            return resource_value(grid)

        seen_states[grid_str] = minute
        grid = next_state(grid)

    return resource_value(grid)

resources = simulate_until(forest2, 1000000000)

exec_time = time.time() - start_time
print(f'Part 2: {resources} ({exec_time:.3f} sec)')

