# AOC 2018 day 12: 
#

import aoc_utils as aoc
import time
import os


DAY = '12'
IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2018,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().split('\n\n')
    
    initial_state = [c for c in data[0].split(': ')[1]]
    ins_temp = data[1].splitlines()
    instructions = []
    for inst in ins_temp:
        pattern, result = inst.split(' => ')
        instructions.append([pattern, result])

    return initial_state, instructions


#########################################################
# Consider storing just the locations where plants exist
#########################################################

def part1(instructions, initial_state):        # => >1309, not 2939, not 1340
    generations = 20
    initial_len = len(initial_state)
    final_state = initial_state.copy()
    pot = 0


    print(f'0: {''.join(final_state)} (len: {len(final_state)})')
    for gen in range(1,generations+1):
        final_state.insert(0,'.')
        final_state.insert(0,'.')
        # final_state.insert(0,'.')
        # final_state.append('.')
        final_state.append('.')
        final_state.append('.')
        int_state = []

        for pot in range(len(final_state)-2):
            changed = False
            plants = ''.join(final_state[pot:pot+5])
            for i, r in instructions:
                if i == plants:
                    int_state.append(r)
                    changed = True
                    break
            if not changed: int_state.append(final_state[pot+2])

        final_state = int_state.copy()
        print(f'{gen}: {''.join(final_state)} (len: {len(final_state)})')

    final_len = len(final_state)
    # diff_len = (final_len - initial_len)//3
    diff_len = (final_len - initial_len)//2
    final_sum = 0
    for idx, p in enumerate(final_state):
        if p == '#':
            final_sum += (idx-diff_len)
            
    return final_sum


def part2(instructions, initial_state):        # => 
    return

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    initstat,instr = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(instr, initstat))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(instr, initstat))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)

