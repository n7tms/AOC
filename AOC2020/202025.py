# AOC 2020 - Day 25
# tags:  #encrypt

import time

IN_FILE = "AOC2020\\202025.txt"
# IN_FILE = "AOC2020\\202024.sample.txt"


def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        out = f.read().split('\n')
    cpk = int(out[0])
    dpk = int(out[1])
    return cpk,dpk

def part1(data):        # => 18293391
    v, ls = 1, 0
    while v != data[0]:
        v = v * 7
        v = v % 20201227
        ls += 1

    return pow(data[1], ls, 20201227)
   

if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    # print(data)

    print("part 1:",part1(data))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))