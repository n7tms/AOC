# AOC 2019 - Day 06
# tags: 

import time
import intcode as ic

IN_File = "AOC2019/06.txt"

def parse():
    with open(IN_File) as f:
        out = f.read().split('\n')


def parse():
    return list(map(int,IN_File.split('-')))


def valid_pwd(pwd):
    pass

def part1(data):    # 
    pass

def part2(data):    # 
    pass


if __name__ == "__main__":
    timestart = time.time()

    data = parse()

    print("part 1:",part1(data))
    print("part 2:",part2(data))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))