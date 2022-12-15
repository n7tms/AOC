# AOC 2022 - Day 13

import time

IN_FILE = "AOC2022\\inputs\\202213.txt"
# IN_FILE = "AOC2022\\inputs\\202213.sample.txt"

def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        # out = [line for line in f.read().split('\n\n')]
        # out = [line.split() for line in out]
        # final_out = [[eval(x),eval(y)] for x,y in out]
        final_out = [[eval(x),eval(y)] for x,y in [line.split() for line in [line for line in f.read().split('\n\n')]]]
    return final_out

def compare_pairs(x,y):
    # both values are integers
    if isinstance(x,int) and isinstance(y,int):
        if x == y:
            return 0 # indeterminate
        elif x < y:
            return 1 # correct order
        else:
            return -1 # wrong order

    # both values are lists
    if isinstance(x,list) and isinstance(y,list):
        for a,b in zip(x,y):
            c = compare_pairs(a,b) 
            if c == 0:
                continue
            else:
                return c
        if len(x) < len(y):
            return 1
        elif len(x) > len(y):
            return -1
        else:
            return 0

    # one value is an integer
    if isinstance(x,int) and isinstance(y,list):
        return compare_pairs([x],y)
    elif isinstance(x,list) and isinstance(y,int):
        return compare_pairs(x,[y])
    else:
        return 0


def part1(data):            # => 5013
    """Solve part 1."""
    cnt = 0
    for idx,pairs in enumerate(data,start=1):
        if compare_pairs(pairs[0],pairs[1]) == 1: cnt += idx
    return cnt


def part2(data):            # => 25038
    """Solve part 2."""
    # turn the data into one big list of lists (rather than pairs of lists)
    one_list = [item for sublist in data for item in sublist]
    one_list.append([[2]])
    one_list.append([[6]])

    # perform a bubble sort
    sorted = False
    while not sorted:
        sorted = True
        for idx in range(len(one_list)-1):
            p1,p2 = one_list[idx],one_list[idx+1]
            c = compare_pairs(p1,p2)
            if c != 1:
                one_list[idx], one_list[idx+1] = one_list[idx+1], one_list[idx]
                sorted = False

    # index of [[2]]
    idx2 = one_list.index([[2]])+1
    # index of [[6]]
    idx6 = one_list.index([[6]])+1
    
    return idx2 * idx6

if __name__ == "__main__":
    timestart = time.time()

    puzzle_input = parse()
    # print(puzzle_input)

    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))