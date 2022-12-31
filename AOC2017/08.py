# AOC 2017 - Day 08
# tags: 

import time
import re

IN_File = "AOC2017/08.txt"
registers = {}

def parse():
    """Parse input."""
    with open(IN_File) as f:
        out = f.read().split('\n')
    return out

def part1(data):    # part1: 7296; part2: 8186
    max_memory = 0
    for line in data:
        instr = line.split(' ',4)
        reg,ud,mag,_,cond = instr
        if reg not in registers:
            registers[reg] = 0

        condition = cond.split(' ')
        reg2,op,val = condition
        if reg2 not in registers:
            registers[reg2] = 0
        cnd = str(registers[reg2]) + op + val
        if eval(cnd):
            if ud == 'inc':
                registers[reg] += int(mag)
            else:
                registers[reg] -= int(mag)
        max_memory = max(max_memory,registers[reg])

    return registers[max(registers, key=registers.get)],max_memory



if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    # print(data)

    maxreg,maxmem = part1(data)

    print("part 1:",maxreg)
    print("part 2:",maxmem)
    
    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))