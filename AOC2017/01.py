# AOC 2017 - Day 01
# tags: #zip 

import time

IN_File = "AOC2017/01.txt"

def parse():
    """Parse input."""
    with open(IN_File) as f:
        out = f.read().split('\n')

    # out = ['1212']
    out = out[0]
    digits = list(map(int,out))
    return digits
 

def part1(data):
    pairs = list(zip(data,data[1:]))
    total = 0
    for p in pairs:
        if p[0] == p[1]:
            total += p[0]
    if data[0] == data[len(data)-1]:
        total += data[0]
    return total

def part2(data):
    half = len(data) // 2
    total = 0
    for i in range(len(data)):
        i2 = (i + half) % len(data)
        if data[i] == data[i2]:
            total += data[i]
    return total    


if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    # print(data)

    print("part 1:",part1(data))
    print("part 2:",part2(data))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))