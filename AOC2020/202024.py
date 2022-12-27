# AOC 2020 - Day 24

import time
import collections
import math

# IN_FILE = "AOC2020\\202024.txt"
IN_FILE = "AOC2020\\202024.sample.txt"

_Hex = collections.namedtuple("Hex", ["q", "r", "s"])
def Hex(q, r, s):
    assert not (round(q + r + s) != 0), "q + r + s must be 0"
    return _Hex(q, r, s)

hex_directions = [Hex(1, 0, -1), Hex(1, -1, 0), Hex(0, -1, 1), Hex(-1, 0, 1), Hex(-1, 1, 0), Hex(0, 1, -1)]
def hex_direction(direction):
    return hex_directions[direction]

def hex_add(a, b):
    return Hex(a.q + b.q, a.r + b.r, a.s + b.s)

def hex_neighbor(hex, direction):
    return hex_add(hex, hex_direction(direction))

# directions
# r: e +1, w -1
# q: se +1, nw -1
# s: sw +1, ne -1

def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        out = f.read().split('\n')
    return out


def fill_in_floor(floor):
    # find min and max r,q,s
    # nr,nq,ns = 0,0,0
    # xr,xq,xs = 0,0,0
    # for t in floor:
    #     r,q,s = t[0]
    #     nr = min([r,nr])
    #     nq = min([q,nq])
    #     ns = min([s,ns])
    #     xr = max([r,xr])
    #     xq = max([q,xq])
    #     xs = max([s,xs])
    # mint = [nr,nq,ns]
    # maxt = [xr,xq,xs]
    
    # nr,nq,ns = [x-1 for x in mint]
    # xr,xq,xs = [x+1 for x in maxt]

    nr,nq,ns = -1000,-1000,-1000
    xr,xq,xs = 1000,1000,1000

    working = floor.copy()

    for r in range(nr,xr+1):
        for q in range(nq,xq+1):
            for s in range(ns,xs+1):
                if [[r,q,s],0] not in floor and [[r,q,s],1] not in floor:
                    working.append([[r,q,s],0])
    return working


def initial_flip(data):
    # create home tile (0,0,0)
    floor = [[[0,0,0],0]]
    for line in data:
        r,q,s = 0,0,0
        i = 0
        while i < len(line):
            if line[i] == 'e':
                q += 1
                s -= 1
            elif line[i] == 'w':
                q -= 1
                s += 1
            elif line[i] == 's':
                i += 1
                if line[i] == 'e':
                    r += 1
                    s -= 1
                elif line[i] == 'w':
                    q -= 1
                    r += 1
            elif line[i] == 'n':
                i += 1
                if line[i] == 'e':
                    q += 1
                    r -= 1
                elif line[i] == 'w':
                    r -= 1
                    s += 1
            i += 1

        if [[r,q,s],0] in floor:
            floor.remove([[r,q,s],0])
            floor.append([[r,q,s],1])
        elif [[r,q,s],1] in floor:
            floor.remove([[r,q,s],1])
            floor.append([[r,q,s],0])
        else:
            floor.append([[r,q,s],1])



    return floor

def get_neighbors(tile,floor):
    r,q,s = tile[0]
    qty = 0
    if [[r,q+1,s-1],1] in floor: # e
        qty += 1
    if [[r+1,q,s-1],1] in floor: # se
        qty += 1
    if [[r+1,q-1,s],1] in floor: # sw
        qty += 1
    if [[r,q-1,s+1],1] in floor: # w
        qty += 1
    if [[r-1,q,s+1],1] in floor: # nw
        qty += 1
    if [[r-1,q+1,s],1] in floor: # ne
        qty += 1
    return qty

def count_blacks(floor):
    # count black (1)
    blacks = 0
    for x in floor:
        blacks += x[1]
    return blacks

def part1(data):        # => 339
    floor = initial_flip(data)
    return count_blacks(floor)

def part2(data,days):        # => 
    floor = initial_flip(data)
    floor = fill_in_floor(floor)

    for d in range(days):
        working = floor.copy()
        for tile in floor:
            qty = get_neighbors(tile,floor)
            if tile[1] == 1: # a black tile
                # how many black neighbors? (0 or >2)
                if qty == 0 or qty > 2:
                    working.remove(tile)
                    working.append([tile[0],0])
            else: # must be a white tile
                # how many black neighbors? (2)
                if qty == 2:
                    working.remove(tile)
                    working.append([tile[0],1])
        floor = working.copy()
    
    return count_blacks(floor)

    

if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    # print(data)

    print("part 1:",part1(data))
    print("part 2:",part2(data,10))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))