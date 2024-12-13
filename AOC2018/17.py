# AOC 2018 day 17: 
#

##########################################################################
# I'm going to try this day a little different -- just straight top-down.
# Just hack out a direct solution and not pretty with functions etc.
##########################################################################

import aoc_utils as aoc
import time
import os
from collections import defaultdict
import re

DAY = '17'
YEAR = '2018'
# IN_FILE = os.path.join("AOC"+YEAR,"inputs",YEAR+"-"+str(DAY)+".in")
IN_FILE = os.path.join("AOC"+YEAR,"inputs",YEAR+"-"+str(DAY)+".sample.txt")


aoc.get_input(2018,DAY,False)
with open(IN_FILE) as fp:
    data = fp.read().strip().splitlines()

clay = set()
maxr, maxc = 0, 0
for line in data:
    xy, a, b, c = re.match(r'([xy])=(\d+), [xy]=(\d+)\.\.(\d+)', line).groups()
    a,b,c = int(a), int(b), int(c)
    if xy == 'x':
        for z in range(b,c+1):
            clay.add((z,a))
        maxr = max(maxr, c)
        maxc = max(maxc, a)
    else:
        for z in range(b,c+1):
            clay.add((a,z))
        maxr = max(maxr, a)
        maxc = max(maxc, c)



DIRS = [(-1,0), (0,1), (1,0), (0,-1)]

start_time = time.time()

##########################################################################
# Solution for Part 1 here vvvvvvvvvvvvvvvvvvvvvvvvv
##########################################################################
# 
waters = set()
water = (0,500)
running_water = list()

# if water can go down (no clay below), go down.
# if water can't go down go left and right.
#   continue to flow left and right until 
running_water.append(water)
while True:
    moved = False
    r,c = running_water[-1] # get the water at the end of the list (LIFO)

    # Check for end conditions
    # if r == 0: # we are back to the source; no solution
    #     part1 = 'no solution'
    #     break
    if r > maxr: # we are dropping off the bottom of the map (done!)
        part1 = len(waters)
        break


    if (r+1,c) not in clay and (r+1,c) not in waters: # go down if no clay and no water
        if r > maxr: break # did we run off the bottom of the map? if yes, then done.
        running_water.append((r+1,c)) 
        waters.add((r+1,c))
        moved = True
    else: # can't do down. Can we go left or right?
        if (r,c-1) not in clay and (r,c-1) not in waters:
            running_water.append((r,c-1))
            waters.add((r,c-1))
            running_water.remove((r,c))
            moved = True
        if (r,c+1) not in clay and (r,c+1) not in waters:
            running_water.append((r,c+1))
            waters.add((r,c+1))
            if (r,c) in running_water: running_water.remove((r,c))
            moved = True
    if not moved:
        running_water.pop()




print(f'Part 1: {part1}')



# Solution for Part 2 here vvvvvvvvvvvvvvvvvvvvvvvvv


part2 = 0
print(f'Part 2: {part2}')




exec_time = time.time() - start_time

