# AOC 2023 day 1
#

import pathlib
import sys

# IN_FILE = "AOC2023\\inputs\\202301.txt"
# IN_FILE = "AOC2023\\inputs\\202301.sample.txt"
IN_FILE = "AOC2023\\inputs\\202301.sample2.txt"

# IN_FILE = "./inputs/202301.txt"
# IN_FILE = "./inputs/202301.sample.txt"

digit_text = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}


def parse(puzzle_input):
    """Parse input."""
    with open(IN_FILE) as fp:
        out = []
        data = fp.read().splitlines()

        for line in data:
            res = []
            for c in line:
                if c.isdigit():
                    res.append(c)
            out.append("".join(str(res[0]) + str(res[-1])))
        final = []
        for x in out:
            final.append(int(x))
    return final


def parse2(puzzle_input):
    """Parse input for part 2."""
    with open(IN_FILE) as fp:
        out = []
        data = fp.read().splitlines()

        for line in data:
            res = []
            for key in digit_text.keys():
                line = line.replace(key, digit_text[key]) 
            for c in line:
                if c.isdigit():
                    res.append(c)
            out.append("".join(str(res[0]) + str(res[-1])))
        final = []
        for x in out:
            final.append(int(x))
    return final

           

def part1(data):            # => 70369
    """Solve part 1."""
    return sum(data)

def part2(data):            # => 203002
    """Solve part 2."""
    return sum(data)





def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    # data = parse(puzzle_input)
    data2 = parse2(puzzle_input)
    #print(data)
    # solution1 = "part 1: " + str(part1(data))
    solution2 = "part 2: " + str(part2(data2))

    return solution1, solution2

if __name__ == "__main__":
    pth = list()
    if len(sys.argv[1:]) == 0:
        pth.append(IN_FILE)
    else:
        pth = sys.argv[1:]

    for path in pth:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
        