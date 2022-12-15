# AOC 2022 - day 10
# adapted from 'juanplopes'

IN_FILE = "AOC2022\\inputs\\202210.txt"

def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        return [line for line in f.read().split('\n')]

def execute(program):
    regval = 1
    for line in program:
        yield regval
        if line[0] == 'addx':
            yield regval
            regval += int(line[1])

out = list(execute(line.split() for line in parse()))
print(sum(out[i - 1] * i for i in [20,60,100,140,180,220]))

# print the CRT
for i in range(6):
    print(''.join('.#'[abs(out[i * 40 + j] - j) <= 1] for j in range(40)))