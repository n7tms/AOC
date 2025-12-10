# AOC 2016 day 09: 
#

import time
import os

DAY = '09'
# IN_FILE = os.path.join("AOC2016","inputs","2016-"+str(DAY)+"-sample.txt")
IN_FILE = os.path.join("AOC2016","inputs","2016-"+str(DAY)+".in")

def parse(puzzle_input):
    """
    Parse
    """
    with open(IN_FILE) as fp:
        data = fp.read().strip()

    return data


def process_marker(chars: int, mag: int, text: str) -> str:
    pass


def part1(x):        # => 98135
    """
    Solve part 1
    """
    result = []
    i = 0
    while i < len(x):
        ch = x[i]
        if ch == "(":
            # read characters until the ")" is found
            i += 1
            j = i
            marker = []
            while j < len(x):
                if x[j] == ")":
                    j += 1
                    # process the marker (27x3)
                    chars, times = "".join(marker).split("x")
                    chars, times = int(chars), int(times)
                    result.append(x[j:j+chars]*times)
                    i = j + chars
                    break
                else:
                    marker.append(x[j])
                    j += 1
        else:
            result.append(x[i])
            i += 1

    return len("".join(result))
        

def part2(x):        # => 
    """
    Solve part 2
    """
    # I think there is a recursive solution here. The problem statement implies that the string will grow
    # very large. But let's see.
    

    return 0


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    x = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(x))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(x))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")


if __name__ == "__main__":
    solve(IN_FILE)
        