# https://github.com/drz416/aoc/blob/main/2024/Day21/d21p2.py


import sys
import re
from collections import deque, Counter, defaultdict
from pathlib import Path
from pprint import pprint
from functools import partial, lru_cache
from itertools import product, combinations

# Run with test data    -> python3 -m d#p#
# Run with puzzle data  -> python3 -m d#p# X (any argument)

def main(argv: list[str]):
    # Prep Code
    lines: list[str]

    if len(argv) == 1:
        test_data = """\
780A
539A
341A
189A
682A"""
        lines = test_data.splitlines()
    else:
        data_file = Path.cwd() / "puzzle_data.txt"
        with open(data_file, "r",) as f:
            lines = f.readlines()

    for i, line in enumerate(lines):
        lines[i] = line.strip()

    # Puzzle code
    #----------------------------------------------------------------

    # Setup lookup maps
    codes = lines
    numpad = {
        "A": {"0": ("<A",),
              "1": ("<^<A", "^<<A",),
              "2": ("<^A", "^<A",),
              "3": ("^A",),
              "4": ("<^<^A", "<^^<A", "^<<^A", "^<^<A", "^^<<A",),
              "5": ("<^^A", "^<^A", "^^<A",),
              "6": ("^^A",),
              "7": ("<^<^^A", "<^^<^A", "<^^^<A", "^<<^^A", "^<^<^A", "^<^^<A",
                    "^^<<^A", "^^<^<A", "^^^<<A",),
              "8": ("<^^^A", "^<^^A", "^^<^A", "^^^<A",),
              "9": ("^^^A",)},
        "0": {"0": ("A",),
              "1": ("^<A",),
              "2": ("^A",),
              "3": ("^>A", ">^A",),
              "4": ("^<^A", "^^<A",),
              "5": ("^^A",),
              "6": ("^^>A", "^>^A", ">>^A",),
              "7": ("^<^^A", "^^<^A", "^^^<A",),
              "8": ("^^^A",),
              "9": ("^^^>A", "^^>^A", "^>^^A", ">^^^A",)},
        "1": {"1": ("A",),
              "2": (">A",),
              "3": (">>A",),
              "4": ("^A",),
              "5": ("^>A", ">^A",),
              "6": ("^>>A", ">^>A", ">>^A",),
              "7": ("^^A",),
              "8": ("^^>A", "^>^A", ">>^A",),
              "9": ("^^>>A", "^>^>A", "^>>^A", ">^^>A", ">^>^A", ">>^^A",)},
        "2": {"2": ("A",),
              "3": (">A",),
              "4": ("<^A", "^<A",),
              "5": ("^A",),
              "6": ("^>A", ">^A",),
              "7": ("<^^A", "^<^A", "^^<A",),
              "8": ("^^A",),
              "9": ("^^>A", "^>^A", ">^^A",)},
        "3": {"3": ("A",),
              "4": ("<<^A", "<^<A", "^<<A",),
              "5": ("<^A", "^<A",),
              "6": ("^A",),
              "7": ("<<^^A", "<^<^A", "<^^<A", "^<<^A", "^<^<A", "^^<<A",),
              "8": ("<^^A", "^<^A", "^^<A",),
              "9": ("^^A",)},
        "4": {"4": ("A",),
              "5": (">A",),
              "6": (">>A",),
              "7": ("^A",),
              "8": ("^>A", ">^A",),
              "9": ("^>>A", ">^>A", ">>^A",)},
        "5": {"5": ("A",),
              "6": (">A",),
              "7": ("<^A", "^<A",),
              "8": ("^A",),
              "9": ("^>A", ">^A",)},
        "6": {"6": ("A",),
              "7": ("<<^A", "<^<A", "^<<A",),
              "8": ("<^A", "^<A",),
              "9": ("^A",)},
        "7": {"7": ("A",),
              "8": (">A",),
              "9": (">>A",)},
        "8": {"8": ("A",),
              "9": (">A",)},
        "9": {"9": ("A",),},
    }

    # Start recurseive search with memoization
    robots = 25                 # for part 1 set to 2
    human_at_level = robots + 1
    ans = 0
    for code in codes:
        prev_button = "A"
        final_length = 0
        for next_button in code:
            shortest_sequence = 10 ** 20
            try:
                possible_paths = numpad[prev_button][next_button]
            except KeyError:
                possible_paths = reverse_sequences(numpad[next_button][prev_button])    
            for path in possible_paths:
                shortest_sequence = min(shortest_sequence, find_shortest(path, robot_level=1, human_level=human_at_level))
            final_length += shortest_sequence
            prev_button = next_button

        print(f"{code} {final_length=}")
        ans += final_length * int(code[:-1])

    print(f"Ans: {ans}")
    # ans: 189235298434780

@lru_cache
def reverse_sequences(directions: tuple[str]) -> tuple[str]:
    reversal_map = {
        "^": "v",
        ">": "<",
        "v": "^",
        "<": ">",
    }
    
    reversed_possibilities = tuple()
    for direction in directions:
        rev = ""
        for c in direction[-2::-1]:
            rev += reversal_map[c]
        reversed_possibilities += (rev+"A",)
    return reversed_possibilities

@lru_cache
def find_shortest(path: str, robot_level: int, human_level: int) -> int:
    if robot_level == human_level:
        return len(path)

    prev_button = "A"
    final_length = 0
    for next_button in path:
        shortest_sequence = 10 ** 20
        possible_paths = get_dirpad_paths(prev_button, next_button)
   
        for path in possible_paths:
            shortest_sequence = min(shortest_sequence, find_shortest(path, robot_level=robot_level+1, human_level=human_level))
        final_length += shortest_sequence
        prev_button = next_button
    return final_length

@lru_cache
def get_dirpad_paths(from_key: str, to_key: str) -> tuple[str]:
    dirpad = {
        "A": {"A": ("A",),
              "^": ("<A",),
              "<": ("<v<A", "v<<A",),
              "v": ("<vA", "v<A",),
              ">": ("vA",)},
        "^": {"^": ("A",),
              "<": ("v<A",),
              "v": ("vA",),
              ">": ("v>A", ">vA",)},
        "<": {"<": ("A",),
              "v": (">A",),
              ">": (">>A",)},
        "v": {"v": ("A",),
              ">": (">A",)},
        ">": {">": ("A",),},
    }
    try:
        possible_paths = dirpad[from_key][to_key]
    except KeyError:
        possible_paths = reverse_sequences(dirpad[to_key][from_key])
    return possible_paths



if __name__ == "__main__":
    main(sys.argv)

