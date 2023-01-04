# AOC 2017 - Day 10
# tags: #hash #reduce #hex #ord

import time
from functools import reduce

IN_File = "AOC2017/10.txt"

def parse1():
    with open(IN_File) as f:
        out = f.read().split(',')

    out = list(map(int,out))
    return out

def parse2():
    with open(IN_File) as f:
        out = f.read().split('\n')

    output = []
    for a in out[0]:
        output.append(ord(a))
    
    output.extend([17, 31, 73, 47, 23])
    return output


def part1(lengths):    # 23715
    lof = list(range(256))  # list of numbers, 0-255
    # lof = list(range(5))  # list of numbers, 0-255
    curpos = 0
    skip = 0

    # lengths = [3,4,1,5]
    for l in lengths:
        for x in range(l//2):
            front = (curpos + x) % 256
            rear = (curpos + l - 1 - x) % 256
            tmp = lof[front]
            lof[front] = lof[rear]
            lof[rear] = tmp
        curpos += l + skip
        skip += 1

    return lof[0] * lof[1]

def part2(lengths):    # 541dc3180fd4b72881e39cf925a50253
    lof = list(range(256))  # list of numbers, 0-255
    curpos = 0
    skip = 0

    for _ in range(64):
        curpos = curpos % 256
        for l in lengths:
            for x in range(l//2):
                front = (curpos + x) % 256
                rear = (curpos + l - 1 - x) % 256
                tmp = lof[front]
                lof[front] = lof[rear]
                lof[rear] = tmp
            curpos += l + skip
            skip += 1

    densehash = []
    for x in range(16):
        group = lof[16*x:16*x+16]
        densehash.append('%02x'%reduce((lambda x,y: x ^ y),group))
    knothash = ''.join(densehash)

    return knothash


if __name__ == "__main__":
    timestart = time.time()

    data1 = parse1()
    data2 = parse2()

    print("part 1:",part1(data1))
    print("part 2:",part2(data2))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))