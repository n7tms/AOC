# AOC 2023 day 13
# from Jonathan Paulson
# https://www.youtube.com/watch?v=KObhCimyl2I

import os

# IN_FILE = os.path.join("AOC2023","inputs","202313.sample.txt")
IN_FILE = os.path.join("AOC2023","inputs","202313.in")
D = open(IN_FILE).read().strip()
L = D.split('\n')
G = [[c for c in row] for row in L]

for part2 in [False, True]:
    ans = 0
    for grid in D.split('\n\n'):
        G = [[c for c in row] for row in grid.split('\n')]
        R = len(G)
        C = len(G[0])

        # vertical reflection
        for c in range(C-1):
            # ok = True # part 1

            # for part2, instead of ok, check for how many mirrors are different.
            # if there is exactly one difference, then this is the new reflection point.
            badness = 0 # part 2


            # iterate down the reflection point comparing characters on the left and right.
            # expand outward in both directions (dc)
            # if no difference is found, ok will remain True.
            for dc in range(C):
                left = c-dc
                right = c+1+dc
                if 0<=left<right<C:
                    for r in range(R):
                        if G[r][left] != G[r][right]:
                            # ok = False # part 1
                            badness += 1 # part 2
            # if ok is still True, then there is a reflection point here (at c+1)
            # if ok: # part 1
            # if badness == 1: # part 2
            if badness == (1 if part2 else 0):
                # print('vert', c+1)
                ans += c+1
        
        # horizontal reflection
        for r in range(R-1):
            # ok = True # part 1
            badness = 0 # part 2
            # iterate across the reflection point comparing characters above (up) and below (down)
            # expand outward (up and down in both directions) (dr)
            # again, if no difference is found, ok will remain True.
            for dr in range(R):
                up = r-dr
                down = r+1+dr
                if 0<=up<down<R:
                    for c in range(C):
                        if G[up][c] != G[down][c]:
                            # ok = False # part 1
                            badness += 1 # part 2
            # if ok is still True, there is a reflection oint here (at r+1)
            # if ok: # part 1
            # if badness == 1: # part 2
            if badness == (1 if part2 else 0):
                # print('HOR', r+1)
                ans += 100*(r+1)
    print(ans)

