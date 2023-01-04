# AOC 2017 - Day 13
# tags: 

import time

IN_File = "AOC2017/13.txt"


def parse():
    with open(IN_File) as f:
        out = f.read().split('\n')
    
    return


def part1(data):    # 
    return

def part2(data):    # 
    return


if __name__ == "__main__":
    timestart = time.time()

    data = parse()

    print("part 1:",part1(data))
    print("part 2:",part2(data))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))