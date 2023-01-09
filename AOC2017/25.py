# AOC 2017 - Day 25
# tags: #

import time
from collections import deque

IN_File = "AOC2017/25.txt"

def parse():
    with open(IN_File) as f:
        out = f.read().split('\n')
    
    for line in out:
        state = ''
        if 'In state' in line:
            state = 



def part1(components):    # 
    pass

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