# AOC 2017 - Day 18
# tags: 

import time

IN_File = "AOC2017/18.txt"

registers = {}

def parse():
    with open(IN_File) as f:
        out = f.read().split('\n')
    return out
    

def part1(data):    #
    ptr = 0 
    sound = 0
    receive = 0

    while ptr > -1 and ptr < len(data):
        instr = data[ptr].split(' ')
        cmd,reg = instr[0],instr[1]
        if len(instr) > 2:
            val = instr[2]
        else:
            val = None

        # make sure the register exists
        if reg not in registers:
            registers[reg] = 0
        
        if val:
            # if val is not a literal, get its value
            if  val.isnumeric() or val[0] == '-':
                val = int(val)
            else:
                if val not in registers:
                    registers[val] = 0
                val = registers[val]
        
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
            sound = val
        elif cmd == 'rcv':
            if registers[reg] > 0: receive = sound

        ptr += 1
    return receive


def part2():    # 
    pass

if __name__ == "__main__":
    timestart = time.time()

    data = parse()

    print("part 1:",part1(data))
    print("part 2:",part2(data))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))