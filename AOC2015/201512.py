# AOC 2015 - Day 12

import time
import re
import json

IN_FILE = "AOC2015/201512.txt"
# IN_FILE = "AOC2015\\201512.sample.txt"


def parse1():
    # read the file as one large string
    with open(IN_FILE) as f:
        out = f.read()
    return out


def parse2():
    with open(IN_FILE) as f:
        out = json.load(f)
    return out

def process_input(data):
    ttl = 0

    # dict: recusively process contents
    if isinstance(data, dict):
        if 'red' in data.values():
            return 0
        for key in data:
            ttl += process_input(data[key])

    # list: recusively process contents
    elif isinstance(data, list):
        for x in data:
            ttl += process_input(x) 

    # int: add the literal value to total and return
    elif isinstance(data, int):
        ttl += data

    return ttl

def part1(data):            # => 119433
    """Solve part 1."""
    all_numbers = map(int,re.findall("-?\d+\.?\d*",data))
    return sum(all_numbers)

def part2(data):            # => 68466
    """Solve part 2."""
    return process_input(data)

if __name__ == "__main__":
    timestart = time.time()

    print("part 1:",part1(parse1()))
    print("part 2:",part2(parse2()))
    
    timeend = time.time()
    print("Execution time: ", f"{timeend-timestart:0.4f}")

