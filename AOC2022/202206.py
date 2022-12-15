# AOC 2022 - Day 6

import time

IN_FILE = "AOC2022\\inputs\\202206.txt"

def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        out = [(line) for line in f.read().split('\n')]
    return out[0]

def part1(data):            # => 1356
    """Solve part 1."""
    for idx in range(len(data)-4):
        marker = data[idx:idx+4] 
        if len(set(marker)) == 4:
            return idx+4

def part2(data):            # => 2564
    """Solve part 2."""
    for idx in range(len(data)-14):
        marker = data[idx:idx+14] 
        if len(set(marker)) == 14:
            return idx+14

def part1b(data):
    # from reddit/xelf
    # https://www.reddit.com/r/adventofcode/comments/zdw0u6/2022_day_6_solutions/iz3m3if/?context=3
    print(next(i for i,c in enumerate(data) if len(set(data[i-4:i]))==4))

if __name__ == "__main__":
    timestart = time.time()
    
    puzzle_input = parse()
    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    print(part1b(puzzle_input))

    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))
