# AOC 2017 - Day 07
# tags: #graph #regex

import time
import re

IN_File = "AOC2017/07.z.txt"

def parse():
    """Parse input."""
    with open(IN_File) as f:
        out = f.read().split('\n')



def part1(data):    # 
    steps = 0
    return steps

def part2(data):    # 
    steps = 0
    return steps

if __name__ == "__main__":
    timestart = time.time()

    data1 = parse()
    # print(data)
    data2 = data1.copy()

    print("part 1:",part1(data1))
    print("part 2:",part2(data2))
    
    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))