# AOC 2015 - Day 15

import time
import re

IN_FILE = "AOC2015\\201515.txt"
# IN_FILE = "AOC2015\\201515.sample.txt"

def parse():
    # with open(IN_FILE) as f:
    #     out = [line for line in f.read().split('\n')]
    text = open(IN_FILE).read()

    # Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
    regex = r'(\w+): capacity (\d+), durability (\d+), flavor (\d+), texture (\d+), calories (\d+)'
    ingredients = []
    for ingr, cap, dur, fla, tex, cal in re.findall(regex,text):
        ingredients.append[list(ingr,cap,dur,fla,tex,cal)]
        

    return ingredients


def part1(distances):
    pass

def part2(distances):
    pass

if __name__ == "__main__":
    timestart = time.time()
    
    puzzle_input = parse()
    # print(puzzle_input)


    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))

