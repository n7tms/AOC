# AOC 2017 - Day 25
# tags: #

import time
from collections import deque

IN_File = "AOC2017/25.txt"

def parse():
    instr = {}
    instr['begin'] = 'A'
    instr['steps'] = 12683008

    instr['A'] = {0:[1,'right','B'], 1:[0,'left','B']}
    instr['B'] = {0:[1,'left','C'], 1:[0,'right','E']}
    instr['C'] = {0:[1,'right','E'], 1:[0,'left','D']}
    instr['D'] = {0:[1,'left','A'], 1:[1,'left','A']}
    instr['E'] = {0:[0,'right','A'], 1:[0,'right','F']}
    instr['F'] = {0:[1,'right','E'], 1:[1,'right','A']}

    return instr


def part1(blueprint):    # 3554
    tape = [0] * 1000001
    cursor = len(tape) // 2
    steps = blueprint['steps']
    state = 'A'

    for s in range(steps):
        # get value at cursor
        rval = tape[cursor]

        # get the appropriate value, dir, and next_state from blueprint
        wval,dir,next_state = blueprint[state][rval]
        
        # execute
        tape[cursor] = wval
        if dir == 'right':
            cursor += 1
        else:
            cursor -= 1
        state = next_state

        if cursor < 0 or cursor > len(tape):
            print(f"Tape too small {cursor}")
            break

    checksum = sum(tape)
    return checksum



if __name__ == "__main__":
    timestart = time.time()

    blueprint = parse()

    print("part 1:",part1(blueprint))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))