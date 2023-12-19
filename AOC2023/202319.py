# AOC 2023 day 19: Aplenty
#

import aoc_utils as aoc
import time
import os
import numpy as np
import re

DAY = 19
IN_FILE = os.path.join("AOC2023","inputs","2023"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2023","inputs","2023"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2023,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().split("\n\n")
    
    a,b = data[0].split('\n'), data[1].split('\n')

    workflows = {}
    for workflow in a:
        match = re.match(r"(\w+){(.+)}", workflow)
        if match:
            name, actions = match.groups()
            workflows[name] = actions.split(',')

    parts = []
    for item in b:
        matches = re.match(r'{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}',item)
        if matches:
            parts.append({
                'x': int(matches.group(1)),
                'm': int(matches.group(2)),
                'a': int(matches.group(3)),
                's': int(matches.group(4))
            })

    return workflows, parts




def part1(data):        # => 487623
    """
    Solve part 1
    
    """
    workflows, parts = data

    accepted = []

    for part in parts:
        pc = 'in'
        # branch = ''
        while not (pc == 'A' or pc == 'R'):
            wfs = workflows[pc]
            for wf in wfs:
                if wf == 'A' or wf == 'R': 
                    pc = wf
                    break
                if ':' in wf:
                    exp,branch = wf.split(':')
                    m = part[exp[0]]
                    n = exp[1:]
                    o = str(str(m)+n)
                    g = eval(str(str(part[exp[0]])+exp[1:]))
                    if g:
                        pc = branch
                        break
                else:
                    pc = wf
                    break
        
        if pc == 'A':
            accepted.append(sum(part.values()))

    return sum(accepted)


def part2(data):            # => 
    """
    Solve part 2
    """
    print(4000*(4000-537)*2439*(4000-3449)*1415*(4000-2663)*(4000-839)*(4000-2006)*(4000-2091)*1716)
    print(4000*4000*4000*4000)
    print(167409079868000)

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
        