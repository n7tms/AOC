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

jet = parse()
# jet = sample

rocks = [[(3,0),(4,0),(5,0),(6,0)], # _
[(4,0),(3,1),(4,1),(5,1),(4,2)],    # +
[(3,0),(4,0),(5,0),(5,1),(5,2)],    # L (reversed)
[(3,0),(3,1),(3,2),(3,3)],          # |
[(3,0),(4,0),(3,1),(4,1)]]          # o

cave = {(0,4),(0,3),(0,2),(0,1),(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(8,1),(8,2),(8,3),(8,4)}


def part1():            # => 3065
    """Solve part 1."""
    ch = 1 # cave height
    next_jet = -1
    falling_rock = {(0,0)}
    tr = 0  # top of top rock
    for fr in range(2022):
        # increase cave height ======================
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
        print("new rck:",sorted(falling_rock))

        while True: # keep dropping until we hit something
            # print("falling:",sorted(falling_rock))
            # push the rock with next jet
            next_jet = (next_jet + 1) % len(jet)
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
            print("shifted:",sorted(falling_rock), nj)

            # drop the rock
            pfr = set(())
            for point in falling_rock:
                x,y = point
                pfr.add((x,y-1))
            if pfr.isdisjoint(cave):
                falling_rock = pfr.copy()
                print("falling:",sorted(falling_rock))
            else:
                cave.update(falling_rock)
                # find the max height of the last fallen rock
                for point in falling_rock:
                    tr = point[1] if point[1]>tr else tr
                print("fallen",sorted(falling_rock),fr,tr)
                break
    return tr


def part2(data):            # => 1562536022966
    """Solve part 2."""

if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    # print(data)

    print("part 1:",part1())
    print("part 2:",part2(data))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))