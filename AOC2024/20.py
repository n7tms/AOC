# AOC 2024 day 20: 
#

import aoc_utils as aoc
import time
import os

DAY = '20'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()
    
    walls = []
    track = []
    start = ()
    exit = ()
    for r,line in enumerate(data):
        for c,ch in enumerate(line):
            if ch == '#': 
                walls.append((r,c))
            elif ch == '.':
                track.append((r,c))
            elif ch == 'S':
                start = (r,c)
                track.append((r,c))
            elif ch == 'E':
                exit = (r,c)
                track.append((r,c))

    return walls, track, start, exit


def part1(walls: list, track: list, start: tuple, exit: tuple):        # => 
    base_case = len(aoc.bfs_shortest_path(track, start, exit)) - 1

    less100 = 0
    # for wall in walls:
    #     track.append(wall)
    #     speed = len(aoc.bfs_shortest_path(track, start, exit)) - 1
    #     if speed > base_case: continue
    #     if speed < base_case-100:
    #         less100 += 1
    #     track.remove(wall)

    # Find the distance to the end from every point on the track; store in dict = {(r,c):distance}
    # Start at start
    #   compare current pos with every pos 2 picoseconds away. 
    #   if current_pos_distance - cheat_pos_distance < 100, we found a cheat


    all_distances = dict()
    for current_pos in track:
        all_distances[current_pos] = len(aoc.bfs_shortest_path(track,current_pos,exit)) - 1
    
    DIRS = [(-2,0),(0,2),(2,0),(0,-2)]
    less100 = 0
    for cur_pos in track:
        for dr,dc in DIRS:
            testr, testc = cur_pos[0] - dr, cur_pos[1] - dc
            if (testr,testc) in track and all_distances[(testr,testc)] < all_distances[cur_pos] and all_distances[cur_pos]-all_distances[(testr,testc)]>100:
                less100 += 1



    return less100


def part2(data):       # => 
    return    


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    w, t, s, e = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(w, t, s, e))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(w, t, s, e))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        