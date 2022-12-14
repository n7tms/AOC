# AOC 2022 - Day 14

import time
import implementation as graph

IN_FILE = "AOC2022\\202214.txt"
# IN_FILE = "AOC2022\\202214.sample.txt"

def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        # out = [line.split() for line in out]
        # final_out = [[eval(x),eval(y)] for x,y in out]
        # final_out = [[eval(x),eval(y)] for x,y in [line.split() for line in [line for line in f.read().split('\n\n')]]]
        out = [line for line in f.read().split('\n')]

    # convert the input to list of coordinates
    walls = []
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

            #normalize
            x1 -= 450
            x2 -= 450
            if x1 == x2:    # this wall is going up/down
                if y1 > y2: 
                    y1,y2 = y2,y1
                for y in range(y1,y2+1):
                    all_walls.append((x1,y))
            else:           # this wall is going left/right
                if x1 > x2:
                    x1,x2 = x2,x1
                for x in range(x1,x2+1):
                    all_walls.append((x,y1))
    print(all_walls)

        
    # cavern = graph.GridWithWeights(525,150)
    cavern = graph.GridWithWeights(75,150)
    cavern.walls = all_walls
    graph.draw_grid(cavern)

    return graph

def drop_sand(graph):
    pass


def part1(data):            # => 592
    """Solve part 1."""


def part2(data):            # => 30367
    """Solve part 2."""


if __name__ == "__main__":
    timestart = time.time()

    puzzle_input = parse()
    # print(puzzle_input)

    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))