# AOC 2017 - Day 18
# tags: #program

import time
from collections import deque

IN_File = "AOC2017/18.txt"

def parse():
    with open(IN_File) as f:
        out = f.read().split('\n')
    return out
    

def execute(registers,q,ptr):
    snd = None
    wt = False

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
    elif cmd == 'jgz':
        if reg.isnumeric():
            x = int(reg)
        else:
            x = registers[reg]
        if x > 0:
            ptr += val
        else:
            ptr += 1
    elif cmd == 'add':
        registers[reg] += val
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


    return registers,q,ptr,snd,wt

def part1(instructions):    # 9423
    registers = {}

    ptr = 0 
    sound = 0
    recover = 0
    r = 0

    while ptr > -1 and ptr < len(instructions):
        instr = instructions[ptr].split(' ')
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
        elif cmd == 'mul':
            registers[reg] *= val
        elif cmd == 'jgz':
            if reg.isnumeric():
                x = int(reg)
            else:
                x = registers[reg]
            if x > 0:
                ptr += val
                continue
        elif cmd == 'add':
            registers[reg] += val
        elif cmd == 'mod':
            registers[reg] = registers[reg] % val
        elif cmd == 'snd':
            sound = r
        elif cmd == 'rcv':
            if registers[reg] > 0: 
                recover = sound
                return recover

        ptr += 1
    return recover


def part2(instructions):    # 7620
    registers0 = {'p': 0}
    registers1 = {'p': 1}
    q0,q1 = deque([]),deque([])
    ptr0, ptr1 = 0,0
    wait0,wait1 = False,False
    p1snd = 0

    while (ptr0 > -1 and ptr0 < len(instructions)) and \
        (ptr1 > -1 and ptr1 < len(instructions)):
        if wait0 and wait1:
            break

        # program 0
        if q0 or not wait0:
            wait0 = False
            registers0,q0,ptr0,snd0,wait0 = execute(registers0,q0,ptr0)
            if snd0 is not None: 
                q1.append(snd0)

        # program 1
        if q1 or not wait1:
            wait1 = False
            registers1,q1,ptr1,snd1,wait1 = execute(registers1,q1,ptr1)
            if snd1 is not None: 
                p1snd += 1
                q0.append(snd1)

    return p1snd



if __name__ == "__main__":
    timestart = time.time()

    data = parse()

    print("part 1:",part1(data))
    print("part 2:",part2(data))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))