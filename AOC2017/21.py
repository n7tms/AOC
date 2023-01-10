# AOC 2017 - Day 21
# tags: #

import time

IN_File = "AOC2017/21.txt"

def parse():
    with open(IN_File) as f:
        out = f.read().split('\n')


def part1(data):    # 125
    pass

def part2(data):    # 1782917
    pass

if __name__ == "__main__":
    timestart = time.time()

    data = parse()

    print("part 1:",part1(data))
    print("part 2:",part2(data))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))