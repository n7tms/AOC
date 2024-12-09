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
    
    antennas = {}
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] != '.':
                antennas[(r,c)] = data[r][c]


    return antennas




def part1(antennas):        # => 
    anti_nodes = set()

    for coords, antenna in antennas.items():
        for oa_r, oa_c in [key for key, value in antennas.items() if value == antenna]:
            # print(f'{other_ant} {antenna}')
            # calculate dr and dc to the node
            dr, dc = (coords[0] - oa_r) // 2, (coords[1] - oa_c) // 2

            # add a node to anti-nodes at a location that distance from this node (-) and from that node (+)
            if oa_r < coords[0]
            

        
        



    return len(anti_nodes)



def part2(calibrations):       # => 
    return 


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
        