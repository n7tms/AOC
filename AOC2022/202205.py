# AOC 2022 - Day 5

import time

IN_FILE = "AOC2022/202205.txt"
# IN_FILE = "AOC2022/202205.sample.txt"

#     [P]                 [Q]     [T]
# [F] [N]             [P] [L]     [M]
# [H] [T] [H]         [M] [H]     [Z]
# [M] [C] [P]     [Q] [R] [C]     [J]
# [T] [J] [M] [F] [L] [G] [R]     [Q]
# [V] [G] [D] [V] [G] [D] [N] [W] [L]
# [L] [Q] [S] [B] [H] [B] [M] [L] [D]
# [D] [H] [R] [L] [N] [W] [G] [C] [R]
#  1   2   3   4   5   6   7   8   9 


def separate(line):
    # move 1 from 7 to 6
    line = line.replace("move","").replace("from","").replace("to","")
    a,b,c = line.split()
    return list(map(int,[a,b,c]))

def parse_crates(raw):
    crates = [list() for x in raw[-1] if x.isdigit()] 
    # print(drawing)

    for line in raw[:-1]:
        for i, v in enumerate(line): 
            if v.isalpha(): 
                crates[int(raw[-1][i]) - 1].insert(0, v)
    out = ["".join(crate) for crate in crates]
    out.insert(0,'')
    return out

def parse():
    """Parse input."""
    # pi = [line for line in puzzle_input.split("\n")]
    with open(IN_FILE) as f:
        stacks, out = [x.split("\n") for x in f.read().split("\n\n")]
        out = [separate(x) for x in out]
    return parse_crates(stacks),out


def part1(stacks,directions):            # => HNSNMTLHQ
    """Solve part 1."""
    # stacks = ["","DLVTMHF","HQGJCTNP","RSDMPH","LBVF","NHGLQ","WBDGRMP","GMNRCHLQ","CLW","RDLQJZMT"]

    for dir in directions:
        qty,src,des = dir
        for i in range(qty):
            stacks[des] = "".join([stacks[des],stacks[src][-1:]])
            stacks[src] = stacks[src][:-1]
    
    return "".join([x[-1:] for x in stacks])


def part2(stacks,directions):            # => RNLFDJMCT
    """Solve part 2."""
    # stacks = ["","DLVTMHF","HQGJCTNP","RSDMPH","LBVF","NHGLQ","WBDGRMP","GMNRCHLQ","CLW","RDLQJZMT"]

    for dir in directions:
        qty,src,des = dir
        stacks[des] = "".join([stacks[des],stacks[src][-qty:]])
        stacks[src] = stacks[src][:-qty]
   
    return "".join([x[-1:] for x in stacks])


if __name__ == "__main__":
    timestart = time.time()
    
    stacks,puzzle_input = parse()
    stacks2 = stacks.copy()
    print("part 1:",part1(stacks,puzzle_input))
    print("part 2:",part2(stacks2,puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))
