# AOC 2015 - Day 9

import time
from itertools import permutations
from collections import defaultdict

IN_FILE = "AOC2015\\201509.txt"
# IN_FILE = "AOC2015\\201509.sample.txt"

def parse():
    with open(IN_FILE) as f:
        out = [line for line in f.read().split('\n')]

    cities = defaultdict(dict)
    for line in out:
        x = line.split()
        c1,_,c2,_,distance = x
        cities[c1][c2] = int(distance)
        cities[c2][c1] = int(distance)
    return cities

def total_dst(cities,city_list):
    return sum(cities[c1][c2] for c1,c2 in zip(city_list,city_list[1:]))

def calc_distances(cities):
    distances = [total_dst(cities,x) for x in permutations(cities.keys())]
    return distances

def part1(distances):
    return min(distances)

def part2(distances):
    return max(distances)


if __name__ == "__main__":
    timestart = time.time()
    
    puzzle_input = parse()
    # print(puzzle_input)

    dists = calc_distances(puzzle_input)

    print("part 1:",part1(dists))
    print("part 2:",part2(dists))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))

# print("part 1: ", min(distances))
# print("part 2: ", max(distances))


