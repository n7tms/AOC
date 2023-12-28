# AOC 2023 day 17: Clumsy Crucible
#
# look at this thread: https://www.reddit.com/r/adventofcode/comments/18kr07r/2023_day_17_part_1_i_admit_defeat/
# and these:
#           https://www.redblobgames.com/pathfinding/a-star/introduction.html
#           https://www.reddit.com/user/MoreBaconPls/
#           https://www.reddit.com/user/Falcon731/
# I'm not sure how helpful those last three will be; I haven't looked at them yet.
#

import aoc_utils as aoc
import time
import os
import numpy as np

DAY = 17
# IN_FILE = os.path.join("AOC2023","inputs","2023"+str(DAY)+".in")
IN_FILE = os.path.join("AOC2023","inputs","2023"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2023,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().split("\n")

    data = [[int(c) for c in row] for row in data]
    return data

def min_cost(data,src: tuple, dst: tuple) -> int:

    # the order of these directions ensures the crucible will not reverse on itself.
    DIRS = [[-1,0],[0,1],[1,0],[0,-1]]

    # cur_dir is the index of DIRS that we are currently moving
    cur_dir = 1
    moves = 0

    R = len(data)
    C = len(data[0])

    m,n = dst   # target, destination
    r,c = 0,0   # origin, starting location

    tc = [[0 for x in range(C)] for x in range(R)]

    # calc the index of the DIRS to check -- straight (ds), left (dl), right (dr)
    ds = cur_dir
    dl = (cur_dir - 1) % 4
    dr = (cur_dir + 1) % 4
    
    # if moves=3, check value of left and right; otherwise check, straight, left, and right.
    # Figure out the least cost of the 2 (or 3) directions
    # if the cur_dir is the same as the least cost direction, inc moves
    # if the cur_dir is different from the least cost direction, moves = 1

    while [r,c] != [m,n]:
        rs,cs = [sum(i) for i in zip([r,c],DIRS[ds])]
        rl,cl = [sum(i) for i in zip([r,c],DIRS[dl])]
        rr,cr = [sum(i) for i in zip([r,c],DIRS[dr])]

        # get the cost (cx) of the data in each of those directions
        cost_s = 99 if not (0<=rs<R) or not (0<=cs<C) else data[rs][cs]
        cost_r = 99 if not (0<=rr<R) or not (0<=cr<C) else data[rr][cr]
        cost_l = 99 if not (0<=rl<R) or not (0<=cl<C) else data[rl][cl]
    
        if cost_s <= cost_r and cost_s <= cost_l and moves < 3:
            # continue straight
            moves += 1
            cur_dir = ds
            tc[r][c] = cost_s
            r,c = rs,cs
        elif cost_r <= cost_s and cost_r <= cost_l:
            # turn right
            moves = 0
            cur_dir = dr
            tc[r][c] = cost_r
            r,c = rr,cr
        else:
            # turn left
            moves = 0
            cur_dir = dl
            tc[r][c] = cost_l
            r,c = rl,cl

            
    
    
    
    
    # tc[0][0] = data[0][0]

	# # Initialize first column of total cost(tc) array
    # for i in range(1, m + 1):
    #     tc[i][0] = tc[i-1][0] + data[i][0]

	# # Initialize first row of tc array
    # for j in range(1, n + 1):
    #     tc[0][j] = tc[0][j-1] + data[0][j]


    # direction = -1  # current direction we just moved
    # dir_times = 0   # number of times we've moved in that direction
	# # Construct rest of the tc array
    # for i in range(1, m + 1):
    #     for j in range(1, n + 1):
    #         # tc[i][j] = min(tc[i-1][j-1], tc[i-1][j],tc[i][j-1]) + data[i][j]
    #         up = 99 if not (0<=i<R) else tc[i-1][j]
    #         dn = 99 if not (0<=i<R) else tc[i+1][j]
    #         lt = 99 if not (0<=j<C) else tc[i][j-1]
    #         rt = 99 if not (0<=j<C) else tc[i][j+1]
    #         tc[i][j] = min(tc[i-1][j],tc[i][j-1]) + data[i][j]

            


    return tc[m][n]




def part1(data):        # => 
    """
    Solve part 1
    
    """
    cost = [[1, 2, 3],
            [4, 8, 2],
            [1, 5, 3]]
    print(min_cost(data, (0,0), (len(data)-1,len(data[0])-1)))


    return


def part2(data):            # => 
    """
    Solve part 2
    """


    return

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(data))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(data))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        