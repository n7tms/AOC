# AOC 2017 - Day 13
# tags: 

import time

IN_File = "AOC2017/13.z.txt"

class Level:
    def __init__(self, name, depth):
        self.name = name
        self.depth = depth
        self.cur_pos = 0
        self.dir = 1
    
    def advance(self):
        if self.cur_pos == 0:
            self.dir = 1
        elif self.cur_pos == (self.depth - 1):
            self.dir = -1
        self.cur_pos += self.dir


firewall = {}

def parse():
    with open(IN_File) as f:
        out = f.read().split('\n')
    
    for line in out:
        layer,depth = line.strip().split(':')
        firewall[int(layer)] = Level(int(layer), int(depth))
    
    return


def part1():    # 2604
    maxlevel = max(firewall)
    caught = 0
    packet_pos = 0

    for l in range(maxlevel + 1):
        if l in firewall:
            if firewall[l].cur_pos == 0:
                d = firewall[l].depth
                caught += l * d
        for f in firewall:
            firewall[f].advance()

    return caught

def part2():    # 
    # This will take FOREVER. 1000 delay cycles took30 seconds. 
    # I didn't wait for 10000 to finish. 
    # See part2b() below for a reasonable solution.
    for delay in range(10000):
        firewall.clear()
        parse()
        for n in range(delay):
            for f in firewall:
                firewall[f].advance()
        if part1() == 0:
            return delay

    return "caught!"


def part2b():   # 3941460
    # from @PythonJuggler
    data = open(IN_File, "r")
    rows = data.read().strip().split("\n")

    valDict = dict()

    for row in rows:
        rowS = row.split(" ")
        valDict[int(rowS[0][:-1])] = int(rowS[-1])

    caught = False
    for delay in range(10, 10**7):
        caught = False
        for i in valDict.keys():
            # The total distance the scanner has to travel (down and back up) is 
            # twice the depth - 2
            if (i+delay) % (2* valDict[i] - 2) == 0:
                caught = True
                break
        if not caught:
            return delay


if __name__ == "__main__":
    timestart = time.time()

    parse()

    print("part 1:",part1())
    print("part 2:",part2b())

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))