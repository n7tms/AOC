# AOC 2024 day 23: 
#

import aoc_utils as aoc
import time
import os
from itertools import combinations

DAY = '23'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()

    parsed = [(l,r) for line in data for l,r in [line.split('-')]]

    connections = {}
    for a,b in parsed:
        connections.setdefault(a,set()).add(b)
        connections.setdefault(b,set()).add(a)

    return connections


def part1(connections):        # => 1437
    threes = set()
    for a,b,c in combinations(connections.keys(),3):
        if b in connections[a] and c in connections[a] and c in connections[b]:
            threes.add(tuple([a,b,c]))
    
    starts_with_t = sum(1 for a, b, c in threes if 't' in [a[0],b[0],c[0]])
    return starts_with_t


def part2(connections):       # => da,do,gx,ly,mb,ns,nt,pz,sc,si,tp,ul,vl
    groups = []
    aoc.bron_kerbosch(set(), set(connections.keys()), set(), connections, groups)
    largest_group = max(groups, key=len)

    largest_group_list = list(largest_group)
    largest_group_list.sort()
    return ','.join(largest_group_list)



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
        