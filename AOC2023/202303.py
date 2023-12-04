# AOC 2023 day 3: 
#

import aoc_utils as aoc
import numpy as np

# IN_FILE = "AOC2023\\inputs\\202303.in"
# IN_FILE = "AOC2023\\inputs\\202303.sample.in"

IN_FILE = "AOC2023/inputs/202303.in"
# IN_FILE = "AOC2023/inputs/202303.sample.in"


def parse(puzzle_input):
    """
    Part Parse
    """
    with open(IN_FILE) as fp:
        out = []
        data = fp.read().splitlines()
    return data


def get_number(data,row,col) -> int:
    in_number = True
    the_number = []
    while in_number and col < len(data[row]):
        if data[row][col].isdigit():
            the_number.append(data[row][col])
            col += 1
        else:
            in_number = False
    return int("".join(the_number))

def adjacent_symbol(data,row,col) -> bool:
    """ returns False if no symbol is adjacent; otherwise True."""
    for d in aoc.DIRS:
        r = row + d[0]
        c = col + d[1]

        if r < 0 or c < 0 or c >= len(data[row]) or r >= len(data):
            pass
        else:
            if (not data[r][c].isdigit()) and (data[r][c] != "."):
                return True
    return False

def get_whole_number(data,row,col) -> int:
    number = []

    # look left
    c = col
    while data[row][c].isdigit() and c >= 0:
        number.insert(0,data[row][c])
        c -= 1
    
    # look right
    c = col + 1
    while c < len(data[row]) and data[row][c].isdigit():
        number.append(data[row][c])
        c += 1
    
    return int("".join(number))


def adjacent_part_number_upl(data,row,col) -> int:
    DIRS = ([-1,-1],[0,-1],[-1,0],[-1,1])
    for d in DIRS:
        r = row + d[0]
        c = col + d[1]
        if data[r][c].isdigit():
            return get_whole_number(data,r,c)
    
    return 0


def adjacent_part_number_dnr(data,row,col) -> int:
    DIRS = ([1,-1],[1,0],[0,1],[1,1])
    for d in DIRS:
        r = row + d[0]
        c = col + d[1]
        if data[r][c].isdigit():
            return get_whole_number(data,r,c)
    
    return 0

def adjacent_part_number(data,row,col) -> int:
    pn1 = 0
    pn2 = 0

    # look up
    DIRS = ([-1,-1],[-1,0],[-1,1])
    for d in DIRS:
        r = row + d[0]
        c = col + d[1]
        if data[r][c].isdigit():
            if pn1:
                pn2 = get_whole_number(data,r,c)
            else:
                pn1 = get_whole_number(data,r,c)
    
    # look left
    DIRS = ([0,-1],)
    for d in DIRS:
        r = row + d[0]
        c = col + d[1]
        if data[r][c].isdigit():
            if pn1:
                pn2 = get_whole_number(data,r,c)
            else:
                pn1 = get_whole_number(data,r,c)

    # look right
    DIRS = ([0,1],)
    for d in DIRS:
        r = row + d[0]
        c = col + d[1]
        if data[r][c].isdigit():
            if pn1:
                pn2 = get_whole_number(data,r,c)
            else:
                pn1 = get_whole_number(data,r,c)

    # look down
    DIRS = ([1,-1],[1,0],[1,1])
    for d in DIRS:
        r = row + d[0]
        c = col + d[1]
        if data[r][c].isdigit():
            if pn1:
                pn2 = get_whole_number(data,r,c)
            else:
                pn1 = get_whole_number(data,r,c)

    print(f"found: {pn1} and {pn2}")
    return pn1 * pn2




def part1(data):            # => 521601
    """
    Solve part 1
    """

    in_number = False
    already_added = False
    sum_of_part_numbers = 0
    part_number = 0

    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c].isdigit():
                if not in_number: 
                    # figure out what this number is
                    part_number = get_number(data,r,c)
                    in_number = True

                if already_added: 
                    continue
                elif adjacent_symbol(data,r,c):
                    sum_of_part_numbers += part_number
                    already_added = True

            else:
                already_added = False
                in_number = False
                part_number = 0

# figure out what the number is
# iterate across the ndigits of the number looking for adjacent symbols
# if a symmbol is found, return the number
#                 


        
    
    return sum_of_part_numbers


def part2(data):            # => 80694070
    """
    Solve part 2
    
    """
    sum_gear_ratios = 0
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] == "*":
                sum_gear_ratios += adjacent_part_number(data,r,c)
                # pn1 = adjacent_part_number_upl(data,r,c)
                # if pn1:
                #     pn2 = adjacent_part_number_dnr(data,r,c)
                # print(f"found: {pn1} and {pn2}")
                # sum_gear_ratios += (pn1 * pn2)

    return sum_gear_ratios

import re
from math import prod
from string import punctuation

def part22():
    # Courtesy of https://www.reddit.com/user/joshbduncan/

    data = open(IN_FILE).read().strip()

    nums = []
    symbols = set()
    re_symbols = "|".join(re.escape(s) for s in punctuation if s != ".")
    width = len(data.split("\n")[0])
    height = len(data.split("\n"))

    for i, line in enumerate(data.split("\n")):
        for m in re.finditer(r"\d+", line):
            nums.append((m.group(), i, m.start()))
        for m in re.finditer(re_symbols, line):
            symbols.add((i, m.start()))


    def coverage(num, row, col):
        return [
            (y, x)
            for y in range(row - 1, row + 2)
            for x in range(col - 1, col + len(num) + 1)
            if 0 <= y <= width and 0 <= x <= height
        ]

    p2 = 0
    for s in symbols:
        matching_nums = set()
        for n in nums:
            num, row, col = n
            if s in coverage(*n):
                matching_nums.add(int(num))
            if len(matching_nums) == 2:
                p2 += prod(matching_nums)
                break
    return p2



def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)

    print(f"part 1: {str(part1(data))}")
    # print(f"part 2: {str(part2(data))}")
    print(f"part 2: {str(part22())}")


if __name__ == "__main__":
    solve(IN_FILE)
        