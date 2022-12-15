# AOC 2022 - Day 10

import time

# IN_FILE = "AOC2022\\inputs\\202210.txt"
IN_FILE = "AOC2022\\inputs\\202210.sample.txt"


def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        # return [[int(c) for c in line.strip()] for line in f]     # integers
        # return [(line.strip()) for line in f.read().split('\n')]    # strings
        # return [([dir,mag] for dir,mag in line.split()) for line in f.read().split('\n')]
        out = [line for line in f.read().split('\n')]
    return [line.split() for line in out]


def part1(data):            # => 12460
    """Solve part 1."""
    cycle = 1
    instridx = 0
    regval = 1
    strength = 0
    inadd = False
    crt = ""

    while True:
        if instridx >= len(data) or cycle > 220:
            break

        instr = data[instridx]

        if regval == cycle - 1 or regval == cycle or regval == cycle +1:
            crt += '#'
        else:
            crt += '.'


        if cycle == 20 or (cycle > 59 and (cycle - 20) % 40 == 0):
            strength += cycle * regval
            # print(cycle,strength)
        if inadd:
            inadd = False
            regval += int(instr[1])
            instridx += 1
        elif instr[0] == 'noop':
            instridx += 1
        else:
            if instr[0] == 'addx':
                inadd = True

        cycle += 1


    return strength,crt

def part2(data):            # => EZFPRAKL
    """Solve part 2."""


if __name__ == "__main__":
    timestart = time.time()
    tm = [[0] * 600] * 600  # initialize tail map

    puzzle_input = parse()
    # print(puzzle_input)

    part1_solution,crt = part1(puzzle_input)
    print("part 1:",part1_solution)
    # print("part 2:",part2(puzzle_input))
    print("part 2:")
    for i in range(6):
        print(crt[i:i+40])
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))

