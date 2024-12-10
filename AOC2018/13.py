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
}


def part1(tracks, carts):        # => 

    while True:
        # Sort the carts by location (left to right, top to bottom)
        sorted_carts = sorted([value['loc'] for value in carts.values()], key=lambda loc: (loc[0],loc[1]))

        for cart in sorted_carts:
            # get the cart information
            for cn, (loc, dir, lastturn) in carts.items():
                if loc == cart:
                    # this is the cart we're looking for. Move it.
                    r,c = loc
                    if tracks[r][c] == '+': #turn
                        new_turn = (carts[cn][lastturn]) + 1 % 3
                        
                        pass
                    else:
                        new_dir = direction_changes.get(tracks[r][c],dir)
                        nr, nc = r+DIRS[new_dir][0], c+DIRS[new_dir][1]
                        carts[cn]['loc'] = (nr, nc)
                        carts[cn]['dir'] = new_dir

                    





    return 


def part2(data):        # => 
    return 


def solve():
    """Solve the puzzle for the given input."""
    t,c = parse()

    start_time = time.time()
    p1 = str(part2(t,c))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(t,c))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve()

