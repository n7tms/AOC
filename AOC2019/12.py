""" Advent of Code 2019, day 12

    AOC puzzle, 2019, day 12 -- The N-Body Problem
"""
import logging
import getaoc as ga
import intcode_c as ic

def get_input():
    """Using the get_input from my getaoc module, read the input from the web
    for the current year and day.
    This particular input parses the input, splits it on the commas, and
    converts it to integers. It then returns a list of ints."""
    data = ga.get_input(12,2019).splitlines()
    data = [int(line) for line in data[0].split(',')]
    return data


def part1(program):
    """"""

def part2(program):
    """"""


def main():
    """solve each part and print the solutions"""

    # Instantiate the logger
    # log_level = logging.DEBUG
    # log_level = logging.INFO
    log_level = logging.WARNING
    log_format = '%(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=log_level, format=log_format)

    program1 = get_input()
    program2 = get_input()

    part1(program1)
    part2(program2)


if __name__ == "__main__":
    main()
