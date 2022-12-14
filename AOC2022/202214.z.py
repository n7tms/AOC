# https://github.com/mattieshoes/aoc2022/blob/main/14.py

IN_FILE = "AOC2022\\202214.txt"
# IN_FILE = "AOC2022\\202214.sample.txt"

def recursive_split(x, *args):
    y = []
    x = x.split(args[0])
    for part in x:
        if len(args) > 1:
            y += [recursive_split(part, *args[1:])]
        else:
            y += [part]
    return y

# returns 1 if the sand comes to rest before the max row
# returns 2 if the sand comes to rest after the max row
# returns 0 if the source location is blocked
def drop_sand():
    if sand_source in rock:
        return 0

    loc = sand_source
    while True:
        # check below
        maybe = (loc[0] + 1, loc[1])
        if maybe not in rock:
            loc = maybe
            continue

        # check below-left
        maybe = (loc[0] + 1, loc[1] - 1)
        if maybe not in rock:
            loc = maybe
            continue
        
        # check below-right
        maybe = (loc[0] + 1, loc[1] + 1)
        if maybe not in rock:
            loc = maybe
            continue

        # came to rest
        rock[loc] = 2
        if loc[0] > max_row:
            return 2
        else:
            return 1

with open(IN_FILE) as f:
    data = recursive_split(f.read().rstrip('\n'), '\n', ' -> ', ',')
    
ans1 = 0
ans2 = 0
rock = {}
max_row = 0
sand_source = (0, 500)

# build rock hash from input
for line in data:
    for idx in range(1, len(line)):
        fr = int(line[idx-1][1])
        fc = int(line[idx-1][0])
        tr = int(line[idx][1])
        tc = int(line[idx][0])
        if fr > max_row:
            max_row = fr
        if tr > max_row:
            max_row = tr
        if fr == tr:    # col varies
            if fc > tc:
                fc, tc = tc, fc
            for i in range(fc, tc+1):
                rock[(fr, i)] = 1
        else:   # row varies
            if fr > tr:
                fr, tr = tr, fr
            for i in range(fr, tr+1):
                rock[(i, fc)] = 1

# build floor for part 2
# as sand can only move down or diagonal, the max deviation in column is about the same as the max height
# so easy enough to just hard code something wide enough.
for c in range(500 - max_row - 10, 500 + max_row + 10):
    rock[(max_row+2, c)] = 1

# part 1 ends when sand first passes the input floors and hits the part-2 floor
while drop_sand() != 2:
    ans1 += 1
print(f"Part 1: {ans1}")

# part 2 ends when sand source is blocked with sand
ans2 += ans1 + 1 # (plus 1 for the one that triggered the end of part 1)
while drop_sand() != 0:
    ans2 += 1 
print(f"Part 2: {ans2}")