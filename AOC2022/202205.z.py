# AOC 2022 Day 5
# Code used to parse the initial stack of crates
# https://www.reddit.com/r/adventofcode/comments/zcxid5/2022_day_5_solutions/iyz110o/?context=3

IN_FILE = "AOC2022\\202205.txt"

with open(IN_FILE, 'r') as f:
    lines=f.readlines()
def getStart():
    startLines=lines[:8]
    print(startLines)
    startLines.reverse()
    print()
    print(startLines)

    stacks={}
    s=0
    for c in range(1,len(startLines[0]),4):
        stacks[s]=""
        for l in range(len(startLines)):
            stacks[s]+=startLines[l][c]
        stacks[s]=stacks[s].strip()
        s+=1
    return stacks

print(getStart())



# ==============================================
# Explore this solution
# https://www.reddit.com/r/adventofcode/comments/zcxid5/2022_day_5_solutions/iyz0qpi/?context=3

from aocd import data
from parse import parse

crates, instructions = data.split("\n\n")
cols0 = {}
for *row, last in zip(*crates.split("\n")):
    if last.isdigit():
        cols0[int(last)] = "".join(x for x in row if x.isupper())

moves = []
for line in instructions.splitlines():
    n, p0, p1 = parse("move {:d} from {:d} to {:d}", line).fixed
    moves.append((n, p0, p1))

for part in "ab":
    step = -1 if part == "a" else None
    cols = cols0.copy()
    for n, p0, p1 in moves:
        cols[p1] = cols[p0][:n][::step] + cols[p1]
        cols[p0] = cols[p0][n:]
    result = "".join([v0 for v0, *_ in cols.values()])
    print(f"part {part}:", result)