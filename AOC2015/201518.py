# --- Day 18:  ---

import time

# IN_FILE = "AOC2015/201518.txt"
IN_FILE = "AOC2015/201518.sample.txt"

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


def part1(data):    # => 
    working = list(data)
    for r in range(len(data)):
        for c in range(len(data[0])):
            # how many adjacent lights?
            adj_on = adj_ons(data,r,c)
            if data[r][c] == '#' and (adj_on == 2 or adj_on == 3):
                # leave light on
                pass
            elif data[r][c] == '.' and adj_on == 3:
                # turn light on
                pass
            else:
                # toggle the light
                if data[r][c] == '#':
                    working[r][c] == '.'
                else:
                    working[r][c] == '#'
    data = list(working)
    print(working)

    final_on_count = 0
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == '#':
                final_on_count += 1

    return final_on_count

def part2(data):    # => 
    return 0


if __name__ == "__main__":
    timestart = time.time()

    puzzle_input = parse()

    print("\nDay 18: ===========================")
    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", f"{timeend-timestart:0.4f}", "\n")


