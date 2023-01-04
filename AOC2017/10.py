# AOC 2017 - Day 10
# tags: 

import time

IN_File = "AOC2017/10.txt"

def parse():
    """Parse input."""
    with open(IN_File) as f:
        out = f.read().split('\n')

    return out[0]
    # return IN_FILE


def part1(data):    # 
    score = 0
    return score

def part2(data):    # 
    ncc = 0 # non-cancelled characters
    return ncc

if __name__ == "__main__":
    timestart = time.time()

    data1 = parse()
    # print(data)
    # data2 = data1.copy()

    print("part 1:",part1(data1))
    print("part 2:",part2(data1))
    
    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))