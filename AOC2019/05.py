# AOC 2019 - Day 05
# tags: 

import time
import intcode as ic

IN_File = "AOC2019/05.txt"

def parse():
    with open(IN_File) as f:
        out = f.read().split(',')
    prgm = list(map(int,out))
    return prgm


def part1(data):    # 
    ic.run()

def part2(data):    # 
    pass


if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    data2 = data[:]

    print("part 1:",part1(data))
    print("part 2:",part2(data))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))