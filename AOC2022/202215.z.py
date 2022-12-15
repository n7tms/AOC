import sys, fileinput, re, math

IN_FILE = "AOC2022\\202215.txt"
# IN_FILE = "AOC2022\\202215.sample.txt"
with open(IN_FILE) as f:
    out = [line for line in f.read().split('\n')]

i = [ list( map( int, re.findall( "-?\d+", l ) ) ) for l in out]
s = { ( sx, sy, abs( sx - bx ) + abs( sy - by ) ) for sx, sy, bx, by in i }

# Part 1
xl = math.inf
xh = -math.inf
for sx, sy, sc in s:
    dx = sc - abs( 2000000 - sy )
    if dx > 0:
        xl = min( xl, sx - dx )
        xh = max( xh, sx + dx )
print("part1:", xh - xl )

# Part 2
for sx, sy, sc in s:
    for p in range( sc + 1 ):
        for tx, ty in ( ( sx - sc - 1 + p, sy - p ),
                        ( sx + sc + 1 - p, sy - p ),
                        ( sx - sc - 1 + p, sy + p ),
                        ( sx + sc + 1 - p, sy + p ) ):
            if ( 0 <= tx <= 4000000 and
                 0 <= ty <= 4000000 and
                 all( abs( tx - ox ) + abs( ty - oy ) > od
                      for ox, oy, od in s ) ):
                print("part2", tx * 4000000 + ty )