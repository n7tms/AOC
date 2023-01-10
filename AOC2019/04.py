# AOC 2019 - Day 2
# tags: #set #direction

import time

IN_File = "AOC2019/03.txt"
DIRS = {'U':[-1,0],'R':[0,1],'D':[1,0],'L':[0,-1]}

def parse():
    with open(IN_File) as f:
        out = f.read().split('\n')
    lines = [[],[]]
    for idx,wire in enumerate(out):
        x,y = 0,0
        for dir in wire.split(','):
            d,m = dir[0],int(dir[1:])
            for pnt in range(1,m+1):
                x += DIRS[d][0]
                y += DIRS[d][1]
                lines[idx].append(tuple([x,y]))

    return lines


def part1(data):    # 1519
    intersection_distance = 999999
    intersections = list(set(data[0]) & set(data[1]))

    for a in intersections:
        distance = abs(a[0]) + abs(a[1])
        intersection_distance = min([intersection_distance,distance])

    return intersection_distance

def part2(data):    # 14358
    intersections = list(set(data[0]) & set(data[1]))
    shortest_steps = 999999

    for x in intersections:
        distance = data[0].index(x) + data[1].index(x)
        shortest_steps = min([shortest_steps,distance])

    return shortest_steps + 2

if __name__ == "__main__":
    timestart = time.time()

    data = parse()

    print("part 1:",part1(data))
    print("part 2:",part2(data))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))