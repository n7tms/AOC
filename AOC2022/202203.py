# AOC 2022 - Day 3

import pathlib
import sys
import time


IN_FILE = "d:\\Dev\AOC2022\\202203.txt"
# IN_FILE = "d:\\Dev\AOC2022\\202203.sample.txt"

def parse(puzzle_input):
    """Parse input."""
    # pi = [line for line in puzzle_input.split("\n")]
    # pi2 = [round.split(" ") for round in pi]

    # return pi2
#    return [line for line in puzzle_input.split("\n\n")]
    with open(IN_FILE) as f:
        out = [(line) for line in f.read().split('\n')]
    return out
        

def part1(data):            # => 7967
    """Solve part 1."""
    total = 0
    for contents in data:
        size = len(contents) // 2
        comp1 = contents[:size]
        comp2 = contents[size:]
        common = ''.join(sorted(set(comp1) & set(comp2), key = comp1.index))
        print(common)
        if common.isupper():
            total += ord(common) - ord('A') + 27
        else:
            total += ord(common) - ord('a') + 1
    return total


def part2(data):            # => 2716
    """Solve part 2."""
    total = 0
    for idx in range(0,len(data), 3):
        comp1 = data[idx]
        comp2 = data[idx+1]
        comp3 = data[idx+2]
        common = ''.join(sorted(set(comp1) & set(comp2) & set(comp3), key = comp1.index))
        if common.isupper():
            total += ord(common) - ord('A') + 27
        else:
            total += ord(common) - ord('a') + 1
    return total




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
