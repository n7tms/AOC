# AOC 2024 day 07: 
#

import aoc_utils as aoc
import time
import os
import itertools

DAY = '07'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")


def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip()
    data = data.splitlines()

    # calibrations = []
    # for d in data:
    #     total, value = d.split(':')
    #     values = value.strip().split(' ')
    #     values = list(map(int,values))
    #     calibrations.append([int(total),values])
    
    calibrations = [ [int(total), list(map(int, value.strip().split()))] for total, value in (d.split(':') for d in data)]


    return calibrations


def do_calc(terms,ops):
    result = terms[0]
    for term,op in (zip(terms[1:], ops)):
        if op == '+':
            result += term
        if op == '*':
            result *= term
        if op == "||":
            result = int(str(result) + str(term))
    return result


def part1(calibrations):        # => 1260333054159

    answer = 0
    for ans,terms in calibrations:
        ops = list(itertools.product(['+','*'],repeat=len(terms) -1))

        # this block with the do_calc subroutine, took about .2 seconds
        for cbo in ops:
            if do_calc(terms,cbo) == ans:
                answer += ans
                break

        # This code took over 4 seconds to execute
        # # build an expression
        # for exp in ops:
        #     expression = f"{terms[0]}"
        #     for i, op in enumerate(exp):
        #         expression += f"{op}{terms[i+1]}"
        #         expression = str(eval(expression))
            
        #     if int(expression) == ans:
        #         answer += ans
        #         break
    return answer

def part2(calibrations):       # => 162042343638683
    answer = 0

    for ans,terms in calibrations:
        ops = list(itertools.product(['+','*','||'],repeat=len(terms) -1))

        # This optimized code took only 17 seconds
        for cbo in ops:
            if do_calc(terms,cbo) == ans:
                answer += ans
                break

        # this original brute force solution took 11 minutes to solve, but it worked.
        # the eval() and string manipulation are expensive!
        # # build an expression
        # for exp in ops:
        #     expression = f"{terms[0]}"
        #     for i, op in enumerate(exp):
        #         expression += f"{op}{terms[i+1]}"
        #         expression = str(eval(expression))
                
        #     if int(expression) == ans:
        #         answer += ans
        #         break
    return answer

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(data))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(data))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        