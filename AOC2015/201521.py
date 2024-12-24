# --- Day 21:  ---

import itertools
import time
import re

IN_FILE = "AOC2015/201521.txt"
# IN_FILE = "AOC2015/201521.sample.txt"

def parse():
    with open(IN_FILE) as f:
        out = [line for line in f.read().splitlines()]

    # [hp, damage, armor]
    traits = [int(re.findall(r'\d+', x)[0]) for x in out]
    return traits

weapons = [[8,4,0],[10,5,0],[25,6,0],[40,7,0],[74,8,0]]
armor = [[0,0,0],[13,0,1],[31,0,2],[53,0,3],[75,0,4],[102,0,5]]
rings = [[0,0,0],[25,1,0],[50,2,0],[100,3,0],[20,0,1],[40,0,2],[80,0,3]]


def fight(weapon, armor, rings, boss):
    bhps, bdam, barm = boss
    phps = 100

    pdam, parm, cost = weapon[1], armor[2], weapon[0]+armor[0]
    for ring in rings:
        pdam += ring[1]
        parm += ring[2]

    while phps > 0 and bhps > 0:
        tdam = pdam - barm
        bhps -= max[1,tdam]
        if bhps < 1: return cost

        tdam = bdam - parm
        phps -= max[1,tdam] 

    return int('inf')



def part1(boss):    # => 
    min_cost = float('inf')

    choices_weapons = weapons
    choices_armor = armor
    choices_rings = rings + [list(r1 + r2) for r1, r2 in itertools.combinations(rings, 2)]
    all_combinations = list(itertools.product(choices_weapons, choices_armor, choices_rings))

    for w,a,r in all_combinations:
        cost = fight(w,a,r, boss)
        min_cost = min(min_cost,cost)

    return min_cost

def part2(data):    # => 
    return    


if __name__ == "__main__":
    timestart = time.time()

    puzzle_input = parse()

    print("\nDay 21: ===========================")
    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", f"{timeend-timestart:0.4f}", "\n")


