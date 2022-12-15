# AOC 2022 - Day 2

import pathlib
import sys
import time


IN_FILE = "AOC2022\\inputs\\202202.txt"
# IN_FILE = "AOC2022\\inputs\\202202.sample.txt"

def parse(puzzle_input):
    """Parse input."""
    pi = [line for line in puzzle_input.split("\n")]
    pi2 = [round.split(" ") for round in pi]

    return pi2
#    return [line for line in puzzle_input.split("\n\n")]
    # with open("2202.sample.txt") as f:
    #     out = [(line) for line in f.read().split('\n\n')]
    # return out

         

def part1(data):            # => 12679
    """Solve part 1."""
    score = 0
    e = 0
    t = 0
    for elf,todd in data:
        if elf == "A":
           e = 1
        if elf == "B":
           e = 2
        if elf == "C":
           e = 3
        if todd == "X":
            t = 1
        if todd == "Y":
            t = 2
        if todd == "Z":
            t = 3
        if e == t:
            score += t + 3
        elif (e == 1 and t == 2) or (e == 2 and t == 3) or (e == 3 and t == 1):
            score += t + 6
        else:
            score += t + 0
        # print(elf,todd,e,t,score)
            
    return score
        

def part2(data):            # => 14470
    """Solve part 2."""
    score = 0
    for elf,todd in data:
        if elf == "A":
           e = 1
        if elf == "B":
           e = 2
        if elf == "C":
           e = 3
        if todd == "Y":
            score += e + 3
        if todd == "X":
            if e == 1:
                score += 3
            elif e == 2:
                score += 1
            else:
                score += 2
        if todd == "Z":
            if e == 1:
                score += 2 + 6
            elif e == 2:
                score += 3 + 6
            else:
                score += 1 + 6
    return score



def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    #print(data)
    solution1 = "part 1: " + str(part1(data))
    solution2 = "part 2: " + str(part2(data))

    return solution1, solution2

if __name__ == "__main__":
    timestart = time.time()
    pth = list()
    if len(sys.argv[1:]) == 0:
        pth.append(IN_FILE)
    else:
        pth = sys.argv[1:]

    for path in pth:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
        
    timeend = time.time()
    print("Execution time: ", timeend-timestart)
