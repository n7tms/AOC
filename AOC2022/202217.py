# AOC 2022 - Day 17

import time

IN_FILE = "AOC2022\\inputs\\202217.txt"
# IN_FILE = "AOC2022\\inputs\\202216.sample.txt"
sample = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"


def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        out = f.read()
    return out

# jet = parse()
jet = sample

rocks = [[(3,0),(4,0),(5,0),(6,0)],
[(4,0),(3,1),(4,1),(5,1),(4,2)],
[(5,0),(5,1),(3,2),(4,2),(5,2)],
[(3,0),(3,1),(3,2),(3,3)],
[(3,0),(4,0),(3,1),(4,2)]]

cave = {(0,4),(0,3),(0,2),(0,1),(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(8,1),(8,2),(8,3),(8,4)}


def part1():            # => 
    """Solve part 1."""
    ch = 1 # cave height
    next_jet = -1
    falling_rock = {(0,1)}
    for fr in range(2022+1):
        # increase cave height
        tr = max(falling_rock)[1]   # top rock
        ch = tr + 4           # cave height

        # put cave walls in "cave"
        new_walls = {(0,ch),(0,ch-1),(0,ch-2),(8,ch),(8,ch-1),(8,ch-2)}
        cave.update(new_walls)

        # place next rock at top of cave
        rock = rocks[fr%5]
        falling_rock = set(())
        for point in rock:
            x,y = point
            falling_rock.add((x,ch+y))

        while True: # keep dropping until we hit something
            # push the rock with next jet
            next_jet += 1
            if next_jet >= len(jet):
                next_jet = 0
            nj = jet[next_jet]
            if nj == '<':
                dir = -1
            else:
                dir = 1
            pfr = set(())
            for point in falling_rock:
                x,y = point
                pfr.add((x+dir,y))
            if pfr.isdisjoint(cave):
                falling_rock = pfr.copy()

            # drop the rock
            pfr = set(())
            for point in falling_rock:
                x,y = point
                pfr.add((x,y-1))
            if pfr.isdisjoint(cave):
                falling_rock = pfr.copy()
            else:
                cave.update(falling_rock)
                break
    return max(falling_rock)


def part2(data):            # => 
    """Solve part 2."""

if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    # print(data)

    print("part 1:",part1())
    print("part 2:",part2(data))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))