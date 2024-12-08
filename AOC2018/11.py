# AOC 2018 day 11: 
#

import aoc_utils as aoc
import time
import os
import re


DAY = '11'
IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".sample.txt")

def parse():
    """
    Parse
    """
    aoc.get_input(2018,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()

    points = []
    for d in data:
        numbers = re.findall(r"-?\d+",d)
        numbers = [int(num) for num in numbers]
        points.append(numbers)

    # matches = re.search(r"position=< (\d+), (\d+)> velocity=<(\d+), (\d+)>", data[0])
    # players = int(matches.group(1))
    # points = int(matches.group(2))
    
    return points


def print_grid(points):
    # Determine the size of the grid
    max_row = max(coord[0] for coord in points)
    max_col = max(coord[1] for coord in points)

    # Create an empty grid
    grid = [["." for _ in range(max_col + 1)] for _ in range(max_row + 1)]

    # Mark the points on the grid
    for row, col, _, _ in points:
        grid[row][col] = "X"

    # Display the grid
    for row in grid:
        print("".join(row))

    print('\n')


def part1(points):        # => XECXBPZB at 10124 seconds
    
    # by looking at the data, I can tell that things are going to get pretty close together after ~10000 seconds.
    # i ran the program to there and then set breakpoints to see how close it was getting until a message appeared.
    # (There must be a programmatic way to determine when the message appears.)
    # My text appears vertical and mirrored. Hmmm.
    seconds = 0
    while True:
        points = [[posc+velc,posr+velr,velc,velr] for posc, posr, velc, velr in points]

        seconds += 1
        if seconds == 10124:
            print_grid(points)
            return seconds
        


def part2(data):        # => 10124
    return


def solve():
    """Solve the puzzle for the given input."""
    data = parse()

    start_time = time.time()
    p1 = str(part1(data))
    # p1 = str(part1(13, 7999))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(data))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve()

