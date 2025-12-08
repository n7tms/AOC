# AOC 2016 day 08: 
#

import time
import os

DAY = '08'
# IN_FILE = os.path.join("AOC2016","inputs","2016-"+str(DAY)+"-sample.txt")
IN_FILE = os.path.join("AOC2016","inputs","2016-"+str(DAY)+".in")

def parse(puzzle_input):
    """
    Parse
    """
    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()

    return data

def rect(display:list, size:list) -> list:
    for c in range(size[0]):
        for r in range(size[1]):
            display[r][c] = 1
    return display


def rotate_row(display:list, row: int, mag: int) -> list:
    mag %= len(display[row])
    display[row] =  display[row][-mag:] + display[row][:-mag]

    return display


def rotate_col(display:list, col: int, mag: int) -> list:
    """Rotate column 'col' downward by k steps (wrap bottom to top)."""
    rows = len(display)
    mag %= rows
    if mag == 0:
        return
    
    col_values = [display[r][col] for r in range(rows)]
    rotated = col_values[-mag:] + col_values[:-mag]
    
    for r in range(rows):
        display[r][col] = rotated[r]

    return display


def count_lights(display: list) -> int:
    on_lights = 0
    for line in display:
        on_lights += sum(line)
    
    return on_lights


def part1(x):        # => 128
    """
    Solve part 1
    """
    display = [[0] * 50 for _ in range(6)]
    for line in x:
        tokens = line.split()
        if tokens[0] == "rect":
            sc, sr = tokens[1].split("x")
            display = rect(display, [int(sc),int(sr)])
        else:
            if tokens[1] == "column":
                col = int(tokens[2][2:])
                mag = int(tokens[4])
                display = rotate_col(display, col, mag)
            else:
                row = int(tokens[2][2:])
                mag = int(tokens[4])
                display = rotate_row(display, row, mag)

    return count_lights(display)
        

def part2(x):        # => EOARGPHYAO
    """
    Solve part 2
    """
    display = [[0] * 50 for _ in range(6)]
    for line in x:
        tokens = line.split()
        if tokens[0] == "rect":
            sc, sr = tokens[1].split("x")
            display = rect(display, [int(sc),int(sr)])
        else:
            if tokens[1] == "column":
                col = int(tokens[2][2:])
                mag = int(tokens[4])
                display = rotate_col(display, col, mag)
            else:
                row = int(tokens[2][2:])
                mag = int(tokens[4])
                display = rotate_row(display, row, mag)

    for r in display:
        for dig in r:
            if dig == 1:
                print("X", end="")
            else:
                print(" ", end="")
        print("")
    return 0


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    x = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(x))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(x))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve(IN_FILE)
        