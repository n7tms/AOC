# AOC 2022 - Day 23

import time

# IN_FILE = "AOC2022\\inputs\\202223.txt"
IN_FILE = "AOC2022\\inputs\\202223.small.txt"
# IN_FILE = "AOC2022\\inputs\\202223.large.txt"

class Elf:
    def __init__(self,location):
        self.x, self.y = location
        self.proposed = [0,0]
        self.move = False

DIRS = ([-1,-1],[0,-1],[1,-1],[-1,0],[0,0],[1,0],[-1,1],[0,1],[1,1])
ROUNDS = ([0,-1],[0,1],[-1,0],[1,0])

def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        out = f.read().split('\n')

    elves = []
    for y in range(len(out)):
        for x in range(len(out[0])):
            if out[y][x] == '#':
                elf = Elf((x,y))
                elves.append(elf)

    return elves

def locate_elf(elves,pos):
    for e in elves:
        if pos == [e.x,e.y]:
            return True
    return False

def considerations(elves,round):
    for e in elves:
        x,y = e.x,e.y
        potentials = list((i+x,j+y) for i,j in DIRS)
        decided = True
        e.proposed = [x,y]
        for d in ROUNDS:
            for p in [potentials[0],potentials[1],potentials[2]]:
                if locate_elf(elves,p):
                    decided = False
            if decided:
                e.proposed = [d[0]+x,d[1]+y]
                break
    return elves



def part1(data):            # => 
    elves = considerations(data,0)
    return 

def part2(data):        # => 
    pass

if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    # print(data)

    print("part 1:",part1(data))
    print("part 2:",part2(data))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))