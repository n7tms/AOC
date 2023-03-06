# --- Day 17: No Such Thing as Too Much ---
# The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

# For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

# 15 and 10
# 20 and 5 (the first 5)
# 20 and 5 (the second 5)
# 15, 5, and 5
# Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?

import time
from itertools import combinations

IN_FILE = "AOC2015/201517.txt"

def parse():
    with open(IN_FILE) as f:
        out = [line for line in f.read().split('\n')]

    out = list(map(int,out))
    return out

def part1(data):    # => 1304
    count = 0
    for n in range(1, len(data)+1):
        for m in combinations(data, n):
            if sum(m) == 150:
                count += 1

    return count

def part2(data):    # => 18
    # It took me a while to understand this part.
    # What is the minimun containers required for 150?
    # If the answer is 4, then how many combinations of 4 containers = 150?
    min_containers = 0
    for n in range(1, len(data)+1):
        for m in combinations(data, n):
            if sum(m) == 150:
                min_containers += 1
        if min_containers > 0:
            break
    return min_containers


if __name__ == "__main__":
    timestart = time.time()

    puzzle_input = parse()

    print("\nDay 17: ===========================")
    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", f"{timeend-timestart:0.4f}", "\n")


