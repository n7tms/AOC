# AOC 2015 - Day 5

import time

IN_FILE = "AOC2015\\201505.txt"
# IN_FILE = "AOC2015\\201505.sample.txt"

def parse():
    """Parse input."""
    # pi = [line for line in puzzle_input.split("\n")]
    with open(IN_FILE) as f:
        out = [(line) for line in f.read().split('\n')]
    return out

def naughty(astring):
    bad_strings = ["ab","cd","pq","xy"]
    for bs in bad_strings:
        if bs in astring:
            return True
    return False

def three_vowels(astring):
    vowels = ['a','e','i','o','u']
    qty = 0
    for v in vowels:
        qty += astring.count(v)
    if qty >= 3:
        return True
    else:
        return False

def double_letters(astring):
    for i in range(len(astring)-1):
        if astring[i] == astring[i+1]:
            return True
    return False

def two_double_letters(astring):
    for i in range(len(astring)-2):
        if astring[i:i+2] in astring[i+2:]:
            return True
    return False

def letter_skip_letter(astring):
    for i in range(len(astring)-2):
        if astring[i] == astring[i+2]:
            return True
    return False


def part1(data):            # => 238
    """Solve part 1."""
    nice_strings = 0
    for strng in data:
        if three_vowels(strng) and double_letters(strng) and not naughty(strng):
            nice_strings += 1
    return nice_strings


def part2(data):            # => 69
    """Solve part 2."""
    nice_strings = 0
    for strng in data:
        if two_double_letters(strng) and letter_skip_letter(strng):
            nice_strings += 1
    return nice_strings


if __name__ == "__main__":
    timestart = time.time()
    
    puzzle_input = parse()
    # print(puzzle_input)
    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))
