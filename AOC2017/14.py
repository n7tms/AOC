# AOC 2017 - Day 14
# tags: #hash #hex #binary

import time
from functools import reduce

INPUT = "amgozmfv-"

def knothash(inp):
    lof = list(range(256))  # list of numbers, 0-255
    curpos = 0
    skip = 0

    inp = list(map(ord,inp)) +  [17, 31, 73, 47, 23]

    for _ in range(64):
        curpos = curpos % 256
        for l in inp:
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


def part1():    # 8222
    knothashes = []
    for r in range(128):
        hash_in = INPUT + str(r)
        aknothash = knothash(hash_in)
        x = f'{int(aknothash,16):0>128b}'
        knothashes.append(x)

    used_squares = 0
    for y in knothashes:
        used_squares += y.count('1')
    return used_squares, knothashes

def part2(knothashes):    # 1086
    seen = set()
    groups = 0
    def search(i, j):
        if ((i, j)) in seen:
            return
        if not int(knothashes[i][j]):
            return
        seen.add((i, j))
        if i > 0:
            search(i-1, j)
        if j > 0:
            search(i, j-1)
        if i < 127:
            search(i+1, j)
        if j < 127:
            search(i, j+1)

    for i in range(128):
        for j in range(128):
            if (i,j) in seen:
                continue
            if not int(knothashes[i][j]):
                continue
            groups += 1
            search(i, j)
    return groups


if __name__ == "__main__":
    timestart = time.time()

    used,khs = part1()
    grps = part2(khs)

    print("part 1:",used)
    print("part 2:",grps)

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))