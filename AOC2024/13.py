# AOC 2024 day 13: 
#

##########################################################################
# I'm going to try this day a little different -- just straight top-down.
# Just hack out a direct solution and not pretty with functions etc.
##########################################################################

import aoc_utils as aoc
import time
import os
from collections import defaultdict
import sympy as sp
import re

DAY = '13'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")


aoc.get_input(2024,DAY,False)
with open(IN_FILE) as fp:
    data = fp.read().strip().split('\n\n')

r = r'X[+=](-?\d+), Y[+=](-?\d+)'
games = [[[int(x),int(y)] for x,y in re.findall(r,groups)] for groups in data]


start_time = time.time()
# Solution for Part 1 here vvvvvvvvvvvvvvvvvvvvvvvvv     # => 29438

tokens = 0
for game in games:
    a = sp.Matrix([[game[0][0],game[1][0]],[game[0][1],game[1][1]]])
    b = sp.Matrix([game[2][0],game[2][1]])
    x = a.solve(b)
    if int(x[0]) == x[0] and int(x[1]) == x[1]:
        tokens += (x[0] * 3) + x[1]


exec_time = time.time() - start_time
print(f'Part 1: {tokens} ({exec_time:.3f} sec)')



start_time = time.time()
# Solution for Part 2 here vvvvvvvvvvvvvvvvvvvvvvvvv    # => 104958599303720
tokens = 0
offset = 10000000000000
for game in games:
    a = sp.Matrix([[game[0][0],game[1][0]],[game[0][1],game[1][1]]])
    b = sp.Matrix([game[2][0]+offset,game[2][1]+offset])
    x = a.solve(b)
    if int(x[0]) == x[0] and int(x[1]) == x[1]:
        tokens += (x[0] * 3) + x[1]


exec_time = time.time() - start_time
print(f'Part 2: {tokens} ({exec_time:.3f} sec)')





