# AOC 2018 day 14: 
# 

import aoc_utils as aoc
import time
import os
from collections import deque


DAY = '14'
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".sample.txt")

# def parse():
#     """
#     Parse
#     """
#     aoc.get_input(2018,DAY,False)

#     with open(IN_FILE) as fp:
#         data = fp.read().splitlines()
    
#     return 



def part1(data):        # => 3171123923
    recipes = [3,7]
    elf1 = 0
    elf2 = 1

    round = 0
    while round < data+11:
        new_recipe = recipes[elf1] + recipes[elf2]
        if new_recipe > 9:
            recipes.append(1)
            recipes.append(new_recipe-10)
        else:
            recipes.append(new_recipe)
        
        # print(recipes)
        elf1 = (recipes[elf1] + 1 + elf1) % len(recipes)
        elf2 = (recipes[elf2] + 1 + elf2) % len(recipes)
        round += 1


    scores = ''.join([str(x) for x in recipes[data:data+10]])
    return scores


def part2(data):        # =>  15615388 < x <3171123923
    data_str = str(data)
    recipes = [3,7]
    elf1 = 0
    elf2 = 1

    round = 0
    while True:
        new_recipe = recipes[elf1] + recipes[elf2]
        if new_recipe > 9:
            recipes.append(1)
            recipes.append(new_recipe-10)
        else:
            recipes.append(new_recipe)



        start = len(recipes) - len(str(data))
        checking1 = ''.join([str(x) for x in recipes[start:]])
        checking2 = ''.join([str(x) for x in recipes[start-1:-1]])
        # if str(data) in [checking1, checking2]:
        if '765071' in [checking1, checking2]:
            return start
        
        # print(recipes)
        elf1 = (recipes[elf1] + 1 + elf1) % len(recipes)
        elf2 = (recipes[elf2] + 1 + elf2) % len(recipes)
        round += 1

        if round > 3171123923: return 'to large'

    scores = ''.join([str(x) for x in recipes[data:data+10]])
    return scores


def part3(): # => 20353748
    # from Jead
    # https://www.reddit.com/r/adventofcode/comments/a61ojp/comment/ebr8abv/

    recipes = '765071'

    score = '37'
    elf1 = 0
    elf2 = 1
    while recipes not in score[-8:]:
        score += str(int(score[elf1]) + int(score[elf2]))
        elf1 = (elf1 + int(score[elf1]) + 1) % len(score)
        elf2 = (elf2 + int(score[elf2]) + 1) % len(score)

    print('Part 1:', score[int(recipes):int(recipes)+10])
    print('Part 2:', score.index(recipes))



def solve():
    """Solve the puzzle for the given input."""
    # data = parse()
    # data = 765071
    data = 59414

    # start_time = time.time()
    # p1 = str(part1(data))
    # exec_time = time.time() - start_time
    # print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    # p2 = str(part2(data))
    p2 = str(part3())
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve()

