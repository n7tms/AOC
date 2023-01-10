# AOC 2019 - Day 1
# tags: 

import time

IN_File = "AOC2019/01.txt"

def parse():
    with open(IN_File) as f:
        out = f.read().split('\n')
    
    masses = list(map(int,out))
    return masses


def part1(data):    # 3256794
    fuel = sum(list((x//3)-2 for x in data))
    return fuel

def part2(data):    # 4882337
    total_fuel = 0

    for x in data:
        f = (x // 3) - 2
        while f>0:
            total_fuel += f
            f = (f // 3) - 2

    return total_fuel
    

if __name__ == "__main__":
    timestart = time.time()

    data = parse()

    print("part 1:",part1(data))
    print("part 2:",part2(data))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))