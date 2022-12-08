# AOC 2015 - Day 7

import time

IN_FILE = "AOC2015/201508.txt"
# IN_FILE = "AOC2015/201508.sample.txt"


def parse():
    """Parse input."""
    # pi = [line for line in puzzle_input.split("\n")]
    with open(IN_FILE) as f:
        out = [(line.strip()) for line in f.read().split('\n')]
    return out


def part1(data):            # => 1333
    """Solve part 1."""
    total_chars, actual_chars = 0,0

    for x in data:
        actual_chars += len(x)
        total_chars += len(eval(x))
        
        # total_chars += len(x)
        # tmp_chars = 0
        # # actual_chars += x.count('\\\"') // 2
        # # actual_chars += 2    #for the quotes on each end
        # # actual_chars += x.count('\\x') * 3
        # tmp_chars += x.count('\\\"')
        # tmp_chars += 2    #for the quotes on each end
        # tmp_chars += x.count('\\x') * 3
        # tmp_chars += x.count('\\\\')
        # actual_chars += tmp_chars

        # total_chars += len(x)
        # total_chars -= 2
        # total_chars -= x.count('\\\"')
        # total_chars -= x.count('\\x') * 3
        # total_chars -= x.count('\\\\')
        # print(x,eval(x),actual_chars,total_chars)

    return actual_chars - total_chars


def part2(data):            # => 2046
    """Solve part 2."""
    total_chars = 0
    for x in data:
        total_chars += 2 + x.count('\\') + x.count('"')
    return total_chars

if __name__ == "__main__":
    timestart = time.time()
    
    puzzle_input = parse()
    # print(puzzle_input)
    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))
