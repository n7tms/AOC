# AOC 2024 day 04: 
#

import aoc_utils as aoc
import time
import os

DAY = '04'
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

    # although the test data worked, the puzzle data kept producing the wrong answer.
    # someone on reddit suggested padding the puzzle data

    # Determine the width of the padded lines
    padding_width = 3
    line_length = len(data[0]) + padding_width * 2
    
    # Create the top and bottom padding lines
    padding_line = '.' * line_length
    
    # Add padding to each line
    padded_data = [padding_line, padding_line, padding_line]
    padded_data += ['.' * padding_width + line + '.' * padding_width for line in data]
    padded_data += [padding_line, padding_line, padding_line]
    
    return padded_data

def find_word1(ws, word,row,col):
    #                L        R       U       D        UR       UL       DR      DL
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, 1), (-1, -1), (1, 1), (1, -1)]
    
    found = 0
    word_length = len(word)
    max_rows = len(ws)
    max_cols = len(ws[0])
    
    for dr, dc in directions:
        chars = ''
        for step in range(word_length):
            r, c = row + dr * step, col + dc * step
            if 0 <= r < max_rows and 0 <= c < max_cols:
                chars += ws[r][c]
            else:
                break  # Stop if out of bounds; shouldn't happen w/ padding
        if chars == word:
            found += 1
    
    return found


def find_word2(ws,r,c):
    # searching for MAS in an X formation
    # the A is located at (r,c)
    
    #                 UL       DR       UR      DL
    directions = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
    
    # Extract the characters at these positions
    chars = [ws[r + dr][c + dc] for dr, dc in directions]

    # test for the X formation
    found = int((chars[0] in 'MS' and chars[1] in 'MS' and
                 chars[2] in 'MS' and chars[3] in 'MS' and
                 {chars[0], chars[1]} == {'M', 'S'} and
                 {chars[2], chars[3]} == {'M', 'S'}))
    
    return found



def part1(wordsearch):        # => 2646
    found = 0
    for r in range(len(wordsearch)):
        for c in range(len(wordsearch[0])):
            if wordsearch[r][c] == "X":
                found += find_word1(wordsearch,'XMAS',r,c)

    return found


def part2(wordsearch):       # => 2000
    found = 0
    for r in range(len(wordsearch)):
        for c in range(len(wordsearch[0])):
            if wordsearch[r][c] == "A":
                found += find_word2(wordsearch,r,c)

    return found


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
        