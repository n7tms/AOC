# AOC 2022 - Day 9

import time

# IN_FILE = "AOC2022\\202209.txt"
IN_FILE = "AOC2022\\202209.sample.txt"


def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        # return [[int(c) for c in line.strip()] for line in f]     # integers
        # return [(line.strip()) for line in f.read().split('\n')]    # strings
        # return [([dir,mag] for dir,mag in line.split()) for line in f.read().split('\n')]
        return [line for line in f.read().split('\n')]

def move_tail(t,h,tm):
    tx,ty = t
    hx,hy = h

    # see if we even need to move
    if abs((tx-hx) * (ty-hy)) < 2:
        return tm

    # different column
    if tx != hx and ty != hy:
        if tx < hx and ty < hy:
            tx += 1
            ty += 1
        elif tx < hx and ty > hy:
            tx += 1
            ty -= 1
        elif tx > hx and ty < hy:
            tx -= 1
            ty += 1
        else:
            tx -= 1
            ty -= 1
    # we moved diagnol; mark it
    tm[tx][ty] = 1

    if tx == hx and ty < hy:
        for i in range(ty,hy-ty):
            ty += 1    


        
    return tm

def part1(data, tm):            # => 
    """Solve part 1."""
    hx,hy = 300,300
    tx,ty = 300,300
    tm[300][300] = 1

    for cmd in data:
        dir,mag = cmd.split()
        if dir == 'R':
            tx += mag
            tm = move_tail([tx,ty],[hx,hy],tm)
        if dir == 'D':
            ty += mag
            tm = move_tail([tx,ty],[hx,hy],tm)
        if dir == 'L':
            tx -= mag
            tm = move_tail([tx,ty],[hx,hy],tm)
        if dir == 'U':
            ty -= mag
            tm = move_tail([tx,ty],[hx,hy],tm)

    total_visits = 0
    for x in tm:
        total_visits += sum(x)
    return total_visits


def part2(data):            # => 
    """Solve part 2."""

if __name__ == "__main__":
    timestart = time.time()
    tm = [[0] * 600] * 600  # initialize tail map

    puzzle_input = parse()
    print(puzzle_input)

    print("part 1:",part1(puzzle_input, tm))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))

