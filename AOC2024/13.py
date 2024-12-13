# AOC 2024 day 13: 
#

##########################################################################
# I'm going to try this day a little different -- just straight top-down.
# Just hack out a direct solution and not pretty with functions etc.
##########################################################################

import aoc_utils as aoc
import time
import os
import sympy as sp
import re


# sympy was my first choice to solve this, and it looks like it was a good one.
# I experimented with different modules, including numpy, but numpy experiences rounding errors, 
# especially with large integers.
# mpmath is also a possibility, but the solutions look much more complex.
# numpy is faster on part1 (~0.01 sec) compared to sympy's ~0.4 sec, but is half a second going
# to make that much difference in the cosmic grand scheme of things!?!

DAY = '13'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")


aoc.get_input(2024,DAY,False)
with open(IN_FILE) as fp:
    data = fp.read().strip().split('\n\n')

r = r'X[+=](-?\d+), Y[+=](-?\d+)'
games = [[[int(x),int(y)] for x,y in re.findall(r,groups)] for groups in data]


# Solution for Part 1 here vvvvvvvvvvvvvvvvvvvvvvvvv     # => 29438
start_time = time.time()
tokens = 0
for game in games:
    a = sp.Matrix([[game[0][0],game[1][0]],[game[0][1],game[1][1]]])
    b = sp.Matrix([game[2][0],game[2][1]])
    x = a.solve(b)
    if int(x[0]) == x[0] and int(x[1]) == x[1]:
        tokens += (x[0] * 3) + x[1]

exec_time = time.time() - start_time
print(f'Part 1: {tokens} ({exec_time:.3f} sec)')



# Solution for Part 2 here vvvvvvvvvvvvvvvvvvvvvvvvv    # => 104958599303720
start_time = time.time()
tokens = 0
offset = 10000000000000
for game in games:
    a = sp.Matrix([[game[0][0], game[1][0]], [game[0][1], game[1][1]]])
    b = sp.Matrix([game[2][0]+offset, game[2][1]+offset])
    x = a.solve(b)
    if int(x[0]) == x[0] and int(x[1]) == x[1]:
        tokens += (x[0] * 3) + x[1]

exec_time = time.time() - start_time
print(f'Part 2: {tokens} ({exec_time:.3f} sec)')
