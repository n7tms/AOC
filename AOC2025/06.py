# AOC 2025 day 06: 
#

import aoc_utils as aoc
import time
import os
import math

DAY = '06'
IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+"-sample.txt")
# IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+".in")

def parse(puzzle_input):
    """
    Parse
    """
    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()

    problems = []
    for line in data:
        aline = []
        for x in line.split():
            aline.append(x)
        problems.append(aline)

    return data


def part1(x):        # => 3525371263915
    problems = []
    for line in x:
        aline = []
        for x in line.split():
            aline.append(x)
        problems.append(aline)


    total_sum = 0
    ops = len(problems)-1

    for i, _ in enumerate(problems[0]):
        digits = []
        for dig in range(ops):
            digits.append(int(problems[dig][i]))
        
        if problems[ops][i] == "+":
            total_sum += sum(digits)
        else:
            total_sum += math.prod(digits)
            
    return total_sum


def part2(x):        # => 
    problems = []
    for line in x:
        aline = []
        for x in line:
            aline.append(x)
        problems.append(aline)


    total_sum = 0
    ops = len(problems)-1

    op = ""
    numbers = []
    for i, _ in enumerate(problems[0]):

        # get the operator
        if problems[ops][i] != " ":
            op = problems[ops][i]

        # get the digits
        digits = []
        for dig in range(ops):
            digits.append(int(problems[dig][i]))
        numbers.append(int("".join(digits))) # do something right here to detect a space in every column; if so, then perform the calculation and reset for the next


        if problems[ops][i] == "+":
            total_sum += sum(digits)
        else:
            total_sum += math.prod(digits)
            
    return total_sum


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
        