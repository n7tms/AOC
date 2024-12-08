# AOC 2018 day 11: 
#

import aoc_utils as aoc
import time
import os
import re


DAY = '11'
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".sample.txt")

IN_FILE = 9424



def part1(data):        # => 
    grid = [[0 for _ in range(301)] for _ in range(301)]

    for r in range(1,len(grid[0])):
        for c in range(1,len(grid)):
            rackid = c + 10
            power_level = rackid * r
            power_level += data
            power_level *= rackid

            if power_level < 100:
                power_level = 0
            else: 
                power_level = (power_level // 100) % 10
            
            power_level -= 5

            grid[r][c] = power_level
    
        max_pl = {}
        for r in range(1,len(grid[0])-2):
            for c in range(1,len(grid)-2):
                tmp_pl = grid[r][c] + grid[r][c+1] + grid[r][c+2] + grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] + grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] 
                max_pl[(r,c)] = tmp_pl
        
        

    
    return
        


def part2(data):        # => 
    return


def solve():
    """Solve the puzzle for the given input."""
    # data = parse()
    data = IN_FILE

    start_time = time.time()
    p1 = str(part1(data))
    # p1 = str(part1(13, 7999))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(data))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve()

