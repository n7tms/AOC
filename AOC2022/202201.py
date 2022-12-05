# AOC 2022 - Day 1

import pathlib
import sys

IN_FILE = "d:\\Dev\AOC2022\\202201.txt"
#IN_FILE = "d:\\Dev\AOC2022\\202201.sample.txt"

def parse(puzzle_input):
    """Parse input."""
#    return [int(line) for line in puzzle_input.split("\n\n")]
#    return [line for line in puzzle_input.split("\n\n")]
    with open(IN_FILE) as fp:
        tmp = 0
        out = []
        line = fp.readline()
        while line:
            if line == '\n':
                out.append(tmp)
                tmp = 0
            else:
                tmp += int(line)
            line = fp.readline()
        out.append(tmp)
    return out

           

def part1(data):            # => 70369
    """Solve part 1."""
    return max(data)

def part2(data):            # => 203002
    """Solve part 2."""
    data.sort()
    return sum(data[-3:])










def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    #print(data)
    solution1 = "part 1: " + str(part1(data))
    solution2 = "part 2: " + str(part2(data))

    return solution1, solution2

if __name__ == "__main__":
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
        