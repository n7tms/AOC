# AOC 2015 - Day 5

import time

IN_FILE = "AOC2015\\201506.txt"
# IN_FILE = "AOC2015\\201506.sample.txt"


def get_directions(line):
    words = line.split(' ')
    if words[0] == 'toggle':
        a,b = words[1].split(',')
        c,d = words[3].split(',')
        parsed = [words[0],a,b,c,d]
    else:
        a,b = words[2].split(',')
        c,d = words[4].split(',')
        parsed = [words[1],a,b,c,d]
    return parsed

def parse():
    """Parse input."""
    # pi = [line for line in puzzle_input.split("\n")]
    out = list()
    with open(IN_FILE) as f:
    #     out = [(line) for line in f.read().split('\n')]
    # return out

        for line in f.read().split('\n'):
            out.append(get_directions(line))
    return out
 

def toggle(range_of_lights, lights):
    xs,ys,xe,ye = map(int,range_of_lights)
    for x in range (xs,xe+1):
        for y in range(ys,ye+1):
            if lights[x][y] == 1:
                lights[x][y] = 0
            else: 
                lights[x][y] = 1
    return lights

def turn(on_off, range_of_lights, lights):
    xs,ys,xe,ye = map(int,range_of_lights)
    for x in range (xs,xe+1):
        for y in range(ys,ye+1):
            lights[x][y] = on_off
    return lights

def part1(data):            # => 543903
    """Solve part 1."""
    lights = [[0] * 1000 for _ in range(1000)]
    # lights = [[0] * 10 for _ in range(10)]
    
    for cmd in data:
        # print(cmd)
        if cmd[0] == 'toggle':
            lights = toggle(cmd[1:],lights)
        else:
            lights = turn(1,cmd[1:],lights) if cmd[0] == 'on' else turn(0,cmd[1:],lights)
    
    return sum(on.count(1) for on in lights)


def toggle2(range_of_lights, lights):
    xs,ys,xe,ye = map(int,range_of_lights)
    for x in range (xs,xe+1):
        for y in range(ys,ye+1):
            lights[x][y] += 2
    return lights

def turn2(on_off, range_of_lights, lights):
    xs,ys,xe,ye = map(int,range_of_lights)
    for x in range (xs,xe+1):
        for y in range(ys,ye+1):
            if (lights[x][y] > 0 and on_off == -1) or on_off == 1:
                lights[x][y] += on_off
    return lights

def total_on(data):
    total = 0
    for j in range(len(data)):
        if type(data[j]) == list :
            total+= total_on(data[j])
        else:
            total += data[j]  
    return total

def part2(data):            # => 14687245
    """Solve part 2."""
    lights = [[0] * 1000 for _ in range(1000)]
    # lights = [[0] * 10 for _ in range(10)]
    
    for cmd in data:
        # print(cmd)
        if cmd[0] == 'toggle':
            lights = toggle2(cmd[1:],lights)
        else:
            lights = turn2(1,cmd[1:],lights) if cmd[0] == 'on' else turn2(-1,cmd[1:],lights)
    # print(lights)
    return total_on(lights)



if __name__ == "__main__":
    timestart = time.time()
    
    puzzle_input = parse()
    # print(puzzle_input)
    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))
