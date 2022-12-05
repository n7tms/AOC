# 201901.py
# sample 

import pathlib
import sys


# for reading a file containing a list of numbers
# this will have to be slightly different if numbers are comma separated
def parse(puzzle_input):
    """Parse input."""
    return [int(line) for line in puzzle_input.split()]

def part1(data):
    """Solve part 1."""
    # mass = 0
    # for num1 in data:
        # mass += ((num1 // 3) - 2)
    # return mass
    return sum(mass // 3 - 2 for mass in data)


def part2(data):
    """Solve part 2."""

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
        