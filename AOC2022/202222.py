# AOC 2022 - Day 22

import time
import re

# IN_FILE = "AOC2022\\inputs\\202222.txt"
IN_FILE = "AOC2022\\inputs\\202222.sample.txt"


def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        m,d = f.read().split('\n\n')
    
    # build the map
    maps = []
    for line in m.split('\n'):
        maps.append(list(c for c in line))
    print(maps)

    # parse the directions
    dirs = re.findall(r'\d+|[RL]',d)
  
    return maps,dirs


#             R D  L  U
DIRECTIONS = [1,1,-1,-1]

def move(maps,cp,cd,mag):
    xm,ym = cp
    if cd == 0: # right
        maps[ym][xm] = '>'
        for x in range(1,mag+1):
            if maps[ym][xm+x] == '#': # hit a wall
                return maps,[x-1,ym]
            elif maps[ym][xm+x] == ' ': # hit the void; wrap
                if maps[ym].index('.') < maps[ym].index('#'):
                    xm = maps[ym].index('.')
                else:
                    return maps,[x-1,ym]
            maps[ym][xm] = '>'

    elif cd == 1: # down
        maps[ym][xm] == 'v'
        for y in range(1,mag+1):
            if maps[ym+y][xm] == '#': # hit a wall
                return maps, [xm,y-1]
            elif maps[ym+y][xm] == ' ': # hit the void; wrap
                for yw in range(len(maps)-1):
                    if maps[yw][xm] == ' ':
                        continue
                    elif maps[yw][xm] == '#':
                        maps[y-1][xm] = 'v' 
                        return maps, [xm,y-1]
            maps[y][xm] = 'v' 

    if cd == 2: # left
        maps[ym][xm] = '<'
        for x in range(1,mag+1):
            if maps[ym][xm-x] == '#': # hit a wall
                return maps,[x+1,ym]
            elif maps[ym][xm-x] == ' ': # hit the void; wrap
                for xw in range(len(maps[ym])-1,0,-1):
                    if maps[ym][xw] == '#':
                        maps[ym][x+1] = '<'
                        return maps,[x+1,ym]
                    elif maps[ym][xw] == ' ':
                        continue
                    maps[ym][xw] = '<'
                    # ????????????????????
                    # if I wrap and hit another '.', it breaks the for
                    # i need to keep track of the location independent of the for
                if maps[ym].index('.') < maps[ym].index('#'):
                    xm = maps[ym].index('.')
                else:
                    return maps,[x+1,ym]
            maps[ym][xm] = '>'
            



def part1(maps,dirs):            # => 
    cp = (maps[0].index('.'),0)  # current position
    cd = 0                       # current direction (R)

    for cmd in dirs:
        if isinstance(cmd,int): # move
            maps,cp = move(maps,cp,cd,int(cmd))
        else: # turn
            pass

    return 1        

def part2(data):            # => 
    pass

if __name__ == "__main__":
    timestart = time.time()

    maps,dirs = parse()
    # print(data)

    print("part 1:",part1(maps,dirs))
    print("part 2:",part2(data))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))