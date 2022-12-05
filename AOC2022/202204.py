# AOC 2022 - Day 4

import time

IN_FILE = "d:\\Dev\AOC2022\\202204.txt"
# IN_FILE = "d:\\Dev\AOC2022\\202204.sample.txt"

def parse():
    """Parse input."""
    # pi = [line for line in puzzle_input.split("\n")]
    with open(IN_FILE) as f:
        out = [(line) for line in f.read().split('\n')]
    return out
        

def part1(data):            # => 464
    """Solve part 1."""
    count = 0
    for ranges in data:
        elf1,elf2 = ranges.split(',')
        e1s,e1e = elf1.split('-')
        e2s,e2e = elf2.split('-')
        if (int(e2s) >= int(e1s) and int(e2e) <= int(e1e)) or (int(e1s) >= int(e2s) and int(e1e) <= int(e2e)):
            count += 1
    return count


def part2(data):            # => 770
    """Solve part 2."""
    count = 0
    for ranges in data:
        elf1,elf2 = ranges.split(',')
        e1s,e1e = elf1.split('-')
        e2s,e2e = elf2.split('-')
        if (int(e2s) <= int(e1e) and int(e1s) <= int(e2e)) or (int(e1s) <= int(e2e) and int(e2s) <= int(e1e)):
            count += 1
    return count


if __name__ == "__main__":
    timestart = time.time()
    
    puzzle_input = parse()
    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))
