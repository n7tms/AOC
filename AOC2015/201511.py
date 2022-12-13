# AOC 2015 - Day 11

import time

# input = "hxbxwxba"
input = "hxaaaxwxabc"


def meets_rules(pwd):
    crit1 = False
    crit2 = False
    crit3 = False

    # increasing straight of three consecutive letters (e.g. 'abc', 'pqr', etc.)
    for i in range(len(pwd)-2):
        tmp = ord(pwd[i])
        if pwd[i:i+3] == "".join([chr(tmp),chr(tmp+1),chr(tmp+2)]):
            crit1 = True
            break
    print(crit1)

    # does not contain 'i', 'o', or 'l'
    if 'i' not in pwd and 'o' not in pwd and 'l' not in pwd:
        crit2 = True
    print(crit2)

    # two different, non-overlapping pairs of letters (e.g. 'aagg', 'ttqq', etc.)
    cnt = 0
    i = 0
    while i < len(pwd)-1:
        if pwd[i] == pwd[i+1]:
            cnt += 1
            i += 1
        i += 1
    if cnt > 1:
        crit3 = True
    print(crit3)


    return crit1 & crit2 & crit3


def part1(data):            # => 
    """Solve part 1."""
    return meets_rules(input)

def part2(data):            # => 
    """Solve part 2."""


if __name__ == "__main__":
    timestart = time.time()

    print("part 1:",part1(input))
    print("part 2:",part2(input))
    
    timeend = time.time()
    print("Execution time: ", f"{timeend-timestart:0.4f}")

