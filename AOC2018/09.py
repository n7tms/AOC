# AOC 2018 day 09: 
#

import aoc_utils as aoc
import time
import os
import re
from itertools import cycle


DAY = '09'
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".in")
IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2018,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()

    matches = re.search(r"(\d+) players;.*?(\d+) points", data[0])
    players = int(matches.group(1))
    points = int(matches.group(2))
    
    return players, points



def part1(players, points):        # => 
    
    # initialize scores
    scores = {}
    for p in players:
        scores[p] = 0

    game = [0]
    current_idx = 0

    round = 0
    for player in cycle(players):
        round += 1
        if round % 23 == 0:
            #do something special
            scores[player] += round
            removal = current_idx - 7
            if removal < 0:
                removal = len(game) - abs(current_idx-7)
        else:
            current_idx += 2
            current_idx = current_idx % len(game) + 1
            game.insert(current_idx, round)






    return score


def part2(data):        # => 
    return

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    plyrs, pnts = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(plyrs, pnts))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(plyrs, pnts))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)

