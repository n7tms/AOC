# AOC 2023 day 17: Clumsy Crucible
#

import aoc_utils as aoc
import time
import os
import numpy as np

DAY = 17
# IN_FILE = os.path.join("AOC2023","inputs","2023"+str(DAY)+".in")
IN_FILE = os.path.join("AOC2023","inputs","2023"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2023,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().split("\n")

    data = [[c for c in row] for row in data]
    return data

def min_cost(data,src: tuple, dst: tuple) -> int:
    # Dynamic Programming Python implementation of Min Cost Path
    # problem
    R = len(data)
    C = len(data[0])

    # def minCost(cost, m, n):
    m,n = dst

	# Instead of following line, we can use int tc[m + 1][n + 1] or
	# dynamically allocate memory to save space. The following
	# line is used to keep te program simple and make it working
	# on all compilers.
    tc = [[0 for x in range(C)] for x in range(R)]

    tc[0][0] = data[0][0]

	# Initialize first column of total cost(tc) array
    for i in range(1, m + 1):
        tc[i][0] = tc[i-1][0] + data[i][0]

	# Initialize first row of tc array
    for j in range(1, n + 1):
        tc[0][j] = tc[0][j-1] + data[0][j]

	# Construct rest of the tc array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # tc[i][j] = min(tc[i-1][j-1], tc[i-1][j],tc[i][j-1]) + data[i][j]
            tc[i][j] = min(tc[i-1][j],tc[i][j-1]) + data[i][j]

    return tc[m][n]




def part1(data):        # => 
    """
    Solve part 1
    
    """
    cost = [[1, 2, 3],
            [4, 8, 2],
            [1, 5, 3]]
    print(min_cost(data, (0,0), (len(data),len(data[0]))))


    return


def part2(data):            # => 
    """
    Solve part 2
    """


    return

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(data))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(data))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        