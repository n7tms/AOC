# AOC 20215 - Day 13

import time
from collections import defaultdict
from itertools import permutations

IN_FILE = "AOC2015/201513.txt"
# IN_FILE = "AOC2015/201513.sample.txt"


def compute_happiness(seating, people):
    happiness = 0

    for idx,person in enumerate(seating):
        if idx < len(seating) - 1:
            next_person = seating[idx+1]
        else:
            next_person = seating[0]
    
        happiness += people[person][next_person]
        happiness += people[next_person][person]
    return happiness

def optimum_happiness(guests, people, first_person):
    perms = list(permutations(people))
    perm_happiness = {}
    for perm in perms:
        if perm <= perm[::-1]:
            perm = list(perm)
            perm.insert(0,first_person)

            perm_happiness[tuple(perm)] = compute_happiness(perm,guests)

    opt_perm_happy = max(perm_happiness.items(),key=lambda x: x[1])[0]
    return perm_happiness, opt_perm_happy

def add_me(guests):
    with_me = guests.copy()
    for person in guests:
        with_me[person]['Me'] = 0
        with_me['Me'][person] = 0
    return with_me


def parse():
    with open(IN_FILE) as f:
        out = [line for line in f.read().split('\n')]
    
    guests = defaultdict(dict)
    for line in out:
        tmp = line[:-1].split()
        person,g_l,hap_units,other_person = tmp[0],tmp[2],tmp[3],tmp[10]
        if g_l == "lose":
            hap_units = int(hap_units) * -1
        else:
            hap_units = int(hap_units)
        guests[person][other_person] = hap_units

    return guests


def part1(guests):          # -> 664
    people = set(guests.keys())
    first_person = people.pop()
    opt_hap, x = optimum_happiness(guests,people,first_person)
    return max(opt_hap.values())



def part2(guests):          # -> 640
    guests = add_me(guests)
    people = set(guests.keys())
    first_person = people.pop()
    opt_hap, x = optimum_happiness(guests,people,first_person)
    return max(opt_hap.values())


if __name__ == "__main__":
    timestart = time.time()
    
    guests = parse()
    print(guests)


    print("part 1:",part1(guests))
    print("part 2:",part2(guests))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))




