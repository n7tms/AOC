# AOC 2017 - Day 12
# tags: 

import time

IN_File = "AOC2017/12.txt"


def parse():
    with open(IN_File) as f:
        out = f.read().split(',')

    return out


def part1(data):    # 
    return 

def part2(data):    # 
    return 



if __name__ == "__main__":
    timestart = time.time()

    data1 = parse()

    print("part 1:",part1(data1))
    print("part 2:",part2(data1))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))