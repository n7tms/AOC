# AOC 2018 day 18: 
#


import aoc_utils as aoc
import time
import os
import copy


DAY = '18'
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".in")
IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".sample.txt")


aoc.get_input(2018,DAY,False)
with open(IN_FILE) as fp:
    data = fp.read().strip().splitlines()

forest = [[ch for ch in line] for line in data]
maxr = len(forest)
maxc = len(forest[0])

DIRS = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

# Solution for Part 1 here vvvvvvvvvvvvvvvvvvvvvvvvv     # => 
start_time = time.time()
for _ in range(10):
    tmp_forest = [['.'] * maxc] * maxr
    for r, line in enumerate(forest):
        for c,ch in enumerate(line):
            # an open acre "." surrounded by 3+ trees becomes a tree "|"; othewise nothing
            if ch == '.':
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

resources = sum(row.count('#') for row in tmp_forest) * sum(row.count('|') for row in tmp_forest)


exec_time = time.time() - start_time
print(f'Part 1: {resources} ({exec_time:.3f} sec)')



# Solution for Part 2 here vvvvvvvvvvvvvvvvvvvvvvvvv    # => 
start_time = time.time()


exec_time = time.time() - start_time
# print(f'Part 2: {tokens} ({exec_time:.3f} sec)')
