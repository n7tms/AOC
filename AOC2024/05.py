# AOC 2024 day 05: 
#

import aoc_utils as aoc
import time
import os

DAY = '05'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip()
    data = data.split('\n\n')

    rules = [list(map(int,line.split('|'))) for line in data[0].splitlines()]
    pages = [list(map(int,line.split(','))) for line in data[1].splitlines()]

    return rules, pages


def in_correct_order(rules, pages):
    for rule1, rule2 in rules:
        if rule1 in pages and rule2 in pages:
            if pages.index(rule1) > pages.index(rule2):
                return False

    return True

def part1(rules, pages_list):        # => 5329
    # iterate through pages, applying rules
    # which are in the correct order?
    # iterate through correctly ordered sets and find sum of middle pages

    correct_order = [pages for pages in pages_list if in_correct_order(rules, pages)]

    middle_value = sum([co[len(co)//2] for co in correct_order])
    return middle_value


def fix(rules, pages):
    sorted = False
    while not sorted:
        sorted = True
        for f,s in rules:
            if f in pages and s in pages:
                idx_f = pages.index(f)
                idx_s = pages.index(s)
                if idx_f > idx_s:
                    pages[idx_f], pages[idx_s] = pages[idx_s], pages[idx_f]
                    sorted = False

    return pages


def part2(rules, pages_list):       # => 5833
    # iterate through pages, applying rules
    # which are NOT in the correct order?
    # fix them and then find sum of the middle pages

    correct_order = [fix(rules,pages) for pages in pages_list if not in_correct_order(rules,pages)]
    middle_value = sum([co[len(co)//2] for co in correct_order])
    return middle_value


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    r,p = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(r,p))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(r,p))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        