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


# Solution for Part 1 here vvvvvvvvvvvvvvvvvvvvvvvvv     # => 
start_time = time.time()
for _ in range(10):
    tmp_forest = []
    for r, line in enumerate(forest):
        for c,ch in enumerate(line):
            # an open acre "." surrounded by 3+ trees becomes a tree "|"; othewise nothing

            # "|" tree becomes a lumberyard "#" if adjacent to 1+ lumberyard and 1+ tree; otherwise nothing

            # a lumberyard "#" remains a "#" if adjacent to 1+ "#" and 1+ "|"; otherwise turns to open "."


exec_time = time.time() - start_time
print(f'Part 1: {tokens} ({exec_time:.3f} sec)')



# Solution for Part 2 here vvvvvvvvvvvvvvvvvvvvvvvvv    # => 
start_time = time.time()


exec_time = time.time() - start_time
print(f'Part 2: {tokens} ({exec_time:.3f} sec)')
