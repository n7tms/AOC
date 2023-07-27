# AOC 2019 Day 10
#
import getaoc as ga
from intcode_c import Intcode


def get_input():
    data = ga.get_input(10,2019).splitlines()

    # --- do other parsing here if necessary ---
    # convert the lines of strings to list of numbers
    # data = [int(line) for line in data[0].split(',')]


    # return the parsed data
    return data


def part1(data):            # -> ?
    ...

def part2(data):            # -> ?
    ...


if __name__ == "__main__":
    part1(get_input())
    part2(get_input())


# Samples
sample = [
    '.#..#',
    '.....',
    '#####',
    '....#',
    '...##'
]

# .7..7
# .....
# 67775
# ....7
# ...87

