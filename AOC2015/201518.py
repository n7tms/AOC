# --- Day 18:  ---

import time

IN_FILE = "AOC2015/201517.txt"

def parse():
    with open(IN_FILE) as f:
        out = [line for line in f.read().split('\n')]

    out = list(map(int,out))
    return out

def part1(data):    # => 
    return 0

def part2(data):    # => 
    return 0


if __name__ == "__main__":
    timestart = time.time()

    puzzle_input = parse()

    print("\nDay 18: ===========================")
    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", f"{timeend-timestart:0.4f}", "\n")


