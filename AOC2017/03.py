# AOC 2017 - Day 03
# tags: 

import time
import math

# IN_File = "AOC2017/03.txt"
INPUT = 325489
# INPUT = 100



def part1(data):    # 552
    # if num is '27', ring = sqrt(27) to (sqrt(27)+2)**2
    base = int(math.sqrt(data)) # the size of the edge of the ring
    if base % 2 == 0: base -= 1

    # distance from middle of edge 
    dmid = (base + 1) // 2

    # length of edge
    loe = base + 2

    # distance around ring
    dar = (base + 1) * 4

    # relative location on the edge
    # rloe = ((((base + 2) ** 2) - data) % loe) // 2

    rloe = (data % (base ** 2)) %  dmid
    distance = base - 1 + dmid - rloe - 1

    


    return distance

def part2(data):    #
    checksum = 0

    return checksum

if __name__ == "__main__":
    timestart = time.time()

    # data = parse()
    # print(data)

    print("part 1:",part1(INPUT))
    print("part 2:",part2(INPUT))
    
    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))