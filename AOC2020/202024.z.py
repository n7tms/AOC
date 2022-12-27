# AOC 2020 - Day 24
# @jbuji
# tags:  #hex 

with open("AOC2020\\202024.txt") as file:
    lines = file.read().strip().split('\n')

size = 141  # enought          White = False, Black = True
floor = [[False for _ in range(size)] for _ in range(size)]

for l in lines:
    q = r = int(size//2)     # reference tile
    while l:
        if   l[0]   == 'e' : l = l[1:]; q += 1
        elif l[0]   == 'w' : l = l[1:]; q -= 1
        elif l[0:2] == 'ne': l = l[2:]; q += 1; r -= 1
        elif l[0:2] == 'nw': l = l[2:]; r -= 1
        elif l[0:2] == 'se': l = l[2:]; r += 1
        elif l[0:2] == 'sw': l = l[2:]; q -= 1; r += 1
    floor[q][r] = not floor[q][r]     # flip
print('Part One:', str(floor).count('True'))


from copy import deepcopy

for day in range(100):
    foo = deepcopy(floor)
    
    for q in range(3, size-1):      # 3 for puzzle data
        for r in range(3, size-1):  # don't know why
            adjacent = floor[q+1][r] + floor[q+1][r-1] \
                     + floor[q-1][r] + floor[q-1][r+1] \
                     + floor[q][r-1] + floor[q][r+1]
            if floor[q][r]:
               if adjacent == 0 or adjacent > 2:
                  foo[q][r] = False
            else:
               if adjacent == 2:
                  foo[q][r] = True
    floor = foo
print('Part Two:', str(floor).count('True'))