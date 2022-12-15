# AOC 2022 - Day 15

import time
import re

# IN_FILE = "AOC2022\\inputs\\202215.txt"
IN_FILE = "AOC2022\\inputs\\202215.sample.txt"

# initialize the cave with all 1 
# all locations in range of sensor get flipped to 0

def man_dist(point1, point2):
    x1,y1 = point1
    x2,y2 = point2
    return abs(x1-x2) + abs(y1-y2)

def in_range(point1, distance, cave):
    x1,y1 = point1
    miny = y1 - distance
    maxy = y1 + distance
    minx = x1 - distance
    maxx = x1 + distance



def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        out = [line for line in f.read().split('\n')]
    
    # [[[2,18],[-2,15]],[[9,16],[10,16]], ... ]
    # min[x,y]   max[x,y]

    sensors = {}
    ul = (0,0) # upper left corner
    lr = (0,0) # lower right corner
    for sb in out:
        x1,y1,x2,y2 = map(int,re.findall("-?\d+\.?\d*",sb))
        md = man_dist([x1,y1],[x2,y2])
        sensors[(x1,y1)] = {"cb":(x2,y2),"md":md}
        x = min()
        floor = max(floor,y+1)
    return sensors


def part1(data):            # => 
    """Solve part 1."""


def part2(data):            # => 
    """Solve part 2."""

if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    # print(data)

    print("part 1:",part1(data))
    print("part 2:",part2(data))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))