# --- Day 20:  ---

import time

# IN_FILE = "AOC2015/201519.txt"
target = 29000000


def part1(x):    # => >453125
    fs = []
    for i in range(1, x + 1):
        if x % i == 0:
            fs.append(i)
    
    total = 0
    for j in fs:
        total += j * 10
        if total >= target:
            return j


def part2(data):    # => 

    return 0


if __name__ == "__main__":
    timestart = time.time()

    puzzle_input = target
    puzzle_input2 = target

    print("\nDay 18: ===========================")
    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input2))
    
    timeend = time.time()
    print("Execution time: ", f"{timeend-timestart:0.4f}", "\n")


