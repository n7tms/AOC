# AOC 2024 day 15: 
#

import aoc_utils as aoc
import time
import os

DAY = '15'
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().split('\n\n')
    
    walls = set()
    robots = set()
    map = []
    for r, line in enumerate(data[0].splitlines()):
        row = []
        for c, ch in enumerate(line):
            if ch == '#': walls.add((r,c))
            if ch == 'O': robots.add((r,c))
            if ch == '@': start = (r,c)
            row.append(ch)
        map.append(row)
    
    moves = [ch for ch in data[1] if ch != '\n']

    return map, walls, robots, moves, start

DIRS = {'^':(-1,0), '>':(0,1), 'v':(1,0), '<':(0,-1)}


def part1(map,walls,robots,moves,start):        # => 

    pos = start
    while moves:
        mv = moves.pop(0)
        dir = DIRS[mv]
        nr, nc = pos[0]+dir[0], pos[1]+dir[1]
        if map[nr][nc] == '.':
            pos = (nr,nc)
        elif (nr,nc) in walls:
            pass
        elif (nr,nc) in robots:
            # iterate in the direction. if find a wall, pass. if find a '.', move everything.
            shifts = []
            while True:
                mr += dir[0]
                mc += dir[1]
                if (mr,mc) in walls: break
                shifts.append((mr,mc))
                if map[mr][mc] == '.':
                    for sh in shifts:
                        robots.add(sh)
                    del robots[(nr,nc)]
                    pos = (nr,nc)


                    



    return


def part2(data):       # => 
    return

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    m,w,r,mv,s = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(m,w,r,mv,s))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(data))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        