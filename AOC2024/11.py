# AOC 2024 day 11: 
#

import aoc_utils as aoc
import time
import os
from collections import Counter

DAY = '11'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")


def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()
    
    stones = data[0].split(' ')
    return stones




def part1(stones: list, blinks):        # => 199982
    for rnd in range(blinks):
        print(f'{rnd}', end=' ')
        idx = 0
        while idx < len(stones):
            stone = stones[idx]
            if stone == '0':
                stones[idx] = '1'
                idx += 1
            elif len(stone) % 2 == 0:
                length = len(stone) // 2
                stones.insert(idx, str(int(stone[0:length])))
                stones[idx+1] = str(int(stone[length:]))
                idx += 2
            else:
                stones[idx] = str(int(stones[idx]) * 2024)
                idx += 1

    return len(stones)




# Function to split a number into two parts if it has an even number of digits
def split_number(n):
    str_n = str(n)
    half = len(str_n) // 2
    left = int(str_n[:half])
    right = int(str_n[half:])
    return left, right


# 75 blinks takes a long time. Let's try a different approach
def part2(s, blinks):       # => 237149922829154
    stones = [int(s1) for s1 in s]

    # Use a frequency table to count stones
    stone_counts = Counter(stones)

    for _ in range(blinks):
        new_counts = Counter()

        for stone, count in stone_counts.items():
            if stone == 0: 
                new_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                left, right = split_number(stone)
                new_counts[left] += count
                new_counts[right] += count
            else:  
                new_counts[stone * 2024] += count

        stone_counts = new_counts

    return sum(stone_counts.values())




def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(data, 25))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    data = parse(puzzle_input)

    start_time = time.time()
    p2 = str(part2(data, 75))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        