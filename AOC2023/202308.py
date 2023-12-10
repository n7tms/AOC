# AOC 2023 day 8: Haunted Wasteland
#

import aoc_utils as aoc
import time
import os
from collections import defaultdict
import re
from math import lcm

IN_FILE = os.path.join("AOC2023","inputs","202308.in")
# IN_FILE = os.path.join("AOC2023","inputs","202308.sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2023,8,False)

    with open(IN_FILE) as fp:
        directions, nodes = fp.read().split("\n\n")
    
    # LDM = (MRM, JKJ)
    parsed_nodes = {}
    for x in nodes.split("\n"):
        # n,l,r = re.findall(r'(\w+) = \((\w+), (\w+)\)',x)
        tmp = re.match(r'(\w+) = \((\w+), (\w+)\)',x)
        n = tmp.group(1)
        l = tmp.group(2)
        r = tmp.group(3)
        parsed_nodes[n] = (l,r)
     
    return directions,parsed_nodes



def part1(directions, nodes):        # => 
    """
    Solve part 1
    
    """
    cur_node = 'AAA'
    end_node = 'ZZZ'
    moves = 0
    while cur_node != end_node:
        d = directions[moves % len(directions)]
        side = 0 if d == 'L' else 1
        cur_node = nodes[cur_node][side]
        moves += 1

    return moves


def finished(nodes):
    for node in nodes:
        if node[2] != 'Z':
            return False
    return True


def part2(directions,nodes):            # => 
    """
    Solve part 2
    """

    cur_nodes = []
    # find all nodes that end with A
    for node in nodes.items():
        k,v = node
        if k[2] == 'A':
            cur_nodes.append(k)
    
    total_moves = []
    for cn in cur_nodes:
        moves = 0
        cur_node = cn
        while cur_node[2] != 'Z':
            d = directions[moves % len(directions)]
            side = 0 if d == 'L' else 1
            cur_node = nodes[cur_node][side]
            moves += 1
        total_moves.append(moves)

    total_total_moves = lcm(*total_moves)
    return total_total_moves


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    directions,nodes = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(directions,nodes))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(directions,nodes))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        