# AOC 2022 - Day 9

IN_FILE = "AOC2022/202209.txt"
# IN_FILE = "AOC2022\\202209.sample.txt"

def get_input(afile):
    with open(afile, "r") as ifile:
        out = [f.strip() for f in ifile.readlines()]
    return out

def calc_tail(instructions,knots):
    moves = {"R":(1,0), "L":(-1,0), "U":(0,1), "D":(0,-1)}    
    positions, known_positions = {f:[0,0] for f in range(10)}, set()
    for command in instructions:
        com, param = command.split(" ")
        vector = moves[com]
        for rep in range(int(param)):
            positions[0][0]+=vector[0]
            positions[0][1]+= vector[1]
            for knot in range(1,10):
                adj_fn = int if (dst := abs((x_diff := positions[knot-1][0] - positions[knot][0])) + abs(y_diff := positions[knot-1][1] - positions[knot][1])) < 3 else lambda x: round(x + ((md := (min((x_diff, y_diff), key=abs)))/abs(md if md != 0 else 1))*0.1)
                positions[knot][0] += adj_fn((positions[knot-1][0] - positions[knot][0]) / 2)
                positions[knot][1] += adj_fn((positions[knot-1][1] - positions[knot][1]) / 2)
            known_positions.add(tuple(positions[knots]))
    return known_positions

def part1():
    instrs = get_input(IN_FILE)
    print("part 1: {}".format(len(calc_tail(instrs, 1))))

def part2():
    instrs = get_input(IN_FILE)
    print("part 2: {}".format(len(calc_tail(instrs, 9))))



part1()
part2()