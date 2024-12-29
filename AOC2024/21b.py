# AOC 2024 day 21: 
#

import aoc_utils as aoc
import time
import os
import seq21 as ton


DAY = '21'
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()
        
    return data


def robot(sequence,padtype = 'r'):
    pad = ton.mov_movements if padtype == 'r' else ton.num_movements
        
    seq = ''
    curpos = 'A'
    for s in sequence:
        if s != curpos:
            seq += pad[(curpos,s)]
        seq += 'A'
        curpos = s

    return seq


def part1(data):        # => 

    complexity = 0
    for seq in data:
        s1 = robot(seq,'n')
        s2 = robot(s1)
        s3 = robot(s2)
        complex = len(s3) * int(seq.partition('A')[0])
    
        print(f'{seq}: {complex} => {s3}')
        complexity += complex
    return complexity

def part2(data):       # => 
    return    


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
        