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
# IN_FILE = 18



def part1(data):        # => 243,72
    grid = [[0 for _ in range(301)] for _ in range(301)]

    for x in range(1,len(grid[0])):
        for y in range(1,len(grid)):
            rackid = x + 10
            power_level = rackid * y
            power_level += data
            power_level *= rackid

            if power_level < 100:
                power_level = 0
            else: 
                power_level = (power_level // 100) % 10
            
            power_level -= 5

            grid[x][y] = power_level
    
    max_pl = {}
    for x in range(1,len(grid[0])-2):
        for y in range(1,len(grid)-2):
            # tmp_pl = grid[x][y] + grid[x][y+1] + grid[x][y+2] + grid[x+1][y] + grid[x+1][y+1] + grid[x+1][y+2] + grid[x+2][y] + grid[x+2][y+1] + grid[x+2][y+2] 
            s = 3
            tmp_pl = 0
            for a in range(s):
                for b in range(s):
                    tmp_pl += grid[x+a][y+b]

            max_pl[(x,y)] = tmp_pl
        
    return max(max_pl, key=max_pl.get)
        


# def part2(data):        # => 
#     grid = [[0 for _ in range(301)] for _ in range(301)]

#     for x in range(1,len(grid[0])):
#         for y in range(1,len(grid)):
#             rackid = x + 10
#             power_level = rackid * y
#             power_level += data
#             power_level *= rackid

#             if power_level < 100:
#                 power_level = 0
#             else: 
#                 power_level = (power_level // 100) % 10
            
#             power_level -= 5

#             grid[x][y] = power_level
    
#     max_pl_size = {}
#     for s in range(150):
#         max_pl = {}
#         for x in range(1,len(grid[0])-s):
#             for y in range(1,len(grid)-s):
#                 tmp_pl = 0
#                 for a in range(s):
#                     for b in range(s):
#                         tmp_pl += grid[x+a][y+b]
#                 max_pl[(x,y)] = tmp_pl
#         max_pl_size[(max(max_pl, key=max_pl.get),s)] = tmp_pl
        
#     return max(max_pl_size, key=max_pl_size.get)


# I plugged my code above into AI and asked it to optomize my code. It produced this:
# I need to learn more about how cummulative sums and integral images work.
def part2(data):        # => (229, 192, 11)
    # Initialize the grid
    grid = [[0] * 301 for _ in range(301)]

    # Populate the power levels in the grid
    for x in range(1, 301):
        for y in range(1, 301):
            rack_id = x + 10
            power_level = ((rack_id * y + data) * rack_id // 100) % 10 - 5
            grid[x][y] = power_level

    # Create a cumulative sum (integral image) grid for fast area sum calculations
    cum_sum = [[0] * 301 for _ in range(301)]
    for x in range(1, 301):
        for y in range(1, 301):
            cum_sum[x][y] = (
                grid[x][y]
                + cum_sum[x - 1][y]
                + cum_sum[x][y - 1]
                - cum_sum[x - 1][y - 1]
            )

    def get_area_sum(x1, y1, x2, y2):
        """Calculate the sum of a rectangle using the integral image."""
        return (
            cum_sum[x2][y2]
            - cum_sum[x1 - 1][y2]
            - cum_sum[x2][y1 - 1]
            + cum_sum[x1 - 1][y1 - 1]
        )

    # Find the top-left corner and size of the square with the maximum power level
    max_power = float('-inf')
    best_coords = None

    for s in range(1, 151):  # Iterate over square sizes
        for x in range(1, 302 - s):
            for y in range(1, 302 - s):
                power = get_area_sum(x, y, x + s - 1, y + s - 1)
                if power > max_power:
                    max_power = power
                    best_coords = (x, y, s)

    return best_coords




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

