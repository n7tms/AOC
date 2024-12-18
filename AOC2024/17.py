# AOC 2024 day 17: 
#

import aoc_utils as aoc
import time
import os
import re

DAY = '17'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sampleb.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().split("\n\n")

    registers = list(map(int,re.findall('\d+',data[0])))
    program = list(map(int,re.findall('\d+',data[1])))

    return program, registers



def part1(pgm, regs):        # => 4,1,5,3,1,5,3,5,7
    """
    Solve part 1
    
    """
    outs = ''
    ip = 0
    while ip < len(pgm):
        opcode = pgm[ip]
        operand = pgm[ip+1]

        if operand < 4: opval = operand
        elif operand == 4: opval = regs[0]
        elif operand == 5: opval = regs[1]
        elif operand == 6: opval = regs[2]
        else: break
    
        if opcode == 0: # adv
            regs[0] = regs[0] // 2**opval

        elif opcode == 1: # bxl
            regs[1] = regs[1] ^ operand
        elif opcode == 2: # bst
            regs[1] = opval % 8
        elif opcode == 3: #jnz
            if regs[0] != 0:
                ip = operand - 2
        elif opcode == 4: # bxc
            regs[1] = regs[1] ^ regs[2]
        elif opcode == 5: # out
            outs = outs + str(opval % 8) + ','
        elif opcode == 6: # bdv
            regs[1] = regs[0] // 2**opval
        elif opcode == 7: #cdv
            regs[2] = regs[0] // 2**opval

        ip += 2

    return outs[:-1]



def part2(pgm, regs):       # => 
    """
    Solve part 2
    """
    localregs = list(regs)
    localpgm = ','.join(map(str,pgm))
    result = ''
    for x in range(30000000000000,9000000000000000):
        localregs = [x,0,0]
        result = part1(pgm,localregs)
        if result == localpgm:
            return x
        elif len(result) > 27:
            print(result)
    
    return f'not found ({len(result)}: {result})'


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    p,r = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(p,r))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(p,r))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        