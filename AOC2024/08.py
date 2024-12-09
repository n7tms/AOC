# AOC 2024 day 08: 
#

import aoc_utils as aoc
import time
import os

DAY = '08'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")


def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()
    
    maxr = len(data)
    maxc = len(data[0])

    # we don't need the entire grid; just return the location of the antennas
    antennas = {}
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] != '.':
                antennas[(r,c)] = data[r][c]

    return antennas, maxr, maxc



def part1(antennas, maxr, maxc):        # => 359
    anti_nodes = set()

    for (r1, c1), antenna in antennas.items():
        for r2, c2 in [key for key, value in antennas.items() if value == antenna and key != (r1,c1)]:
            # if (oa_r,oa_c) == coords: continue # skip if this is the same node

            # calculate dr and dc to the node
            dr, dc = r1 - r2, c1 - c2

            # add a node to anti-nodes at a location that distance from this node (-) and from that node (+)
            node1r, node1c = r1 + dr, c1 + dc
            node2r, node2c = r2 - dr, c2 - dc

            if 0 <= node1r < maxr and 0 <= node1c < maxc:
                anti_nodes.add((node1r,node1c))
            if 0 <= node2r < maxr and 0 <= node2c < maxc:
                anti_nodes.add((node2r,node2c))

    return len(anti_nodes)



def part2(antennas, maxr, maxc):       # => 1293
    anti_nodes = set()

    for coords, antenna in antennas.items():
        for oa_r, oa_c in [key for key, value in antennas.items() if value == antenna and key != coords]:
            # if (oa_r,oa_c) == coords: continue # skip if this is the same node

            # calculate dr and dc to the node
            dr, dc = coords[0] - oa_r, coords[1] - oa_c

            # add a node to anti-nodes at a location that distance from this node (-) and from that node (+)
            # and keep adding them until we run off the map...
            node1r, node1c = coords
            while 0 <= node1r < maxr and 0 <= node1c < maxc:
                anti_nodes.add((node1r,node1c))
                node1r, node1c = node1r + dr, node1c + dc

            node2r, node2c = oa_r, oa_c
            while 0 <= node2r < maxr and 0 <= node2c < maxc:
                anti_nodes.add((node2r,node2c))
                node2r, node2c = node2r - dr, node2c - dc
   
    return len(anti_nodes) 


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data,mr,mc = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(data,mr,mc))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(data,mr,mc))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        