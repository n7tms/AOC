# AOC 2024 day 22: 
#

import aoc_utils as aoc
import time
import os

DAY = '25'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")


def calc_pins_lock(lock: list) -> list:
    pins = [0]*5

    for c in range(len(lock[0])):
        for r in range(len(lock)):
            if r == 0: continue
            if lock[r][c] == '.':
                pins[c] = r - 1
                break
    return pins

def calc_pins_key(key: list) -> list:
    pins = [0]*5

    for c in range(len(key[0])):
        for r in range(len(key)-1,-1,-1):
            if r == 6: continue
            if key[r][c] == '.':
                pins[c] = 6 - r - 1
                break
    return pins


def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().split('\n\n')

    keys = []
    locks = []

    for item in data:
        something = item.splitlines()
        if something[0][0] == '#': #lock
            locks.append(calc_pins_lock(something))
        else: #key
            keys.append(calc_pins_key(something))
    return keys, locks

def lock_key(lock:list, key:list) -> bool:
    for i in range(len(lock)):
        if lock[i] + key[i] <= 5:
            continue
        else:
            return False
    return True


def part1(locks:list, keys:list):        # => 2770
    fit = sum(1 for k in keys for l in locks if lock_key(k,l))
    return fit

# def part2(locks:list, keys:list):       # => 

#     return    





def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    l,k = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(l,k))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    # start_time = time.time()
    # p2 = str(part2(l,k))
    # exec_time = time.time() - start_time
    # print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        