# AOC 2017 - Day 11
# tags: #hexgrid
# see https://redblobgames.com/grids/hexagons

import time

IN_File = "AOC2017/11.txt"


def parse():
    with open(IN_File) as f:
        out = f.read().split(',')
    return out

def distance(q,r):
    return (abs(0 - q) + abs(0 + 0 - q - r) + abs(0 - r)) // 2

def part12(data):    # part1: 643; part2: 1471
    q,r = 0,0   # home/start location
    maxdist = 0

    for dir in data:
        if dir == 'n':
            r -= 1
        elif dir == 's':
            r += 1
        elif dir == 'nw':
            q -= 1
        elif dir == 'se':
            q += 1
        elif dir == 'ne':
            q += 1
            r -= 1
        elif dir == 'sw':
            q -= 1
            r += 1
        maxdist = max(maxdist,distance(q,r))    # furthest distance so far

    # calculate final distance from home
    dist = distance(q,r)

    return dist,maxdist



if __name__ == "__main__":
    timestart = time.time()

    data1 = parse()

    print("part 1,2:",part12(data1))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))