# AOC 2024 day 24: 
#

import aoc_utils as aoc
import time
import os
import re

DAY = '24'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().split('\n\n')

    initial_states = dict()
    for s in data[0].splitlines():
        wire,val = s.split(': ')
        initial_states[wire] = int(val)
    
    pattern = r'\w+|->'
    connections = []
    for outputs in data[1].splitlines():
        result = re.findall(pattern, outputs)
        connections.append([result[0],result[1],result[2],result[4]])
        for wire in [result[0],result[2],result[4]]:
            if wire not in initial_states:
                initial_states[wire] = -1
    
    return initial_states, connections


def part1(states, connections):        # => 63168299811048

    done = False
    while not done:
        for s0, op, s1, d in connections:
            if states[s0] > -1 and states[s1] > -1:
                if op == 'AND':
                    states[d] = states[s0] & states[s1]
                elif op == 'OR':
                    states[d] = states[s0] | states[s1]
                elif op == 'XOR':
                    states[d] = states[s0] ^ states[s1]
        
        done = True
        for k,v in states.items():
            if k[0] == 'z' and v < 0:
                done = False
    
    z_keys = sorted([k for k in states.keys() if k.startswith('z')], reverse=True)
    binary = ''.join([str(states[k]) for k in z_keys])
    decimal = int(binary,2)

    return decimal


def part2(states, connections):       # => 
    bad_zs = []
    for s0,op,s1,d in connections:
        if d[0] == 'z' and op != 'XOR':
            bad_zs.append('1-'+d)
        elif (d[0] != 'z' and (s0[0] not in ['x','y'] and s1[0] not in ['x','y'])) and op == 'XOR':
            bad_zs.append(f'2- {d} ({s0} {s1})')

    return bad_zs


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    s,c = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(s,c))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(s,c))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        