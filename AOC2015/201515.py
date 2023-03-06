# AOC 2015 - Day 15

import time
import re

IN_FILE = "AOC2015\\201515.txt"
# IN_FILE = "AOC2015\\201515.sample.txt"

def parse():
    with open(IN_FILE) as f:
        out = [line for line in f.read().split('\n')]

    # Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
    ingredients = []
    for x in out:
        ingr, a = x.split(':')
        b = a.split(' ')
        _,cap,_,dur,_,fla,_,tex,_,cal = a.strip().split(' ')
        ingredients.append(list([ingr,int(cap.strip(',')),int(dur.strip(',')),int(fla.strip(',')),int(tex.strip(',')),int(cal)]))

    return ingredients


def part1(ingredients):     # -> 13882464, 11171160
    imax = 0
    imax500 = 0

    for a in range(1,100):
        for b in range(1,100):
            for c in range(1,100):
                for d in range(1,100):
                    if a + b + c + d == 100:
                        cap = (a * ingredients[0][1]) + (b * ingredients[1][1]) + (c * ingredients[2][1]) + (d * ingredients[3][1])
                        dur = (a * ingredients[0][2]) + (b * ingredients[1][2]) + (c * ingredients[2][2]) + (d * ingredients[3][2])
                        fla = (a * ingredients[0][3]) + (b * ingredients[1][3]) + (c * ingredients[2][3]) + (d * ingredients[3][3])
                        tex = (a * ingredients[0][4]) + (b * ingredients[1][4]) + (c * ingredients[2][4]) + (d * ingredients[3][4])
                        cal = (a * ingredients[0][5]) + (b * ingredients[1][5]) + (c * ingredients[2][5]) + (d * ingredients[3][5])
                        if cap < 0: cap = 0
                        if dur < 0: dur = 0
                        if fla < 0: fla = 0
                        if tex < 0: tex = 0
                        total = cap * dur * fla * tex
                        imax = max([imax,total])
                        if cal == 500:
                            imax500 = max([imax500,total])
    
    return imax,imax500


if __name__ == "__main__":
    timestart = time.time()
    
    puzzle_input = parse()
    p1,p2 = part1(puzzle_input)

    print("part 1:",p1)
    print("part 2:",p2)
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))

