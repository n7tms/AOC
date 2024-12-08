# AOC 2018 day 09: 
#

import aoc_utils as aoc
import time
import os
import re
from itertools import cycle
from collections import deque


DAY = '09'
IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".sample.txt")

def parse():
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



def part1(players, points):        # => 390592
    
    # initialize scores
    scores = {}
    for p in range(players):
        scores[p] = 0

    game = [0]
    current_idx = 0

    round = 0
    for player, score in cycle(scores.items()):
        round += 1
        if round % 23 == 0:
            #do something special
            scores[player] += round
            removal = current_idx - 7
            if removal < 0:
                removal = len(game) - abs(current_idx-7)
            current_idx = removal
            scores[player] += game[current_idx]
            game.pop(current_idx)
        else:
            current_idx += 1
            current_idx = current_idx % len(game) + 1
            game.insert(current_idx, round)

        if round == points:
            return max(scores.values())

    return score


def part2(players, points):        # => 3277920293
    # initial part2 brute force took 7390 seconds (see part 1)
    # Optimized version with rotating deque took 0.77 seconds!

    # Initialize scores
    scores = {p: 0 for p in range(players)}

    # Use deque for efficient circular operations
    game = deque([0])
    
    for round in range(1, points + 1):
        if round % 23 == 0:
            # Special scoring rule
            current_player = (round - 1) % players
            game.rotate(7)  # Move 7 steps counter-clockwise
            scores[current_player] += round + game.pop()
            game.rotate(-1)  # Adjust to the new current marble
        else:
            game.rotate(-1)  # Move 1 step clockwise
            game.append(round)  # Insert the new marble

    return max(scores.values())


def solve():
    """Solve the puzzle for the given input."""
    plyrs, pnts = parse()

    start_time = time.time()
    p1 = str(part2(plyrs, pnts))
    # p1 = str(part1(13, 7999))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(plyrs, pnts*100))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve()

