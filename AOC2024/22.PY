# AOC 2024 day 22: 
#

import aoc_utils as aoc
import time
import os
import aoc_utils as aoc

DAY = '22'
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()
        
    secret_numbers = [int(x) for x in data]
    return secret_numbers


def evolve_secret_number(secret_number:int, times:int):
    for _ in range(times):
        secret_number = ((secret_number ^ (secret_number * 64)) % 16777216 ^ ((secret_number ^ (secret_number * 64)) % 16777216 // 32)) % 16777216 ^ (((((secret_number ^ (secret_number * 64)) % 16777216 ^ ((secret_number ^ (secret_number * 64)) % 16777216 // 32)) % 16777216) * 2048)) % 16777216
    return secret_number


def part1(data:list,t:int):        # => 18694566361
    new_numbers = sum([evolve_secret_number(sn,t) for sn in data])
    return new_numbers


def part2(data):       # => 
    t = 2000
    # create a dictionary of price changes for each secret number
    # which four-price sequence occurs most frequently
    # Feed that sequence through the dictionary to count bananas

    # one's digit = number % 10

    # create a list of all the differentials
    secret_numbers = []
    for secnum in data:
        sn = []
        prev = secnum % 10
        new_num = secnum
        for _ in range(t):
            new_num = evolve_secret_number(new_num,1)
            ones = new_num % 10
            sn.append([ones, ones-prev])
            prev = new_num % 10
        secret_numbers.append(sn)
    
    # Select the best pattern       
    


    return    





def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(data,2000))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(data))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        