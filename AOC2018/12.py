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
    
    is0 = [c for c in data[0].split(': ')[1]]
    # initial_state = []
    # for inum, ival in enumerate(is0):
    #     if ival == '#':
    #         initial_state.append[inum]

    initial_state = [inum for inum,ival in enumerate(is0) if ival=='#']

    ins_temp = data[1].splitlines()
    instructions = {}
    for inst in ins_temp:
        pattern, result = inst.split(' => ')
        instructions[pattern] = result

    return initial_state, instructions


# I got this idea (but not the code) from reddit.
# store the pot numbers, rather than a visual representation of the empty and full pots -- just the pots with plants.
# using the pattern list comprehension, construct the hash and period pattern looks like around that number.
# compare that pattern to the instruction dictionary.
# if the instruction is present, add the result (from the dictionary) to a temporary list containing the new plants/structure.
# worked like a charm!!!

def part1(instructions, initial_state, generations):        # => 3221   (>1309, not 2939, not 1340)
    final_sum = 0
    
    final_state = initial_state.copy()
    for gen in range(generations):
        prev_sum = final_sum
        temp_state = []

        cur_plant = min(final_state) - 2
        max_plant = max(final_state) + 2
        while cur_plant < max_plant:
            pattern = ''.join(['#' if cur_plant + offset in final_state else '.' for offset in range(-2,3)])
            if pattern in instructions and instructions[pattern] == '#':
                temp_state.append(cur_plant)
            cur_plant += 1
        final_state = temp_state.copy()

        final_sum = sum(final_state)    
        # print(f'{gen}: {sum(final_state)}  (diff {final_sum-prev_sum})')

    return final_sum


def part2(instructions, initial_state):        # => 2600000001872
    # a little bit of manual intervention here.
    # at 129 generations, the sum increases by 52 in EVERY generation.
    # So, (50000000000 - 129) * 52 = 2599999993292
    # that plus the 8580 that was the sum so far gives us 2600000001872
    return 2600000001872

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    initstat,instr = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(instr, initstat, 20))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    # p2 = str(part1(instr, initstat, 50000000000))
    p2 = str(part2(instr, initstat))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)

