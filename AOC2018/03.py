# AOC 2018 day 03: 
#

import aoc_utils as aoc
import time
import os
import re

DAY = '03'
IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".sample.txt")


def assemble_set(claim):
    # claim_set = set()
    # for r in range(claim['height']):
    #     for c in range(claim['width']):
    #         claim_set.add((claim['row']+r,claim['col']+c))
    # return claim_set

    # this set comprehension is a bit faster and much more pythonic!
    return {
        (claim['row'] + r, claim['col'] + c)
        for r in range(claim['height'])
        for c in range(claim['width'])
    }

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2018,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()

    claims = {}
    for line in data:
        matches = re.findall(r'\d+', line)
        claim, col, row, width, height = matches
        claims[claim] = {'row':int(row), 'col':int(col), 'width':int(width), 'height':int(height)}
        claims[claim]['claim_set'] = set(assemble_set(claims[claim]))

    return claims


def part1(claims):        # => 115348
    fabric = set()
    overlap = set()
    for claim in claims:
        claim_set = claims[claim]['claim_set']
        if  claim_set & fabric:
            overlap.update(claims[claim]['claim_set'] & fabric)
        fabric.update(claim_set)

    return len(overlap)



def part2(claims):       # => Claim # 188
    # add claims set to the claims
    # iterate through all the claims
    # if a claim does not intersect with any other claims -- you found it!

    # for claim in claims:
    #     claims[claim]["claim_set"] = assemble_set(claims[claim])
    
    # for k in claims:
    #     unique = True
    #     for k2 in claims:
    #         if k != k2:
    #             if claims[k]['claim_set'] & claims[k2]['claim_set']:
    #                 unique = False
    #     if unique: return k

    for k, v in claims.items():
        if all(v['claim_set'].isdisjoint(claims[k2]['claim_set']) for k2 in claims if k != k2):
            return k

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(data))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(data))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)

