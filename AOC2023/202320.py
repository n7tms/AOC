# AOC 2023 day 20: Pulse Propagation
#

import aoc_utils as aoc
import time
import os
import numpy as np
import re
from collections import deque

DAY = 20
# IN_FILE = os.path.join("AOC2023","inputs","2023"+str(DAY)+".in")
IN_FILE = os.path.join("AOC2023","inputs","2023"+str(DAY)+".sample.a.txt")
# IN_FILE = os.path.join("AOC2023","inputs","2023"+str(DAY)+".sample.b.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2023,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().split("\n")
    
    mod_cfg = {}
    pattern = re.compile(r'^([%&]?)([a-zA-Z]+) -> (.+)$')

    for line in data:
        match = pattern.match(line)
        if match:
            module_type, module_name, destinations = match.groups()
            destination_list = [dest.strip() for dest in destinations.split(',')]
            mod_cfg[module_name] = {'type': module_type, 'destinations': destination_list, 'state':False}        

    return mod_cfg


def part1(data, target_cycles=1):        # => 
    """
    Solve part 1
    
    """
    
    cycles = 0
    low_pulses = 0
    high_pulses = 0
    q = deque()

    while cycles < target_cycles:
        cur_mod = 'broadcaster'
        pulse = False # False=low; True=high

        q.append(cur_mod)
        while q:
            cur_mod = q.popleft()
            for dst in data[cur_mod]['destinations']:
                mod_type = data[dst]['type']
                mod_dst = data[dst]['destinations']

                if mod_type == '%':     # flip-flop
                    if pulse==0 and data[dst]['state']==0:
                        data[dst]['state']==1
                    elif pulse==1 and data[dst]['state']==1:
                        data[dst]['state']==0

                elif mod_type == '&':   # conjunction
                    data[dst]['state'] = pulse
                else:
                    print(f"unknown module type encountered [{mod_type}]")
                    cycles = target_cycles
                    break

                q.append(dst)


    total_pulses = low_pulses * high_pulses
    return total_pulses


def part2(data):            # => 
    """
    Solve part 2
    """


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
        