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
    for line in data:
        x,y = line.split(',')
        coordinates.append((int(x),int(y)))

    return coordinates



def part1(data):        # => 
    # fill a massive grid with a the distance to the first point (how massive?)
    # for the next point, iterate through the entire grid again, replacing points with this one, if its closer
    # same for each point
    # go through all the points and exclude the ones touch the permiter of the grid
    # count the rest to see which covers the most coords in the grid
    return 

def part2(data):        # => 
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

