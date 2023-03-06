# AOC 2015 - Day 16

import time
import re

IN_FILE = "AOC2015/201516.txt"

mfcsam = {"children":'3',"cats":'7',"samoyeds":'2',"pomeranians":'3',"akitas":'0',"vizslas":'0',"goldfish":'5',"trees":'3',"cars":'2',"perfumes":'1'}


def parse():
    with open(IN_FILE) as f:
        out = [line for line in f.read().split('\n')]

    # Sue 12: samoyeds: 6, trees: 6, perfumes: 2
    sues = list()
    for line in out:
        regex = r"Sue\s*(\d+):\s*(\w+):\s*(\d+),\s*(\w+):\s*(\d+),\s*(\w+):\s*(\d+)"
        vals = re.match(regex,line)
        tmp = list(vals.groups())
        tmp.insert(0,'Sue')
        sue = {tmp[i]: tmp[i + 1] for i in range(0, len(tmp), 2)}
        sues.append(sue)

    return sues


def part1(data):    # => 213
    for sue in data:
        this_sue = 0
        matches = 0
        for item in sue.keys():
            if item == 'Sue':
                this_sue = sue[item]
            else:
                if item in mfcsam:
                    if mfcsam[item] == sue[item]:
                        matches += 1
                    else:
                        break
        if matches == 3:
            return this_sue

    return 0

def part2(data):    # => 323
    for sue in data:
        this_sue = 0
        matches = 0
        for item in sue.keys():
            if item == 'Sue':
                this_sue = sue[item]
            else:
                if item in mfcsam:
                    if item == 'cats' or item == 'trees':
                        if mfcsam[item] < sue[item]:
                            matches += 1
                    elif item == 'pomeranians' or item == 'goldfish':
                        if mfcsam[item] > sue[item]:
                            matches += 1
                    elif mfcsam[item] == sue[item]:
                        matches += 1
                    else:
                        break
        if matches == 3:
            return this_sue

    return 0


if __name__ == "__main__":
    timestart = time.time()

    puzzle_input = parse()

    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", f"{timeend-timestart:0.4f}")

