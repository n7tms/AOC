# AOC 2017 - Day 09
# tags: #nested

import time

IN_File = "AOC2017/09.txt"

def parse():
    """Parse input."""
    with open(IN_File) as f:
        out = f.read().split('\n')

    return out[0]


def part(data):    # part1: 14421; part2: 6817
    score = 0
    ncc = 0 # non-cancelled characters
    level = 0
    garbage = False
    i = 0
    while i < len(data):
        if data[i] == '{' and not garbage:
            level += 1
            score += level
        elif data[i] == '!':
            i += 1
        elif data[i] == '}' and not garbage:
            level -= 1
        elif data[i] == '<' and not garbage:
            garbage = True
        elif data[i] == '>' and garbage:
            garbage = False
        elif garbage:
            ncc += 1
        i += 1
    return score,ncc

if __name__ == "__main__":
    timestart = time.time()

    data1 = parse()
    score,ncc = part(data1)

    print("part 1:",score)
    print("part 2:",ncc)
    
    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))