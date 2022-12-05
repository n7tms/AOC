# AOC 2015 - Day 5

import time

# IN_FILE = "AOC2015\\201506.txt"
IN_FILE = "AOC2015\\201506.sample.txt"


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

def part1(data):            # => 238
    """Solve part 1."""
    lights = [[0] * 1000 for _ in range(1000)]

def part2(data):            # => 69
    """Solve part 2."""



if __name__ == "__main__":
    timestart = time.time()
    
    puzzle_input = parse()
    print(puzzle_input)
    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))
