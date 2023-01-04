# AOC 2017 - Day 12
# tags: #sets

import time
from collections import defaultdict

IN_File = "AOC2017/12.txt"

edges = set()
node_map = defaultdict(set)

def parse():
    with open(IN_File) as f:
        out = f.read().split('\n')
    
    for line in out:
        nodes = line.strip().split('<->')
        for node in nodes[1].strip().split(','):
            edges.add((int(nodes[0]),int(node)))

    return

zero_connects = []

def count_conns(node):
    for x in node:
        if x in zero_connects:
            continue
        else:
            zero_connects.append(x)
            count_conns(node_map[x])
    return

def part1(data):    # 115

    for x,y in edges:
        node_map[x].add(y)
        node_map[y].add(x)

    count_conns(node_map[0])

    return len(zero_connects)

def part2(data):    # 221
    groups = 1

    for n in range(1,2000):
        if n in zero_connects:
            continue
        else:
            groups += 1
            count_conns(node_map[n])
    return groups



if __name__ == "__main__":
    timestart = time.time()

    data = parse()

    print("part 1:",part1(data))
    print("part 2:",part2(data))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))