# AOC 2022 - Day 4
# This solution adopted from https://www.reddit.com/r/adventofcode/comments/zc0zta/2022_day_4_solutions/iyub5rp/?context=3

import time
timestart = time.time()

IN_FILE = "d:\\Dev\AOC2022\\202204.txt"

def part1():
    overlaps = 0
    for line in open(IN_FILE):
        # replace the '-' with commas, split on the commas, and convert all the values to ints
        e1s,e1e,e2s,e2e = map(int,line.replace('-',',').split(','))
        if e1s <= e2s and e1e >= e2e or e2s <= e1s and e2e >= e1e:
            overlaps += 1
    return overlaps

def part2():
    overlaps = 0
    for line in open(IN_FILE):
        e1s,e1e,e2s,e2e = map(int,line.replace('-',',').split(','))
        if e2s <= e1s <= e2e or e2s <= e1e <= e2e or e1s <= e2s <= e1e or e1s <= e2e <= e1e:
            overlaps += 1
    return overlaps

    
print("part 1: ", part1())
print("part 2: ", part2())
timeend = time.time()
print(timeend-timestart)
 