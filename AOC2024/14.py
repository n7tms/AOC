# AOC 2024 day 14: 
#


import aoc_utils as aoc
import time
import os
import sympy as sp
import re


DAY = '14'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")


aoc.get_input(2024,DAY,False)
with open(IN_FILE) as fp:
    data = fp.read().strip().split('\n\n')


# Solution for Part 1 here vvvvvvvvvvvvvvvvvvvvvvvvv     # => 29438
start_time = time.time()


exec_time = time.time() - start_time
print(f'Part 1: {tokens} ({exec_time:.3f} sec)')



# Solution for Part 2 here vvvvvvvvvvvvvvvvvvvvvvvvv    # => 104958599303720
start_time = time.time()


exec_time = time.time() - start_time
print(f'Part 2: {tokens} ({exec_time:.3f} sec)')
