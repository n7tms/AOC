# AOC 2015 day 19: 
#

# import aoc_utils as aoc
import time
import os
import re
# import numpy as np

DAY = '19'
# IN_FILE = os.path.join("AOC2015","2015"+str(DAY)+".txt")
IN_FILE = os.path.join("AOC2015","2015"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    # aoc.get_input(2023,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().split("\n")

    replacements = []
    regex = r"(\w+) => (\w+)"
    for r in data[0].split('\n'):
        vals = list(re.match(regex,r).groups())
        replacements.append([vals[0],vals[1]])

    return replacements,data[1]


def part1(medicine,replacements):    # => 

    molecules = []
    # iterate through the replacements
        # iterate through the medicine
            # replace the first occurence of the replacement
            # save the new medicine in a list of molecules
    # turn the molecule list into a set
    # return the length (count) in the molecule set


    for src,rep in replacements:
        start = 0
        while start < len(medicine):
            idx = medicine.find(src,start)
            


    return 0

def part2(data):    # => 

    return 0


if __name__ == "__main__":
    timestart = time.time()

    replacements,medicine = parse()

    print("\nDay 18: ===========================")
    print("part 1:",part1(medicine,replacements))
    # print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", f"{timeend-timestart:0.4f}", "\n")


