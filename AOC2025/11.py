# AOC 2025 day 11: 
#


import time
import os
from collections import defaultdict

DAY = '11'
# IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+"-sample.txt")
IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+".in")

def parse(puzzle_input):
    """
    Parse
    """
    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()

    wiring = defaultdict()
    for line in data:
        node, neighbors = line.split(":",1)
        node = node.strip()
        neighbors = neighbors.strip().split()
        wiring[node] = neighbors
        
    return wiring


def find_all_paths(wiring, start, target, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    path.append(start)
    visited.add(start)

    if start == target:
        yield list(path)
    else:
        for neighbor in wiring.get(start, []):
            yield from find_all_paths(wiring, neighbor, target, path, visited)
    
    path.pop()
    visited.remove(start)


def part1(x):        # => 683
    start_node = "you"
    target_node = "out"

    paths = list(find_all_paths(x, start_node, target_node))

    return len(paths)


def part2(x):        # => 
    start_node = "svr"
    target_node = "out"
    node1 = "dac"
    node2 = "fft"
    
    # results = []

    # for path1 in find_all_paths(x, start_node, node1):
    #     for path2 in find_all_paths(x, node1, node2):
    #         for path3 in find_all_paths(x, node2, target_node):
    #             full_path = path1[:1] + path2[:-1] + path3
    #             results.append(full_path)

    # for path1 in find_all_paths(x, start_node, node2):
    #     for path2 in find_all_paths(x, node1, node2):
    #         for path3 in find_all_paths(x, node1, target_node):
    #             full_path = path1[:1] + path2[:-1] + path3
    #             results.append(full_path)
    
    count = 0
    pathsa = list(find_all_paths(x, start_node, node1))
    for mid in find_all_paths(x, node1, node2):
        count += len(pathsa) * len(list(find_all_paths(x, node2, target_node)))
    
    pathsb = list(find_all_paths(x, start_node, node2))
    for mid in find_all_paths(x, node2, node1):
        count += len(pathsb) * len(list(find_all_paths(x, node1, target_node)))

    return count


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    x = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(x))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(x))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve(IN_FILE)
        