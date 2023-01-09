# AOC 2017 - Day 24
# tags: #

import time
from collections import deque

IN_File = "AOC2017/24.txt"

def parse():
    with open(IN_File) as f:
        out = f.read().split('\n')
    return out
   


def part1(instructions):    # 
    pass

def part2(instructions):    # 
    pass


if __name__ == "__main__":
    timestart = time.time()

    data = parse()

    print("part 1:",part1(data))
    print("part 2:",part2(data))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))