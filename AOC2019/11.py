"""Advent of Code 2019, day 11

AOC puzzle, 2019, day 11 -- Paint Robot
"""

import getaoc as ga
import intcode_c as ic

def get_input():
    """Using the get_input from my getaoc module, read the input from the web
    for the current year and day.
    This particular input parses the input, splits it on the commas, and
    converts it to integers. It then returns a list of ints."""
    data = ga.get_input(11,2019).splitlines()
    data = [int(line) for line in data[0].split(',')]
    return data



def part1(program):
    """Solve part 1"""
    code = ic.Intcode('Paint Robot',program,[1])
    print(code.run())

    return None



def part2() -> None:
    """Solve part 2"""
    ...

def main():
    """solve each part and print the solutions"""
    program = get_input()
    part1(program)
    part2()

if __name__ == "__main__":
    main()
