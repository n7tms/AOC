# AOC 20215 - Day 13

import time
from collections import defaultdict
from itertools import permutations

# IN_FILE = "AOC2015/201513.txt"
IN_FILE = "AOC2015/201513.sample.txt"

class Graph:
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)

        # Define the type of a graph
        self.m_directed = directed

        self.m_adj_list = {node: set() for node in self.m_nodes}      

    def add_edge(self, node1, node2, weight=1):
        self.m_adj_list[node1].add((node2, weight))

        if not self.m_directed:
            self.m_adj_list[node2].add((node1, weight))

    def print_adj_list(self):
        for key in self.m_adj_list.keys():
            print("node", key, ": ", self.m_adj_list[key])


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

def optimum_happiness(people, happiness, first_person):
    perms = list(permutations(people))
    perm_happiness = {}
    for perm in perms:
        if perm <= perm[::-1]:
            perm = list(perm)
            perm.insert(0,first_person)

            perm_happiness[tuple(perm)] = compute_happiness(perm,people)

    opt_perm_happy = max(perm_happiness.items(),key=lambda x: x[1])[0]
    return perm_happiness, opt_perm_happy



def parse():
    with open(IN_FILE) as f:
        out = [line for line in f.read().split('\n')]
    
    people = defaultdict(dict)
    for line in out:
        tmp = line[:-1].split()
        person,g_l,hap_units,other_person = tmp[0],tmp[2],tmp[3],tmp[10]
        if g_l == "lose":
            hap_units = int(hap_units) * -1
        else:
            hap_units = int(hap_units)
        people[person][other_person] = hap_units

    return people


def part1(data):
    people = set(data.keys())
    first_person = people.pop()
    opt_hap, x = optimum_happiness(data,people,first_person)
    return opt_hap



def part2(data):
    pass


if __name__ == "__main__":
    timestart = time.time()
    
    puzzle_input = parse()
    print(puzzle_input)


    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))




