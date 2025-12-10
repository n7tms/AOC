# AOC 2016 day 10: 
#

import time
import os

DAY = '10'
IN_FILE = os.path.join("AOC2016","inputs","2016-"+str(DAY)+"-sample.txt")
# IN_FILE = os.path.join("AOC2016","inputs","2016-"+str(DAY)+".in")

def parse(puzzle_input):
    """
    Parse
    """
    with open(IN_FILE) as fp:
        data = fp.read().strip()

    return data

class node():
    value1 = None
    value2 = None
    low_dest = None
    high_dest = None



def part1(x):        # => 
    """
    Solve part 1
    """
   
    # value-61 goes to 32


    return 0
        

def part2(x):        # => 
    """
    Solve part 2
    """

    

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
        