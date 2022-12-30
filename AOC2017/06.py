# AOC 2017 - Day 06
# tags: #regex #map

import time
import re

IN_File = "AOC2017/06.txt"
# sample = '0 2 7 0'

def parse():
    """Parse input."""
    with open(IN_File) as f:
        out = f.read().split('\n')

    return list(map(int,re.split('\s',out[0])))

def part2(data,cnt, first):    # part1: 6681; part2: 2392
    history = []

    while history.count(data) < cnt:
        x = data.copy()
        history.append(x)
        maxidx = data.index(max(data))
        maxval = data[maxidx]
        data[maxidx] = 0

        for i in range(maxidx+1,maxidx+maxval+1):
            data[i % len(data)] += 1

    return len(history) - first

if __name__ == "__main__":
    timestart = time.time()

    data1 = parse()
    # print(data1)
    data2 = data1.copy()

    first = part2(data1,1,0)
    print("part 1:",first)
    print("part 2:",part2(data2,2,first))
    
    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))