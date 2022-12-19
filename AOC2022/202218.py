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
    for cube in data:
        x,y,z = cube
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
            
    



def part2(data):            # => 1562536022966
    """Solve part 2."""

if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    # print(data)

    print("part 1:",part1(data))
    print("part 2:",part2(data))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))