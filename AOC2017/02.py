# AOC 2017 - Day 02
# tags: 

import time
# from itertools import combinations

IN_File = "AOC2017/02.txt"

def parse():
    """Parse input."""
    with open(IN_File) as f:
        out = f.read().split('\n')

    return list([int(x) for x in line.split(' ') if x.isnumeric()] for line in out)
 

def part1(data):    # 54426
    return sum(max(row) - min(row) for row in data)

def part2(data):    #333
    checksum = 0
    for row in data:
        lc = list()
        for i in range(len(row)):
            for j in range(len(row)):
                if i == j: continue
                else: 
                    if row[i] > row[j]: # only a greater num mod a lower number could produce a valid result
                        lc.append([row[i],row[j]])


        # iterate through the valid responses looking for the checksum values
        checksum += [k[0] // k[1] for k in lc if k[0] % k[1] == 0][0]

    return checksum

if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    # print(data)

    print("part 1:",part1(data))
    print("part 2:",part2(data))
    
    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))