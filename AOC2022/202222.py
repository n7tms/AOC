# AOC 2022 - Day 22

import time
import re

IN_FILE = "AOC2022/inputs/202222.txt"
# IN_FILE = "AOC2022/inputs/202222.sample.txt"


def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        m,d = f.read().split('\n\n')
    
    # build the map
    maps = []
    max_len = 0
    for line in m.split('\n'):
        tmp = list(c for c in line)
        max_len = max([max_len,len(tmp)])
        maps.append(tmp)
    
    # append spaces in short rows
    for x in range(len(maps)):
        if len(maps[x]) < max_len:
            tmp = [' ' * 1 for _ in range(max_len - len(maps[x]))]
            maps[x].extend(tmp)
            
    # print(maps)

    # parse the directions
    dirs = re.findall(r'\d+|[RL]',d)
  
    return maps,dirs


#             R D  L  U
DIRECTIONS = [1,1,-1,-1]

def move(maps,cp,cd,mag):
    xm,ym = cp
    if cd == 0: # right
        maps[ym][xm] = '>'
        while mag > 0:
            if (xm+1 > len(maps[ym])-1) or maps[ym][xm+1] == ' ': # hit the void; wrap
                if maps[ym].index('.') < maps[ym].index('#'):
                    xm = maps[ym].index('.')-1
                else:
                    return maps,[xm,ym]
            elif maps[ym][xm+1] == '#': # hit a wall
                return maps,[xm,ym]
            mag -= 1
            xm += 1
            maps[ym][xm] = '>'

    elif cd == 2: # left
        maps[ym][xm] = '<'
        while mag > 0:
            if (xm-1 < 0) or maps[ym][xm-1] == ' ': # hit the void; wrap
                tmp_map = maps[ym]
                tmp_map.reverse()
                if tmp_map.index('.') < tmp_map.index('#'):
                    xm = len(tmp_map) - tmp_map.index('.') - 1
                else:
                    return maps,[xm,ym]
            elif maps[ym][xm-1] == '#': # hit a wall
                return maps,[xm,ym]
            mag -= 1
            xm -= 1
            maps[ym][xm] = '<'

    elif cd == 1: # down
        maps[ym][xm] = 'v'
        while mag > 0:
            if (ym+1 > len(maps)-1) or maps[ym+1][xm] == ' ': # hit the void; wrap
                for yw in range(len(maps)-1):
                    if maps[yw][xm] == ' ':
                        continue
                    elif maps[yw][xm] == '#':
                        maps[ym][xm] = 'v' 
                        return maps, [xm,ym]
                    ym = yw - 1
                    break
            elif maps[ym+1][xm] == '#': # hit a wall
                return maps, [xm,ym]
            mag -= 1
            ym += 1
            maps[ym][xm] = 'v' 

    else: # up
        maps[ym][xm] = '^'
        while mag > 0:
            if (ym-1 < 0) or maps[ym-1][xm] == ' ': # hit the void; wrap
                for yw in range(len(maps)-1,-1,-1):
                    if maps[yw][xm] == ' ':
                        continue
                    elif maps[yw][xm] == '#':
                        ym = yw
                        maps[ym][xm] = 'v' 
                        return maps,[xm,ym]
                    ym = yw + 1
                    break
            elif maps[ym-1][xm] == '#': # hit a wall
                return maps,[xm,ym]
            mag -= 1
            ym -= 1
            maps[ym][xm] = '^' 
    return maps,[xm,ym]

            



def part1(maps,dirs):            # => 
    cp = (maps[0].index('.'),0)  # current position
    cd = 0                       # current direction (R)

    for cmd in dirs:
        if cmd.isnumeric(): # move
            maps,cp = move(maps,cp,cd,int(cmd))
        else: # turn
            if cmd == 'R':
                cd = (cd + 1) % 4
            else:
                cd = (cd - 1) % 4
    password = ((cp[1] + 1) * 1000) + ((cp[0] + 1) * 4) + cd
    return password        

def part2(data):            # => 
    pass

if __name__ == "__main__":
    timestart = time.time()

    maps,dirs = parse()
    # print(data)

    print("part 1:",part1(maps,dirs))
    # print("part 2:",part2(data))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))