# AOC 2017 - Day 16
# tags: 

import time

IN_File = "AOC2017/16.txt"
prgms = 'abcdefghijklmnop'
# prgms = 'abcde'

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
    # the following block will take forever -- >5000 hours
    # for _ in range(1000000000):
    #     part1(moves,prgms)
    # return prgms

    # so, just follow the pattern:
    # a moves to 1
    # b moves to 6
    # c moves to 11
    # etc. 
    # do those moves 1000000000 times
    new_moves = []
    new_moves.append([0,prgms.index('a')]) # a
    new_moves.append([1,prgms.index('b')]) # b
    new_moves.append([2,prgms.index('c')]) # c
    new_moves.append([3,prgms.index('d')]) # d
    new_moves.append([4,prgms.index('e')]) # e
    new_moves.append([5,prgms.index('f')]) # f
    new_moves.append([6,prgms.index('g')]) # g
    new_moves.append([7,prgms.index('h')]) # h
    new_moves.append([8,prgms.index('i')]) # i
    new_moves.append([9,prgms.index('j')]) # j
    new_moves.append([10,prgms.index('k')]) # k
    new_moves.append([11,prgms.index('l')]) # l
    new_moves.append([12,prgms.index('m')]) # m
    new_moves.append([13,prgms.index('n')]) # n
    new_moves.append([14,prgms.index('o')]) # o
    new_moves.append([15,prgms.index('p')]) # p

    pl = []
    for c in prgms:
        pl.append(c)

    history = []
    for i in range(1000000000):
        tmp = []
        for c in  new_moves:
            tmp.append(pl[c[0]])

        for c in new_moves:
            pl[c[1]] = tmp[c[0]]
        
        if pl not in history:
            history.append([pl])
        else:
            return i,pl
    
    return ''.join(pl)
    


if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    # data = ['s1','x3/4','pe/b']

    prgms = part1(data,prgms)
    print("part 1:",prgms)
    print("part 2:",part2(data,prgms))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))