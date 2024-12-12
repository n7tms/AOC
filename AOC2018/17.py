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

DAY = '17'
YEAR = '2018'
# IN_FILE = os.path.join("AOC"+YEAR,"inputs",YEAR+"-"+str(DAY)+".in")
IN_FILE = os.path.join("AOC"+YEAR,"inputs",YEAR+"-"+str(DAY)+".sample.txt")


aoc.get_input(2018,DAY,False)
with open(IN_FILE) as fp:
    data = fp.read().strip().splitlines()


DIRS = [(-1,0), (0,1), (1,0), (0,-1)]

start_time = time.time()
# Solution for Part 1 here vvvvvvvvvvvvvvvvvvvvvvvvv


part1 = 0
print(f'Part 1: {part1}')



# Solution for Part 2 here vvvvvvvvvvvvvvvvvvvvvvvvv


part2 = 0
print(f'Part 2: {part2}')




exec_time = time.time() - start_time

