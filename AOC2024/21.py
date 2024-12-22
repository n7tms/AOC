# AOC 2024 day 21: 
#

import aoc_utils as aoc
import time
import os
import aoc_utils as aoc

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

doorpad = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(3,1),(3,2)]
doorpadchars = {'7':(0,0), '8':(0,1), '9':(0,2),
                '4':(1,0), '5':(1,1), '6':(1,2),
                '1':(2,0), '2':(2,1), '3':(2,2),
                '0':(3,1), 'A':(3,2)}

dirpad = [(0,1),(0,2),(1,0),(1,1),(1,2)]
dirpadchars = {'^':(0,1), 'A':(0,2),
               '<':(1,0), 'v':(1,1), '>':(1,2)}




def path_to_arrows(path: list) -> str:
    arrows = ''
    for i, (r,c) in enumerate(path[1:],1):
        if path[i-1][0] == r and path[i-1][1] > c: arrows += '<'
        elif path[i-1][0] == r and path[i-1][1] < c: arrows += '>'
        elif path[i-1][0] > r and path[i-1][1] == c: arrows += '^'
        elif path[i-1][0] < r and path[i-1][1] == c: arrows += 'v'
    
    arrows += "A"
    return arrows


curpos1 = (3,2)
curpos2 = (0,2)
curpos3 = (0,2)

# the robot pressing the keypad on the door
def robot1(sequence: str): 
    global curpos1
    seq1 = []
    for s in sequence:
        # sq = aoc.bfs_shortest_path(doorpad,curpos1,doorpadchars[s])
        sq = aoc.bfs_all_paths(doorpad,curpos1,doorpadchars[s])
        pth = ''
        for s1 in sq:
            pth += path_to_arrows(s1)
        seq1.append(pth)
        curpos1 = doorpadchars[s]

    return seq1
    
    

# the robot pressing the keypad on robot1 
def robot2(sequence: str):
    global curpos2
    seq2 = ''
    for s in sequence:
        sq = aoc.bfs_shortest_path(dirpad,curpos2,dirpadchars[s])
        seq2 += path_to_arrows(sq)
        curpos2 = dirpadchars[s]

    return seq2

# the robot pressing the keypad on robot2
def robot3(sequence: str):
    global curpos3
    seq3 = ''
    for s in sequence:
        sq = aoc.bfs_shortest_path(dirpad,curpos3,dirpadchars[s])
        seq3 += path_to_arrows(sq)
        curpos3 = dirpadchars[s]

    return seq3


######################################################################################################
# TODO
# I need to get all the paths from each seq and see which combination of the paths is the shortest.
# Right now, the "shortest" total path is two characters longer, but there must be an intermmediate
# path in seq1 that makes seq2 shorter....or a path in seq2 that makes seq3 shorter.
######################################################################################################


def part1(data):        # => 
    # iterate through the list of sequences
    #   pass the original sequence to robot1, and return seq1
    #   pass seq1 to robot23, and return seq2
    #   pass seq2 to robot23, and return seq3
    #   pass seq3 to human and return seq4
    # x = len(seq4) * numerical part of original sequence
    # add all the x's together and return answer

    complexity = 0 
    for sequence in data:
        seq1 = robot1(sequence)
        print(seq1)
        seq2 = robot2(seq1)
        print(seq2)
        seq3 = robot3(seq2)
        print(seq3)
        # seq4 = robot23(seq3)
        print(f'{sequence}: {len(seq3)} * {int(sequence.partition('A')[0])}   =>  {seq3}')
        complexity += (len(seq3) * int(sequence.partition('A')[0]) )

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
        