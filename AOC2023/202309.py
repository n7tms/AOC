# AOC 2023 day 9: Mirage Maintenance
#

import aoc_utils as aoc
import time
import os


IN_FILE = os.path.join("AOC2023","inputs","202309.in")
# IN_FILE = os.path.join("AOC2023","inputs","202309.sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2023,9,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().split("\n")
    
    histories = []
    for d in data:
        
        histories.append([int(i) for i in d.split(' ')])

    return histories


def next_term(history: list) -> int:
    if sum(history) == 0:
        return 0
    else:
        cmp = [[x,y] for x,y in zip(history,history[1:])]
        new_hist = [y-x for x,y in cmp]
        out = next_term(new_hist)
        return new_hist[-1] + out

def prev_term(history: list) -> int:
    if sum(history) == 0:
        return 0
    else:
        cmp = [[x,y] for x,y in zip(history,history[1:])]
        new_hist = [y-x for x,y in cmp]
        out = prev_term(new_hist)
        return new_hist[0] - out


def part1(histories):        # => 1702218515
    """
    Solve part 1
    
    """
    total = 0
    for history in histories:
        total += next_term(history) + history[-1]

    return total



def part2(histories):            # => 925
    """
    Solve part 2
    """

    total = 0
    for history in histories:
        total += history[0] - prev_term(history)

    return total


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
        