# --- Day 18:  ---

# This is VERY sloppy and slow. I could not get a copy of the initial list without creating a reference.
# Even using list.copy(), it still created a reference.
# I ended up creating a new list to keep track of which lights needed to change.
# Then iterating through that list and toggling the lights in the original list that need to change.
# The result is O(3n^2) -- which lights need to change; change the lights; count the on lights.
# ...and do that twice -- part 1 and part 2. The resulting execution time is bout 24 seconds. TOO LONG!


import time

IN_FILE = "AOC2015/201518.txt"
# IN_FILE = "AOC2015/201518.sample.txt"

def parse():
    with open(IN_FILE) as f:
        out = [line for line in f.read().split('\n')]

    out = list(list(x) for x in out)
    return out


def adj_ons(grid,row,col):
    adjacents = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

    new_coords = []
    for x in adjacents:
        new_coords.append([x[0]+row,x[1]+col])

    on_count = 0
    for r,c in new_coords:
        if r < 0 or c < 0 or r > len(grid)-1 or c > len(grid[0])-1:
            pass
        else:
            if grid[r][c] == '#':
                on_count += 1
    
    return on_count


def part1(data,cycles):    # => 821
    gs = len(data) # grid size

    for _ in range(cycles):
        working = [[0 for i in range(gs)] for j in range(gs)]
        for r in range(gs):
            for c in range(gs):
                # how many adjacent lights?
                adj_on = adj_ons(data,r,c)
                if data[r][c] == '#' and not (adj_on == 2 or adj_on == 3):
                    # turn light off
                    working[r][c] = 1
                elif data[r][c] == '.' and adj_on == 3:
                    # turn light on
                    working[r][c] = 1
    
        # toggle the lights that should change
        for r in range(gs):
            for c in range(gs):
                if working[r][c] == 1:
                    if data[r][c] == '#':
                        data[r][c] = '.'
                    else:
                        data[r][c] = '#'

    final_on_count = 0
    for r in range(gs):
        for c in range(gs):
            if data[r][c] == '#':
                final_on_count += 1

    return final_on_count

def part2(data,cycles):    # => 886
    gs = len(data) # grid size
    # turn on the four corners
    data[0][0] = '#'
    data[0][gs-1] = '#'
    data[gs-1][0] = '#'
    data[gs-1][gs-1] = '#'

    for _ in range(cycles):
        working = [[0 for i in range(gs)] for j in range(gs)]
        for r in range(gs):
            for c in range(gs):
                if (r == 0 and c == 0) or (r == gs-1 and c == gs-1) or (r == 0 and c == gs-1) or (r == gs-1 and c == 0):
                    # ignore the corner lights
                    pass
                else:
                    # how many adjacent lights?
                    adj_on = adj_ons(data,r,c)
                    if data[r][c] == '#' and not (adj_on == 2 or adj_on == 3):
                        # turn light off
                        working[r][c] = 1
                    elif data[r][c] == '.' and adj_on == 3:
                        # turn light on
                        working[r][c] = 1
    
        # toggle the lights that should change
        for r in range(gs):
            for c in range(gs):
                if working[r][c] == 1:
                    if data[r][c] == '#':
                        data[r][c] = '.'
                    else:
                        data[r][c] = '#'

    final_on_count = 0
    for r in range(gs):
        for c in range(gs):
            if data[r][c] == '#':
                final_on_count += 1

    return final_on_count


if __name__ == "__main__":
    timestart = time.time()

    puzzle_input = parse()
    puzzle_input2 = parse()

    print("\nDay 18: ===========================")
    print("part 1:",part1(puzzle_input,100))
    print("part 2:",part2(puzzle_input2,100))
    
    timeend = time.time()
    print("Execution time: ", f"{timeend-timestart:0.4f}", "\n")


