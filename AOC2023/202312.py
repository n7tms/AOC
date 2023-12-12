# AOC 2023 day 12: Hot Springs
#

import aoc_utils as aoc
import time
import os
import numpy as np
import exrex


# IN_FILE = os.path.join("AOC2023","inputs","202312.in")
IN_FILE = os.path.join("AOC2023","inputs","202312.sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2023,12,False)

    with open(IN_FILE) as fp:
        data = fp.read().split("\n")
    
    condition_records = []
    for line in data:
        spring_conditions, p = line.split(" ")
        pattern = [int(x) for x in p.split(",")]
        condition_records.append((spring_conditions,pattern))
    return condition_records


def is_valid(cond_rec, pattern) -> bool:
    # cond_rec looks like '#.#.###'
    # pattern looks like [1,1,3]
    # determine if cond_rec matches pattern
    springs = cond_rec.split(".")   # ['#','#','###']
    spring_count = [i for i in [s.count('#') for s in springs] if i > 0]
    

    if spring_count == pattern:    
        return True
    else:
        return False

def generate_regex(pattern):
    """
    Generates a regular expression based on a given pattern with wildcards.

    Args:
    pattern (str): The pattern with wildcards ("?" for any character).

    Returns:
    str: The generated regular expression.
    """
    regex_chars = []
    for char in pattern:
        if char == "?":
            regex_chars.append("[.#]")
        else:
            regex_chars.append(char)
    return "^" + "".join(regex_chars) + "$"


def part1(condition_records):        # => 7204
    """
    Solve part 1
    
    """

    total_valid = 0
    for x in condition_records:
        this_valid = 0
        springs, pattern = x
        spring_re = generate_regex(springs.replace('.','\\.'))
        options = list(exrex.generate(spring_re))

        for y in options:
            if y.count("#") == sum(pattern):
                if is_valid(y,pattern):
                    total_valid += 1

    return total_valid


def part2(condition_records):            # => 1672318386674
    # This is the correct answer, but is was received from 202312.a.py.
    # https://topaz.github.io/paste/#XQAAAQCBBgAAAAAAAAA0m0pnuFI8c/T1e0vJBsZpw7o6qWXaGffgC3nca072y4us6B1UAQiJgfnY4yag93N/+aA72Y5CrxtgYd+jHLxeVCAWc1RqFMB7ho41VToLPe5X9aYN9O6j+zt06VoM/jigV5a7Gc7qUDtI/vdOmSsu0kgZ5NUKib82FQbLfNUPoHjhnpxP76z4Ywlp2tUKNx2xWZPy6u2LaWHXQKPIcCHqNX8x9H9HjHdIWA0a8/12Bhz9WaiT3WSZUg2KT0KKyh+YHy65ftfcRr2rM728FWb/R0Qka84rR6snSkZAPFwob+z45GUQr1rYqhtUcFMWGfG6EBUDVlPmD5tB9ECOSjTs2yf+a+1NHaiaqg3R+44BODFjWSLet9WyQP1BCu8Hx4miPjSWD5P56ew2hx/M2bGOnzCvyYNWhWF0DWOV38Tf/JatBpt51L8v04tuQ4hituHXAxBnhPHEM2EPmw68Py5AS3t4cej8Xyvqwnh0J/9BeqbsTRTjsBHdGkcqQ01Z5GmDmDCQVxVabq4z4Cfc4mI8PYRgt5OBF9XMTszWxry3/ZVIUFXRXB8GOpVM/7OAT07C0voeNmNQa3I8kjAKBWTCgrxmPLex0dbsocp0/8LE73bYAjsesTReXU0bvg5ejLL3Db69cGnYubeHc57M7gROjREcwM9p7asfroxWuRjhNUNUyAiPrPVr+MZZEneKDQzA919s4jx9icFfM/D3ay+8FfCbzGufn/2BXV6dJNCmU5r7nWePvLnEbeLXIKE1JqNV0qffFAavUkTnkrSvhJQJvyaJFTnHml9QXeI80xCC9mpjsTwzjSFKy+l9aYBNyjdBLDjctjn8sgitx/xZDTBzdCZAgfHyo+sxz4CRIeys/dWx4WqGfkD3Df8ZsbA0RKOocIkqwpMhRpN8y9VODTvAnYep9AWaaP/u8dcqQQvojn+337HFS58VnHWJg9jmGKS0+XWsYUVHFFS67+z0mXAYmE0k5SERjGAIlLQAb4A+5iJS69Ft+Kb8E1MT4udo+nH+04LdL494ge0SeDFeWfjXcyKWi6gorZNw/61TbPM=
    # !!! I don't even know how he got there !!!
    """
    Solve part 2
    """
    total_valid = 0
    for x in condition_records:
        this_valid = 0
        s, p = x

        # unfold (make 5 copies...)
        springs = ""
        pattern = []
        for _ in range(4):
            springs = springs + s + '?'
            pattern.extend(p)
        springs += s
        pattern.extend(p)

        spring_re = generate_regex(springs.replace('.','\\.'))
        options = list(exrex.generate(spring_re))

        for y in options:
            if y.count("#") == sum(pattern):
                if is_valid(y,pattern):
                    total_valid += 1

    return total_valid


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)

    start_time = time.time()
    # p1 = str(part1(data))
    exec_time = time.time() - start_time
    # print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(data))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        