# sample.py
# testing on aoc template structure
# https://realpython.com/python-advent-of-code/

import pathlib
import sys
import parse as p


# for pattern matching and/or string parsing
def match():
    PATTERN = p.compile("{outer_color} bags contain {num:d} {inner_color} bags.")
    m = PATTERN.search("shiny gold bags contain 2 dark red bags.")
    print(m.named)

# for reading a file containing a list of numbers
# this will have to be slightly different if numbers are comma separated
def parse(puzzle_input):
    """Parse input."""
    return [int(line) for line in puzzle_input.split()]

def part1(data):
    """Solve part 1."""
    for num1 in data:
        for num2 in data:
            if num1 < num2 and num1 + num2 == 2020:
                return num1 * num2

def part2(data):
    """Solve part 2."""
    return 3

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    match()
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
        