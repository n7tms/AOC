# AOC 2017 - Day 23
# tags: #program

import time
from collections import deque

IN_File = "AOC2017/23.txt"

def parse():
    with open(IN_File) as f:
        out = f.read().split('\n')
    return out
    

def execute(registers,q,ptr):
    # I added support for 'sub' and 'jnz' and reused day 18's code

    snd = None
    wt = False
    mult_count = 0

    instr = data[ptr].split(' ')
    cmd,reg = instr[0],instr[1]
    if len(instr) > 2:
        val = instr[2]
        # if val is not a literal, get its value
        if  val.isnumeric() or val[0] == '-':
            val = int(val)
        else:
            if val not in registers:
                registers[val] = 0
            val = registers[val]
    else:
        val = None

    # make sure the register exists and get its value
    if reg.isnumeric() or reg[0] == '-':
        r = int(reg)
    else:
        if reg not in registers:
            registers[reg] = 0
        r = registers[reg]
    
    # execute the command
    if cmd == 'set': 
        registers[reg] = val
        ptr += 1
    elif cmd == 'mul':
        registers[reg] *= val
        ptr += 1
        mult_count += 1
    elif cmd == 'jgz':
        if reg.isnumeric():
            x = int(reg)
        else:
            x = registers[reg]
        if x > 0:
            ptr += val
        else:
            ptr += 1
    elif cmd == 'jnz':
        if reg.isnumeric():
            x = int(reg)
        else:
            x = registers[reg]
        if x != 0:
            ptr += val
        else:
            ptr += 1
    elif cmd == 'add':
        registers[reg] += val
        ptr += 1
    elif cmd == 'sub':
        registers[reg] -= val
        ptr += 1
    elif cmd == 'mod':
        registers[reg] = registers[reg] % val
        ptr += 1
    elif cmd == 'snd':
        snd = r
        ptr += 1
    elif cmd == 'rcv':
        if q:
            registers[reg] = q.popleft()
            ptr += 1
        else:
            wt = True


    return registers,q,ptr,snd,wt,mult_count

def part1(instructions):    # 3025
    registers = {}

    ptr = 0 
    sound = 0
    recover = 0
    r = 0
    mult_count = 0

    while ptr > -1 and ptr < len(instructions):
        instr = instructions[ptr].split(' ')
        cmd,reg = instr[0],instr[1]
        
        # execute the command
        registers,_,ptr,_,_,mc = execute(registers,0,ptr)
        mult_count += mc

    return mult_count


def part2(instructions):    # 915
    # I don't understand completely why this works.
    # This solution is from @ghlmtz
    # See the reddit megathread (https://www.reddit.com/r/adventofcode/comments/7lms6p/2017_day_23_solutions/)
    h = 0
    for x in range(105700,122700 + 1,17):
        for i in range(2,x):
            if x % i == 0:
                h += 1
                break
    return h


    # for some reason, the following code appears to enter an endless loop
    # registers = {'a':1}

    # ptr = 0 
    # sound = 0
    # recover = 0
    # r = 0
    # mult_count = 0

    # while ptr > -1 and ptr < len(instructions):
    #     instr = instructions[ptr].split(' ')
    #     cmd,reg = instr[0],instr[1]
        
    #     # execute the command
    #     registers,_,ptr,_,_,mc = execute(registers,0,ptr)
    #     mult_count += mc

    # return registers['h']



if __name__ == "__main__":
    timestart = time.time()

    data = parse()

    print("part 1:",part1(data))
    print("part 2:",part2(data))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))