# AOC 2023 day 1
#

import pathlib
import sys

IN_FILE = "AOC2023\\inputs\\202301.in"
# IN_FILE = "AOC2023\\inputs\\202301.sample.in"
# IN_FILE = "AOC2023\\inputs\\202301.sample2.in"

# IN_FILE = "./inputs/202301.in"
# IN_FILE = "./inputs/202301.sample.in"

digit_text = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def extract_digits(data: str) -> list:
    """
    Iterate through the line of text. 
    If the character is a digit, store the digit (in out[]).
    Otherwise, attempt to match (starting at that character) with something in digit_text.
    If a match is found, store the corresponding digit.
    """
    out = []
    for i,c in enumerate(data):
        if c.isdigit():
            out.append(c)
        else:
            for x in digit_text:
                if len(data)-i >= len(x):
                    slc = slice(i,i+len(x))
                    if data[slc] == x:
                        out.append(digit_text[x])
                        break
    return out
        

def parse(puzzle_input):
    """
    Part 1 Parse
    Just look for digits (numbers) in the text.
    Create a list of the numbers in the line.
    Concatenate the first and last digit and append the result to final[].
    Convert each item in final[] to ints.
    Return final[]
    """
    with open(IN_FILE) as fp:
        out = []
        data = fp.read().splitlines()

        for line in data:
            res = []
            for c in line:
                if c.isdigit():
                    res.append(c)
            try:
                out.append("".join(str(res[0]) + str(res[-1])))
            except:
                continue

        final = []
        for x in out:
            final.append(int(x))
    return final


def parse2(puzzle_input):
    """
    Part 2 Parse
    Written out numbers (one, two, etc.) now count.
    And they can over lap (twoneight = 218)
    Uses extract_digits() to accurately extract the digits (words and/or numbers) from the input.
    Concatenate the first and last digit and append the result to final[].
    Convert each item in final[] to ints.
    Return final[]

    """
    with open(IN_FILE) as fp:
        out = []
        data = fp.read().splitlines()

        for line in data:
            res = extract_digits(line)
            out.append("".join(str(res[0]) + str(res[-1])))
        final = []
        for x in out:
            final.append(int(x))
    return final

           

def part1(data):            # => 56465
    """Solve part 1."""
    return sum(data)

def part2(data):            # => 55902
    """Solve part 2."""
    return sum(data)





def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = "part 1: " + str(part1(data))

    data = parse2(puzzle_input)
    solution2 = "part 2: " + str(part2(data))

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
        