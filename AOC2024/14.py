# AOC 2024 day 14: 
#


import aoc_utils as aoc
import time
import os
import copy
import re


DAY = '14'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")


aoc.get_input(2024,DAY,False)
with open(IN_FILE) as fp:
    data = fp.read().strip().splitlines()

r = r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)'
robots = [[int(x), int(y), int(vx), int(vy)] for groups in data for x, y, vx, vy in re.findall(r, groups)]

sizex = 101
sizey = 103

def print_robots(rbts,minute):
    print(f'Minute: {minute}')
    for r in range(sizey):
        for c in range(sizex):
            printed = False
            for r1,c1,_,_ in rbts:
                if r==r1 and c==c1:
                    print('#', end='')
                    printed = True
                    break
            if not printed: print(' ', end='')
        print()


# Solution for Part 1 here vvvvvvvvvvvvvvvvvvvvvvvvv     # => 216027840
start_time = time.time()

for m in range(100):
    new_robots = []
    for robot in robots:
        c,r,vc,vr = robot
        c += vc
        if c >= sizex:
            c = 0 + (c - sizex)
        elif c < 0:
            c = sizex + c
        r += vr
        if r >= sizey:
            r = 0 + (r - sizey)
        elif r < 0:
            r = sizey + r
        new_robots.append([c,r,vc,vr])
    robots = copy.deepcopy(new_robots)



# now remove the robots from the middle
midc = sizex // 2
midr = sizey // 2
quad1, quad2, quad3, quad4 = 0,0,0,0
for c,r,_,_ in robots:
    if c == midc or r == midr:
        continue
    if c < midc and r < midr: # quad1
        quad1 += 1
    elif c > midc and r < midr: # quad2
        quad2 += 1
    elif c < midc and r > midr: # quad3
        quad3 += 1
    elif c > midc and r > midr: # quad4
        quad4 += 1


result = quad1 * quad2 * quad3 * quad4
exec_time = time.time() - start_time
print(f'Part 1: {result} ({exec_time:.3f} sec)')



# Solution for Part 2 here vvvvvvvvvvvvvvvvvvvvvvvvv    # => 6876
# Part 2 was a very manual process for me. I essentially watched every set of robots
# scroll by until I FINALLY saw the Christmas tree!!
start_time = time.time()

for m2 in range(m+2,6877):
    new_robots = []
    for robot in robots:
        c,r,vc,vr = robot
        c += vc
        if c >= sizex:
            c = 0 + (c - sizex)
        elif c < 0:
            c = sizex + c
        r += vr
        if r >= sizey:
            r = 0 + (r - sizey)
        elif r < 0:
            r = sizey + r
        new_robots.append([c,r,vc,vr])
    robots = copy.deepcopy(new_robots)

    if m2==6876: 
        print_robots(robots, m2)


exec_time = time.time() - start_time
print(f'Part 2: {m2} ({exec_time:.3f} sec)')



