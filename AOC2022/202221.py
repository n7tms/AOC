# AOC 2022 - Day 21

import time

IN_FILE = "AOC2022\\inputs\\202221.txt"
# IN_FILE = "AOC2022\\inputs\\202221.sample.txt"


def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        out = f.read().split('\n')
    
    monkeys = {}
    for line in out:
        monkey,callout = line.split(':')
        callout = callout.strip()
        if callout.isnumeric():
            callout = int(callout)
        monkeys[monkey] = callout
    
    return monkeys


def yelling(data, monkey):
    if isinstance(data[monkey],int):
        return data[monkey]
    else:
        m1,op,m2 = data[monkey].split(' ')
        if op == '+':
            return yelling(data,m1) + yelling(data,m2)
        elif op == '-':
            return yelling(data,m1) - yelling(data,m2)
        elif op == '*':
            return yelling(data,m1) * yelling(data,m2)
        elif op == '/':
            return yelling(data,m1) / yelling(data,m2)


def part1(data):            # => 364367103397416
    """Solve part 1."""
    return yelling(data,'root')
        


def part2(data):            # => 
    """Solve part 2."""
    data['humn'] = 0
    

if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    # print(data)

    print("part 1:",part1(data))
    print("part 2:",part2(data))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))