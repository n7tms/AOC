# AOC 2022 - Day 7

import time

# IN_FILE = "AOC2022\\202207.txt"
IN_FILE = "AOC2022\\202207.sample.txt"
# directory = {'a':{'e':{'i':584},'f':29116,'g':2557,'h.lst':62596},'b':14848514,'c':8504156,'d':{'j':406,'d.log':803}}
directory = {}
commands = None
idx = [0]


def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        out = [(line) for line in f.read().split('\n')]
    return out


def get_line():
    return commands[idx[0]].split()

def sub_dir(sd):
    idx[0] += 1
    line = get_line()
    if line[0] == '$':
        return sd
    if line[0] == 'dir':
        sd[line[1]] = {}
    else:
        sd[line[1]] = int(line[0])
    return sub_dir(sd)

def execute_cmd(cur_dir):
    if idx[0] == len(commands):
        return cur_dir
    
    line = get_line()
    if line[0] == '$':  # command prompt
        if line[1] == 'cd':
            if line[2] == '..':
                return cur_dir  # backup
            else:
                idx[0] += 1
                cur_dir[line[2]] = execute_cmd(cur_dir[line[2]]) # change directory
        elif line[1] == 'ls':
            cur_dir = sub_dir(cur_dir)
    # idx[0] -= 1
    return execute_cmd(cur_dir)

def sum_dirs(max_size):
    pass

def part1(data):            # => 
    """Solve part 1."""
    idx[0] = 1
    directory = execute_cmd({}) # start with the second command
    # return sum_dirs(100000)
    return directory



    for cmd in data[1:]:  # skip the first command "cd /"
        if cmd == '$ ls':
            pass







def part2(data):            # => 
    """Solve part 2."""
    

if __name__ == "__main__":
    timestart = time.time()
    
    puzzle_input = parse()
    commands = puzzle_input.copy()

    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))
