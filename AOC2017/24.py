# AOC 2017 - Day 24
# tags: #pathfinding #djikstra

import time
from collections import deque

IN_File = "AOC2017/24.z.txt"

def parse():
    with open(IN_File) as f:
        out = f.read().split('\n')

    components = [list(map(int,c.split('/'))) for c in out]
    return components
   
def build_bridge(start, components):
    pass
    # create a new bridge, bridge[]
    # add start to the bridge
    # end = start[1]
    # search through components for another that begins or ends with end
    # if not in bridge, add it
    # set end = to the other end of that one
    # recurse

    # if not more components found, add up the strength in bridge and return.

    # this only checks the first that is found; need to recurse through all the components.



def part1(components):    # 
    strength = 0
    for c in components:
        if c[0] == 0:
            s = build_bridge(0,components)
            strength = max(list(s,strength))

def part2(instructions):    # 
    pass


if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    data2 = data[:]

    print("part 1:",part1(data))
    print("part 2:",part2(data2))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))