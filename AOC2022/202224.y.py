# AOC 2022 - Day 24
# @ 
# https://topaz.github.io/paste/#XQAAAQD3AwAAAAAAAAARiEJHiiMzw3cPM/1Vl+2nx/DqKkM2yi+HUVwAE+CIF9ie0IJIptpEb22HoLICX4T+E68jZJB00/Qfzsw8MI9yThy4szIGR5o1eTtfxGqAXjFJUP/5vfkHVzYEg0YdxnPMM8z3he9tIuzWuPD+vn8NjTHaRTgoT1g4tko4MmBbjp6GQaDrUWuD+eA5p2b5YjXu+5VYvxgFGO0ow/yDbYXfARBKSnwkrZOR64YH5wNI9t4c6kTiDSLTu028PWh3x2bcNfJ9vYTJtQYrYZR0ollUbizkibrugKtkqbplmhbkVFS7ephrj9dDZ1Cl5Vv5VZa70TRJr8/VGJR5bhkkXRhbO0jpW46nYK2i6NZnYbGCMudGzMBIb2lxO/gngAxM45US9yGfNWPWKMFDG+025aPHQV4fGFM2F7+Z/Ryzwf/ms3D99mJX01oBs4OoVivUe2f208oj7BxBdoUsaplljQN9wATiAFn10uYwoNo8MmgPGQ3pBi6TRXSAooHjIdLqVdRa+72zNwuDACMAgAYHCeW6inBGLKEF0djWYK09m4BAYIqHrHcZsuIW3aJSLhExnxtfYB3/zC0oBzlGQ0dpKtYOcafIENiSceTFVL2GmZEyZ+bPFfPlHtH8WSyULJbLJtLFQlrAMOC3k8K9dvAlufaaqmKRQZy6T26k52v8L5ISdbbmL4LHRgUZA2me1kBbBvvajilsZa3/aeCv/DhhBS9/4DeH/+rPM+Q=
W=set()
B=set()
for y, line in enumerate(open("AOC2022\\inputs\\202224.txt")):
    for x, c in enumerate(line):
        if c=='#': W.add((x-1,y-1))
        if c=='>': B.add((x-1,y-1,+1,0))
        if c=='<': B.add((x-1,y-1,-1,0))
        if c=='^': B.add((x-1,y-1,0,-1))
        if c=='v': B.add((x-1,y-1,0,+1))
X = max(x for x,y in W)
Y = max(y for x,y in W)
print(f"maze size: {X}x{Y}, {len(W)} walls, {len(B)} blizzards")
# add some walls on the top and bottom, otherwise the player escapes the maze
W |= { (x,-2) for x in range(-1,3) }
W |= { (x,Y+1) for x in range(X-3,X+2) }
start = (0, -1)
exit = (X-1, Y)

t = 0
q = {start}
goals = [exit, start, exit]
while goals:
    t += 1
    b = {((px+t*dx)%X, (py+t*dy)%Y) for px,py,dx,dy in B}
    n = {(px+dx, py+dy) for dx,dy in ((1,0),(0,1),(-1,0),(0,-1),(0,0)) for px,py in q}
    q = n - b - W
    #print(t, len(q), goals[0])
    if goals[0] in q:
        print(f"goal {goals[0]} reached after {t} steps (queue size: {len(q)})")
        q = {goals.pop(0)}
