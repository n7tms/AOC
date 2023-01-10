# AOC 2019 - Day 2
# tags: #intcode

import time
import intcode as ic

IN_File = "AOC2019/02.txt"

def parse():
    with open(IN_File) as f:
        out = f.read().split(',')
    
    prgm = list(map(int,out))
    return prgm


def part1(data):    # 3790645
    return ic.run(12,2,data)

def part2(data):    # 6577
    target_output = 19690720
    tmp = data[:]

    for a in range(100):
        for b in range(100):
            if ic.run(a,b,data) == target_output:
                return (a * 100) + b
            data = tmp[:]
    
    return "no solution found"


if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    data2 = data[:]

    print("part 1:",part1(data))
    print("part 2:",part2(data2))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))