# AOC 2022 - Day 18

import time

IN_FILE = "AOC2022\\inputs\\202218.txt"
# IN_FILE = "AOC2022\\inputs\\202218.sample.txt"


def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        out = f.read().split('\n')
    cubes = []
    for line in out:
        x,y,z = map(int,line.split(','))
        cubes.append([x,y,z])
    return cubes


def part1(data):            # => 3374
    """Solve part 1."""
    not_connected = 0
    for x,y,z in data:
        if [x+1,y,z] not in data:
            not_connected += 1
        if [x,y+1,z] not in data:
            not_connected += 1
        if [x,y,z+1] not in data:
            not_connected += 1
        if [x-1,y,z] not in data:
            not_connected += 1
        if [x,y-1,z] not in data:
            not_connected += 1
        if [x,y,z-1] not in data:
            not_connected += 1
    return not_connected
            
def is_exposed(data,x,y,z):
    not_connected = 0
    for x,y,z in data:
        if [x+1,y,z] not in data:
            not_connected += 1
        if [x,y+1,z] not in data:
            not_connected += 1
        if [x,y,z+1] not in data:
            not_connected += 1
        if [x-1,y,z] not in data:
            not_connected += 1
        if [x,y-1,z] not in data:
            not_connected += 1
        if [x,y,z-1] not in data:
            not_connected += 1
    return not_connected


def part2(data):            # => 2010
    """Solve part 2."""
    xs,ys,zs,xm,ym,zm = 2,2,2,2,2,2
    for x,y,z in data:
        xs = max([xs,x])
        ys = max([ys,y])
        zs = max([zs,z])
        xm = min([xm,x])
        ym = min([ym,y])
        zm = min([zm,z])
    print(xm,ym,zm,xs,ys,zs)
    exposed = 0
    for x,y,z in data:
        if x == xs or x == xm or y == ys or y == ym or z == zm or z == zs:
            exposed += is_exposed(data,x,y,z)
    return exposed
        







if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    # print(data)

    print("part 1:",part1(data))
    print("part 2:",part2(data))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))