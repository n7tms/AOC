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