# --- Day 19:  ---


import time

# IN_FILE = "AOC2015/201519.txt"
IN_FILE = "AOC2015/201519.sample.txt"

def parse():
    with open(IN_FILE) as f:
        out = [line for line in f.read().split('\n\n')]
    
    replacements = out[0]
    medicine = out[1]

    return replacements,medicine



def part1(data):    # => 

    molecules = []
    # iterate through the replacements
        # iterate through the medicine
            # replace the first occurence of the replacement
            # save the new medicine in a list of molecules
    # turn the molecule list into a set
    # return the length (count) in the molecule set
    return 0

def part2(data):    # => 

    return 0


if __name__ == "__main__":
    timestart = time.time()

    puzzle_input = parse()
    puzzle_input2 = parse()

    print("\nDay 18: ===========================")
    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input2))
    
    timeend = time.time()
    print("Execution time: ", f"{timeend-timestart:0.4f}", "\n")


