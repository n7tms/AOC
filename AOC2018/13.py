# AOC 2018 day 13: 
#

import aoc_utils as aoc
import time
import os


DAY = '13'
IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".sample.txt")

def parse():
    """
    Parse
    """
    aoc.get_input(2018,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()
    
    tracks = []
    carts = {}
    cartnum = 0
    for r,line in enumerate(data):
        track = []
        for c,ch in enumerate(line):
            if ch == '<': direction = 0
            if ch == '>': direction = 2
            if ch == '^': direction = 1
            if ch == 'v': direction = 3
            if ch in ['<','>']:
                # make the last turn direction "right", so the next (first) turn direction is "left"
                carts[cartnum] = {'loc':(r,c), 'dir':direction, 'last':2}
                track.append('-')
                cartnum += 1
            elif ch in ['^','v']:
                carts[cartnum] = {'loc':(r,c), 'dir':direction, 'last':2}
                track.append('|')
                cartnum += 1
            else:
                track.append(ch)
        tracks.append(track)
    
    return tracks, carts

TURNS = [-1,0,1]        # left, straight, right
DIRS = [(0,-1),(-1,0),(0,1),(1,0)]  # left, up, right, down
direction_changes = {
    ('/', 1): 2,  # Right
    ('/', 3): 0,  # Left
    ('/', 0): 3,  # Down
    ('/', 2): 1,  # Up
    ('\\', 2): 3,  # Down
    ('\\', 3): 1,  # Right
    ('\\', 0): 1,  # Up
    ('\\', 1): 0,  # Left
    ('-', 0): 0,  # keep left
    ('-', 2): 2,  # keep right
    ('|', 1): 1,  # keep Up
    ('|', 3): 3,  # keep down
    ('+', 0): 0,
    ('+', 1): 1,
    ('+', 2): 2,
    ('+', 3): 3,
}


def part1(tracks, carts):        # => 8,9   (I return (9,8) in (r,c) format; AOC wants (x,y) coords ==> (c,r))

    while True:
        # Sort the carts by location (left to right, top to bottom)
        sorted_carts = sorted([value['loc'] for value in carts.values()], key=lambda loc: (loc[0],loc[1]))

        for cart in sorted_carts:
            # get the cart information
            for cn, values in carts.items():
                loc, dir, last = values['loc'], values['dir'], values['last']
                if loc == cart:
                    # this is the cart we're looking for. Move it.
                    r,c = loc
                    if tracks[r][c] == '+': #turn
                        carts[cn]['last'] = (last + 1) % 3
                        dir = (TURNS[carts[cn]['last']] + dir) % 4
                    new_dir = direction_changes[(tracks[r][c],dir)]
                    nr, nc = r+DIRS[new_dir][0], c+DIRS[new_dir][1]
                    carts[cn]['loc'] = (nr, nc)
                    carts[cn]['dir'] = new_dir
                    break
            # Check for collision
            if [key for key, details in carts.items() if key != cn and details['loc'] == carts[cn]['loc']]:
                # collision!
                return carts[cn]['loc']        


    return 


def part2(tracks, carts):        # => 73,33      
    # this solution does not produce (73,33). Help from Jonathan Poulson
    # my code spits out (71,124), although the example works correctly.
    # not sure what is going on here ???
    while True:
        if len(carts) == 1:
            return carts
        
        # Sort the carts by location (left to right, top to bottom)
        sorted_carts = sorted([value['loc'] for value in carts.values()], key=lambda loc: (loc[0],loc[1]))

        for cart in sorted_carts:
            # get the cart information
            for cn, values in carts.items():
                loc, dir, last = values['loc'], values['dir'], values['last']
                if loc == cart:
                    # this is the cart we're looking for. Move it.
                    r,c = loc
                    if tracks[r][c] == '+': #turn
                        carts[cn]['last'] = (last + 1) % 3
                        dir = (TURNS[carts[cn]['last']] + dir) % 4
                    new_dir = direction_changes[(tracks[r][c],dir)]
                    nr, nc = r+DIRS[new_dir][0], c+DIRS[new_dir][1]
                    carts[cn]['loc'] = (nr, nc)
                    carts[cn]['dir'] = new_dir

                # Check for collision
                    crashed_carts = [key for key, details in carts.items() if key != cn and details['loc'] == carts[cn]['loc']]
                    if crashed_carts:
                        # collision! delete the offending carts
                        del carts[cn]
                        del carts[crashed_carts[0]]
                    break


def solve():
    """Solve the puzzle for the given input."""
    t,c = parse()

    start_time = time.time()
    p1 = str(part1(t,c))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    # start with a fresh set of carts
    t,c = parse()

    start_time = time.time()
    p2 = str(part2(t,c))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve()

