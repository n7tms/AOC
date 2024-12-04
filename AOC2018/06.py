# AOC 2018 day 06: 
#

import aoc_utils as aoc
import time
import os


DAY = '06'
IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2018,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()
    
    coordinates = []
    max_r, max_c = 0, 0
    for line in data:
        y,x = line.split(',')
        coordinates.append((int(x),int(y)))
        max_c = int(x) if int(x) > max_r else max_r
        max_r = int(y) if int(y) > max_c else max_c

    return coordinates, max_r, max_c



def part1(data, max_r, max_c):        # => 4171
    # fill a massive grid with a the distance to the first point (how massive?)
    # for the next point, iterate through the entire grid again, replacing points with this one, if its closer
    # same for each point
    # go through all the points and exclude the ones touch the permiter of the grid
    # count the rest to see which covers the most coords in the grid

    # initialize the grid
    grid = {}

    # iterate through the coordinates
    for rc in data:
        grid[rc] = [rc, 0, 1]
        
        # mark all the minimum distances
        for rd in range(max_r+1):
            for cd in range(max_c+1):
                man_dist = aoc.manhattan_distance(rc,(rd,cd))
                if (rd,cd) not in grid:
                    grid[(rd,cd)] = [rc, man_dist, 1]
                else:
                    if not (rc == (rd,cd)):
                        if grid[(rd,cd)][1] == man_dist:
                            grid[(rd,cd)] = [rc, man_dist, grid[(rd,cd)][2]+1]
                        elif grid[(rd,cd)][1] > man_dist:
                            grid[(rd,cd)] = [rc, man_dist, 1]


    grids_to_count = data.copy()
    # top edge
    for col in range(max_c+1):
        if grid[0,col][0] in grids_to_count and grid[0,col][2] < 2:
            grids_to_count.remove(grid[0,col][0])
    
    # bottom edge
    for col in range(max_c+1):
        if grid[max_r,col][0] in grids_to_count and grid[max_r,col][2] < 2:
            grids_to_count.remove(grid[max_r,col][0])
    
    # left edge
    for row in range(max_r+1):
        if grid[row,0][0] in grids_to_count and grid[row,0][2] < 2:
            grids_to_count.remove(grid[row,0][0])
    
    # right edge
    for row in range(max_r+1):
        if grid[row,max_c][0] in grids_to_count and grid[row,max_c][2] < 2:
            grids_to_count.remove(grid[row,max_c][0])
    
    marked_points = 0
    for g in grids_to_count:
        this_points = 0
        for _,v in grid.items():
            if v[0] == g and v[2] < 2:
                this_points += 1
        marked_points = this_points if marked_points < this_points else marked_points
   
    return marked_points

def part2(data, max_r, max_c):        # => 39545
    # the grid will contain the sum of the distance to every given coordinate
    # eliminate all the points with a distance >9999 (keep those < 10000)
    # What is the size of the region? (how many are <10000?)

    grid = {}
    for r in range(max_r+1):
        for c in range(max_c+1):
            this_sum = 0
            for d in data:
                this_sum += aoc.manhattan_distance((r,c), d)
            grid[(r,c)] = this_sum
    
    less_than = 0
    for _,v in grid.items():
        if v < 10000: less_than += 1

    return less_than

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data, mr, mc = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(data,mr,mc))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(data,mr,mc))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)

