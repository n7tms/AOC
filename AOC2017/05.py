# AOC 2017 - Day 05
# tags: 

import time

IN_File = "AOC2017/05.txt"

def parse():
    """Parse input."""
    with open(IN_File) as f:
        out = f.read().split('\n')

    return list(map(int,out))


def part1(data):    # 325922
    steps = 0
    idx = 0
    while idx > -1 and idx < len(data):
        next_idx = idx + data[idx]
        data[idx] += 1
        idx = next_idx
        steps += 1
    return steps

def part2(data):    # 24490906
    steps = 0
    idx = 0
    while idx > -1 and idx < len(data):
        next_idx = idx + data[idx]
        
        if data[idx] >= 3:
            data[idx] -= 1
        else:
            data[idx] += 1
        idx = next_idx
        steps += 1
    return steps

if __name__ == "__main__":
    timestart = time.time()

    data1 = parse()
    # print(data)
    data2 = data1.copy()

    print("part 1:",part1(data1))
    print("part 2:",part2(data2))
    
    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))