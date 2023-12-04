# AOC 2023 day 3: Gear Ratios
#

import aoc_utils as aoc
import numpy as np

# IN_FILE = "AOC2023\\inputs\\202303.in"
# IN_FILE = "AOC2023\\inputs\\202303.sample.in"

IN_FILE = "AOC2023/inputs/202303.in"
# IN_FILE = "AOC2023/inputs/202303.sample.in"


def parse(puzzle_input):
    """
    Get the input
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


def convert_to_num(pn: list) -> int:
    return int("".join(pn))

def search_for_gear(data, coords: tuple) -> tuple:
    """search surrounding coords for an '*' """

    r,c = coords
    for x,y in aoc.DIRS:
        dr = r + x
        dc = c + y

        if 0 <= dr < len(data) and 0 <= dc < len(data[r]):
            if data[dr][dc] == "*":
                return (dr,dc)
    
    return None

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

    return sum_of_part_numbers


def part2(data):            # => 80694070
    """
    Solve part 2
    """
    gears = dict() # (x,y): [[x,y],[x,y]]
    part_number = []
    found_gear = tuple()

    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c].isdigit():
                part_number.append(data[r][c])
                if not found_gear:
                    found_gear = search_for_gear(data,(r,c))
            else:
                if found_gear:
                    if found_gear in gears:
                        gears[found_gear].append(convert_to_num(part_number))
                    else:
                        gears[found_gear] = [convert_to_num(part_number)]
                # else:
                found_gear = tuple()
                part_number = []
        
        # handle edge case -- literally!
        # this block executes at the end of each row.
        # if found_gear == True, then there was a part_number on the edge of the line
        # adjacent to a gear and we need to deal with it.
        if found_gear:
            if found_gear in gears:
                gears[found_gear].append(convert_to_num(part_number))
            else:
                gears[found_gear] = [convert_to_num(part_number)]

        # regardless if we found a gear, we're at the end of the row and nothing carries over.
        found_gear = tuple()
        part_number = []



    product_of_gears = 0
    for g in gears.values():
        if len(g) == 2:
            product_of_gears += g[0] * g[1]
    
    return product_of_gears




def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)

    print(f"part 1: {str(part1(data))}")
    print(f"part 2: {str(part2(data))}")


if __name__ == "__main__":
    solve(IN_FILE)
        