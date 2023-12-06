# AOC 2023 day 6: Wait for it
#

import aoc_utils as aoc
import time
import numpy as np

# IN_FILE = "AOC2023\\inputs\\202306.in"
# IN_FILE = "AOC2023\\inputs\\202306.sample.txt"

IN_FILE = "AOC2023/inputs/202306.txt"
# IN_FILE = "AOC2023/inputs/202306.sample.txt"

def parse(puzzle_input):
    """
    Parse
    """
    with open(IN_FILE) as fp:
        out = []
        # data = fp.read().splitlines()
        data = fp.read().split("\n")

        times = [x for x in data[0].split(":")[1].split(" ") if x]
        distances = [x for x in data[1].split(":")[1].split(" ") if x]


    return times,distances

def race(btn_hold, race_duration) -> int:
    return (race_duration - btn_hold) * btn_hold


def part1(times,records):            # => 5133600
    """
    Solve part 1
    
    """
    # convert values to ints
    times = [int(i) for i in times]
    records = [int(i) for i in records]

    winners = []
    for idx, r in enumerate(times):
        win_count = 0
        for x in range(r):
            dst = race(x, r)
            if dst > records[idx]:
                win_count += 1
        winners.append(win_count)
    
    return np.prod(winners)

def part2(times, records):            # => 40651271
    """
    Solve part 2
    """
    # convert list of times and records to single number(s)
    # (brute-forced; there is probably a faster way.)
    times = int("".join(times))
    records = int("".join(records))

    win_count = 0
    for x in range(times):
        dst = race(x, times)
        if dst > records:
            win_count += 1

    return win_count


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    times, records = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(times, records))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(times, records))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        