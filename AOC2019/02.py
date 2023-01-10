# AOC 2019 - Day 2
# tags: 

import time

IN_File = "AOC2019/02.txt"

def parse():
    with open(IN_File) as f:
        out = f.read().split(',')
    
    prgm = list(map(int,out))
    return prgm


def intcode(noun,verb,prgm):
    ptr = 0
    instr = 0

    prgm[1] = noun
    prgm[2] = verb

    while True:
        instr = prgm[ptr]

        if instr == 1:      # add
            a,b,d = prgm[ptr+1],prgm[ptr+2],prgm[ptr+3]
            prgm[d] = prgm[a] + prgm[b]
            ptr += 4
        
        elif instr == 2:    # mult
            a,b,d = prgm[ptr+1],prgm[ptr+2],prgm[ptr+3]
            prgm[d] = prgm[a] * prgm[b]
            ptr += 4

        elif instr == 99:   # end
            break

        else:               # invalid instruction
            break
    
    return prgm[0]



def part1(data):    # 3790645
    return intcode(12,2,data)

def part2(data):    # 6577
    target_output = 19690720
    tmp = data[:]

    for a in range(100):
        for b in range(100):
            if intcode(a,b,data) == target_output:
                return (a * 100) + b
            data = tmp[:]
    
    return "no solution found"


if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    data2 = data[:]

    print("part 1:",part1(data))
    print("part 2:",part2(data2))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))