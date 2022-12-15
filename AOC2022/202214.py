# AOC 2022 - Day 14

import time
import implementation as graph

IN_FILE = "AOC2022/202214.txt"
# IN_FILE = "AOC2022/202214.sample.txt"

def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        out = [line for line in f.read().split('\n')]
    
    # for line in out:
    #     coord = [list(map(int,x.split(','))) for x in line.split(' -> ')]

    # convert the input to list of coordinates
    walls = []
    floor = 0
    for idx,line in enumerate(out):
        coords = line.split(' -> ')
        x = [eval('[' + coord + ']') for coord in coords]
        walls.append(x)
    
    # build the walls
    all_walls = []
    for wall in walls:
        for idx in range(len(wall)-1):
            x1,y1 = wall[idx]
            x2,y2 = wall[idx+1]

            x1,x2 = sorted([x1,x2])
            y1,y2 = sorted([y1,y2])
            for x in range(x1,x2+1):
                for y in range(y1,y2+1):
                    all_walls.append(x+y*1j)
                    floor = max(floor,y+1)

    return all_walls,floor

def drop_sand(walls):
    pass


def part1(walls,floor):            # => 592
    """Solve part 1."""
    total_sand = 0
    while True:
        level = 500 + 0j                          # start at 500 + 0j
        while True:
            if level.imag >= floor:
                return total_sand
            elif level + 1j not in walls:         # drop sand straight down
                level += 1j
            elif (level - 1) + 1j not in walls:   # drop sand down/left
                level = (level - 1) + 1j
            elif (level + 1) + 1j not in walls:   # drop sand down/right
                level = (level + 1) + 1j
            else:                                 # can't drop. Make it a "wall"
                walls.append(level)
                total_sand += 1
                break


def part2(walls,floor):            # => 30367
    """Solve part 2."""
    total_sand = 0
    
    while (500 + 0j) not in walls:
        level = 500 + 0j                          # start at 500 + 0j
        while True:
            if level.imag >= floor:
                walls.append(level)
                total_sand += 1
                break
            elif level + 1j not in walls:         # drop sand straight down
                level += 1j
            elif (level - 1) + 1j not in walls:   # drop sand down/left
                level = (level - 1) + 1j
            elif (level + 1) + 1j not in walls:   # drop sand down/right
                level = (level + 1) + 1j
            else:                                 # can't drop. Make it a "wall"
                walls.append(level)
                total_sand += 1
                break
    return total_sand


if __name__ == "__main__":
    timestart = time.time()

    walls, floor = parse()
    walls2 = walls.copy()
    # print(puzzle_input)

    print("part 1:",part1(walls,floor))
    print("part 2:",part2(walls2,floor))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))