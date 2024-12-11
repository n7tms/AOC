# AOC 2018 day 16: 
#

import aoc_utils as aoc
import time
import os
import re
from collections import defaultdict

DAY = '16'
IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".sample.txt")

def parse():
    """
    Parse
    """
    aoc.get_input(2018,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().split('\n\n\n')
    
    examples = []
    for e in data[0].split('\n\n'):
        b, c, a = e.splitlines()
        before = list(map(int, re.findall(r'\d+', b)))
        code = list(map(int,c.split(' ')))
        after = list(map(int, re.findall(r'\d+', a)))
        examples.append([before, code, after])

    test_program = [list(map(int, tp.split(' '))) for tp in data[1].strip().splitlines()]

    return examples, test_program

#####################
# OpCode processors #
#####################

# addr
def addr(params, inregs):
    # params = registers A, B, C
    # regs = input registers 0, 1, 2, 3

    a,b,c = params

    outregs = inregs.copy()
    outregs[c] = inregs[a] + inregs[b]
    return outregs

# addi
def addi(params, inregs):
    # params = registers A, B, C
    # regs = input registers 0, 1, 2, 3

    a,b,c = params

    outregs = inregs.copy()
    outregs[c] = inregs[a] + b
    return outregs

# mulr
def mulr(params, inregs):
    # params = registers A, B, C
    # regs = input registers 0, 1, 2, 3

    a,b,c = params

    outregs = inregs.copy()
    outregs[c] = inregs[a] * inregs[b]
    return outregs

# muli
def muli(params, inregs):
    # params = registers A, B, C
    # regs = input registers 0, 1, 2, 3

    a,b,c = params

    outregs = inregs.copy()
    outregs[c] = inregs[a] * b
    return outregs

# banr
def banr(params, inregs):
    # params = registers A, B, C
    # regs = input registers 0, 1, 2, 3

    a,b,c = params

    outregs = inregs.copy()
    outregs[c] = inregs[a] & inregs[b]
    return outregs

# bani
def bani(params, inregs):
    # params = registers A, B, C
    # regs = input registers 0, 1, 2, 3

    a,b,c = params

    outregs = inregs.copy()
    outregs[c] = inregs[a] & b
    return outregs

# borr
def borr(params, inregs):
    # params = registers A, B, C
    # regs = input registers 0, 1, 2, 3

    a,b,c = params

    outregs = inregs.copy()
    outregs[c] = inregs[a] | inregs[b]
    return outregs

# bori
def bori(params, inregs):
    # params = registers A, B, C
    # regs = input registers 0, 1, 2, 3

    a,b,c = params

    outregs = inregs.copy()
    outregs[c] = inregs[a] | b
    return outregs

# setr
def setr(params, inregs):
    # params = registers A, B, C
    # regs = input registers 0, 1, 2, 3

    a,b,c = params

    outregs = inregs.copy()
    outregs[c] = inregs[a]
    return outregs

# seti
def seti(params, inregs):
    # params = registers A, B, C
    # regs = input registers 0, 1, 2, 3

    a,b,c = params

    outregs = inregs.copy()
    outregs[c] = a
    return outregs

# gtir
def gtir(params, inregs):
    # params = registers A, B, C
    # regs = input registers 0, 1, 2, 3

    a,b,c = params

    outregs = inregs.copy()
    outregs[c] = 1 if a > inregs[b] else 0
    return outregs

# gtri
def gtri(params, inregs):
    # params = registers A, B, C
    # regs = input registers 0, 1, 2, 3

    a,b,c = params

    outregs = inregs.copy()
    outregs[c] = 1 if inregs[a] > b else 0
    return outregs

# gtrr
def gtrr(params, inregs):
    # params = registers A, B, C
    # regs = input registers 0, 1, 2, 3

    a,b,c = params

    outregs = inregs.copy()
    outregs[c] = 1 if inregs[a] > inregs[b] else 0
    return outregs

# eqir
def eqir(params, inregs):
    # params = registers A, B, C
    # regs = input registers 0, 1, 2, 3

    a,b,c = params

    outregs = inregs.copy()
    outregs[c] = 1 if a == inregs[b] else 0
    return outregs

# eqri
def eqri(params, inregs):
    # params = registers A, B, C
    # regs = input registers 0, 1, 2, 3

    a,b,c = params

    outregs = inregs.copy()
    outregs[c] = 1 if inregs[a] == b else 0
    return outregs

# eqrr
def eqrr(params, inregs):
    # params = registers A, B, C
    # regs = input registers 0, 1, 2, 3

    a,b,c = params

    outregs = inregs.copy()
    outregs[c] = 1 if inregs[a] == inregs[b] else 0
    return outregs



def part1(examples):        # => 563
    more3 = 0
    for ins, code, outs in examples:
        m = 0
        if addr(code[1:],ins) == outs: m += 1
        if addi(code[1:],ins) == outs: m += 1
        if mulr(code[1:],ins) == outs: m += 1
        if muli(code[1:],ins) == outs: m += 1

        if banr(code[1:],ins) == outs: m += 1
        if bani(code[1:],ins) == outs: m += 1
        if borr(code[1:],ins) == outs: m += 1
        if bori(code[1:],ins) == outs: m += 1
        if setr(code[1:],ins) == outs: m += 1
        if seti(code[1:],ins) == outs: m += 1
        if gtir(code[1:],ins) == outs: m += 1
        if gtri(code[1:],ins) == outs: m += 1
        if gtrr(code[1:],ins) == outs: m += 1
        if eqir(code[1:],ins) == outs: m += 1
        if eqri(code[1:],ins) == outs: m += 1
        if eqrr(code[1:],ins) == outs: m += 1

        if m >= 3: more3 += 1


    return more3


def add_opcode(opcode, instr, opcodes):
    if instr in opcodes:
        opcodes[instr].add(opcode)
    else:
        opcodes[instr] = {opcode}
    return opcodes


def narrow_down_opcodes(candidates):
    final_opcodes = {}
    while candidates:
        # Find unique opcode candidates (those with exactly one opcode left)
        unique = {instr: list(opcodes)[0] for instr, opcodes in candidates.items() if len(opcodes) == 1}
        
        # Remove these unique opcodes from all other instruction sets
        for instr, opcode in unique.items():
            final_opcodes[instr] = opcode
            del candidates[instr]
            for opcodes in candidates.values():
                opcodes.discard(opcode)
    return final_opcodes




def part2(examples, test_program):        # =>  629
    # Create a dictionary of all of the opcodes the COULD match an instruction
    # (Stored in a set so duplicates are automatically removed)

    opcodes = defaultdict(set)

    for ins, code, outs in examples:
        if addr(code[1:],ins) == outs: 
            opcodes = add_opcode(code[0], 'addr', opcodes)
        if addi(code[1:],ins) == outs: 
            opcodes = add_opcode(code[0], 'addi', opcodes)
        if mulr(code[1:],ins) == outs: 
            opcodes = add_opcode(code[0], 'mulr', opcodes)
        if muli(code[1:],ins) == outs: 
            opcodes = add_opcode(code[0], 'muli', opcodes)
        if banr(code[1:],ins) == outs: 
            opcodes = add_opcode(code[0], 'banr', opcodes)
        if bani(code[1:],ins) == outs: 
            opcodes = add_opcode(code[0], 'bani', opcodes)
        if borr(code[1:],ins) == outs: 
            opcodes = add_opcode(code[0], 'borr', opcodes)
        if bori(code[1:],ins) == outs: 
            opcodes = add_opcode(code[0], 'bori', opcodes)
        if setr(code[1:],ins) == outs: 
            opcodes = add_opcode(code[0], 'setr', opcodes)
        if seti(code[1:],ins) == outs: 
            opcodes = add_opcode(code[0], 'seti', opcodes)
        if gtir(code[1:],ins) == outs: 
            opcodes = add_opcode(code[0], 'gtir', opcodes)
        if gtri(code[1:],ins) == outs: 
            opcodes = add_opcode(code[0], 'gtri', opcodes)
        if gtrr(code[1:],ins) == outs: 
            opcodes = add_opcode(code[0], 'gtrr', opcodes)
        if eqir(code[1:],ins) == outs: 
            opcodes = add_opcode(code[0], 'eqir', opcodes)
        if eqri(code[1:],ins) == outs: 
            opcodes = add_opcode(code[0], 'eqri', opcodes)
        if eqrr(code[1:],ins) == outs: 
            opcodes = add_opcode(code[0], 'eqrr', opcodes)

    # Figure out which opcodes are unique to each instruction
    final_opcodes = narrow_down_opcodes(opcodes)

    # Reverse the keys and values so I can lookup the opcodes
    the_opcodes = {value: key for key, value in final_opcodes.items()}

    # Execute test program ...................
    registers = [0,0,0,0]

    for program in test_program:
        opcode = program[0]
        inregs = program[1:]

        match the_opcodes[opcode]:
            case 'addr':
                registers = addr(inregs, registers)
            case 'addi':
                registers = addi(inregs, registers)
            case 'mulr':
                registers = mulr(inregs, registers)
            case 'muli':
                registers = muli(inregs, registers)
            case 'banr':
                registers = banr(inregs, registers)
            case 'bani':
                registers = bani(inregs, registers)
            case 'borr':
                registers = borr(inregs, registers)
            case 'bori':
                registers = bori(inregs, registers)
            case 'setr':
                registers = setr(inregs, registers)
            case 'seti':
                registers = seti(inregs, registers)
            case 'gtir':
                registers = gtir(inregs, registers)
            case 'gtri':
                registers = gtri(inregs, registers)
            case 'gtrr':
                registers = gtrr(inregs, registers)
            case 'eqir':
                registers = eqir(inregs, registers)
            case 'eqri':
                registers = eqri(inregs, registers)
            case 'eqrr':
                registers = eqrr(inregs, registers)
                
    return registers[0]



def solve():
    """Solve the puzzle for the given input."""
    e,t = parse()

    start_time = time.time()
    p1 = str(part1(e))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(e,t))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve()

