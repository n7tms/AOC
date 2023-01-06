# AOC 2017 - Day 16
# tags: #large #memoize #repeating

import time

IN_File = "AOC2017/16.txt"
prgms = 'abcdefghijklmnop'

billion = 1000000000

def parse():
    with open(IN_File) as f:
        out = f.read().split('\n')
    
    moves = out[0].strip().split(',')
    return moves

def part1(moves,prgms):    # namdgkbhifpceloj
    for cmd in moves:
        if cmd[0] == 's':
            mag = int(cmd[1:])
            prgms = prgms[-mag:] + prgms[:-mag]
        elif cmd[0] == 'x':
            s,e = list(map(int,cmd[1:].split('/')))
            tmps = prgms[s]
            tmpe = prgms[e]
            prgms = prgms.replace(prgms[s],'X')
            prgms = prgms.replace(prgms[e],'Y')
            prgms = prgms.replace('X',tmpe)
            prgms = prgms.replace('Y',tmps)
        elif cmd[0] == 'p':
            s,e = cmd[1:].split('/')
            tmps = s
            tmpe = e
            prgms = prgms.replace(s,'X')
            prgms = prgms.replace(e,'Y')
            prgms = prgms.replace('X',tmpe)
            prgms = prgms.replace('Y',tmps)

    return prgms

def part2(moves,prgms):    # 
    history = ['abcdefghijklmnop']
    for i in range(billion):
        prgms = part1(moves,prgms)
        if prgms in history:
            break   # quit if we start to see a duplicate
        else:
            history.append(prgms)

    index = billion % (i + 2)
    return history[index-1]


if __name__ == "__main__":
    timestart = time.time()

    data = parse()

    prgms = part1(data,prgms)
    print("part 1:",prgms)
    print("part 2:",part2(data,prgms))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))