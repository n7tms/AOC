# AOC 2022 - Day 19

import time

IN_FILE = "AOC2022\\inputs\\202219.txt"
# IN_FILE = "AOC2022\\inputs\\202219.sample.txt"


def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        out = f.read().split('\n')
    
    blueprints = []
    for line in out:
        bp = line.split(' ')
        bpid = bp[1].split(':')[0]
        orc,crc,orco,orcc,grcor,grcob = bp[6], bp[12], bp[18], bp[21], bp[27], bp[30]
        blueprints.append([bpid,orc,crc,orco,orcc,grcor,grcob])
    return blueprints






def part1(data):            # => 
    """Solve part 1."""

            
    



def part2(data):            # => 
    """Solve part 2."""

if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    # print(data)

    print("part 1:",part1(data))
    print("part 2:",part2(data))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))