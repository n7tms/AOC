# AOC 2017 - Day 19
# tags: #coords

import time

IN_File = "AOC2017/19.txt"

def parse():
    with open(IN_File) as f:
        out = f.read().split('\n')
    return out

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def part1(the_map):    # BPDKCZWHGT, 17728
    passed_letters = []
    dir = [1,0]
    pos = [0,the_map[0].index('|')]
    steps = 0

    # walk the map
    while True:
        steps += 1
        pos = [sum(i) for i in zip(pos,dir)]

        elem = the_map[pos[0]][pos[1]]
        if elem == ' ': break # left the map; done!

        if elem in LETTERS:
            passed_letters.append(elem)
        elif elem == '+':
            # if dir up/do, look for '-' on le/ri
            if dir[1] == 0:
                if the_map[pos[0]][pos[1]-1] == '-' or the_map[pos[0]][pos[1]-1] in LETTERS:
                    dir = [0,-1]
                else:
                    dir = [0,1]
            # if dir le/ri, look for '|' on up/do
            else:
                if the_map[pos[0]-1][pos[1]] == '|' or the_map[pos[0]-1][pos[1]] in LETTERS:
                    dir = [-1,0]
                else:
                    dir = [1,0]

    return ''.join(passed_letters),steps


if __name__ == "__main__":
    timestart = time.time()

    data = parse()

    letters,steps = part1(data)
    print("part 1:",letters)
    print("part 2:",steps)

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))