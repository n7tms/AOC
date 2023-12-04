from collections import defaultdict

DIRECTIONS = [[0,1], [1,0], [0,-1], [-1, 0], [-1,1], [-1,-1], [1,-1], [1,1]]
IN_FILE = "AOC2023/inputs/202303.in"

def number_from_digits(digits: list[str]):
    return int(''.join(digits))

with open(IN_FILE) as f:
    lines = f.readlines()
    gear_ratio_candidates = defaultdict(list) # for symbols '*' at position (x, y) we will keep track of adjacent numbers

    max_x = len(lines[0].strip())
    max_y = len(lines)

    for i in range(max_y):
        digits = []
        adjacent = []

        for j in range(max_x):
            c = lines[i][j]

            # collect digits which form a number
            if c.isdigit():
                digits.append(c)

                # we already know this number is adjacent to a symbol '*'
                if adjacent:
                    continue

                # look for symbols adjacent to a number
                for dx, dy in DIRECTIONS:
                    x, y = j + dx, i + dy

                    # make sure we stay inside the engine schematic
                    if 0 <= x < max_x and 0 <= y < max_y:
                        c = lines[y][x]
                        
                        # look for symbols which is '*'
                        if len(adjacent) == 0 and c == '*':
                            adjacent.append((x, y)) # in part 1 we had a boolean here now we track position of symbol '*'
                            break;
            else:
                if len(adjacent) > 0:
                    part_number = number_from_digits(digits)
                    for xy in adjacent:
                        gear_ratio_candidates[xy].append(part_number)

                digits = []
                adjacent = []
    
        # edge case where number ends with the line
        if len(adjacent) > 0:
            part_number = number_from_digits(digits)
            for xy in adjacent:
                gear_ratio_candidates[xy].append(part_number)

    # calculate and print sum of gear ratios
    print(sum(gears[0] * gears[1] for gears in gear_ratio_candidates.values() if len(gears) == 2))