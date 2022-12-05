# AOC 2015 - Day 5

import time

# IN_FILE = "d:\\Dev\AOC2015\\201505.txt"
IN_FILE = "d:\\Dev\AOC2015\\201505.sample.txt"


def parse():
    """Parse input."""
    # pi = [line for line in puzzle_input.split("\n")]
    with open(IN_FILE) as f:
        out = [(line) for line in f.read().split('\n')]
    return out

not_strings = ["ab","cd","pq","xy"]


def naughty(astring):
    # print(astring)
    bad = [1 for s in astring if any(x in s for x in not_strings)]
    print(bad)
    if not bad:
        return True
    else:
        return False



def part1(data):            # => 254575
    """Solve part 1."""
    nice_strings = 0
    for strng in data:
        if not naughty(strng):
            nice_strings += 1
    print(nice_strings)


def part2(data):            # => 1038736
    """Solve part 2."""



if __name__ == "__main__":
    timestart = time.time()
    
    puzzle_input = parse()
    # print(puzzle_input)
    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))
