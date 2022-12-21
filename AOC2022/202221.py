# AOC 2022 - Day 21

import time

IN_FILE = "AOC2022/inputs/202221.txt"
# IN_FILE = "AOC2022/inputs/202221.sample.txt"


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
    return yelling(data,'root')
        

def part2(data):            # => 3782852515583

    # This is a TOTAL hack!
    # After some brute force failures (literally about a million of them),
    # I pasted the results of the first 20 brute-force trials into a spreadsheet to look for patterns.
    # I found that the difference between trial(n) and trial(n-1) was a constant...
    # Dividing the difference between both sides of the 'root' operation and that constant
    # gives me a number -- a number that just happened to be the correct answer!
    #
    # I don't know if this will work with other inputs, but it worked with mine.

    # The constant is 43.75

    # "data" is a dictionary; 
    # key = monkey name, value = equation or literal associated with that monkey

    # Get both sides of the 'root' monkey
    m1,_,m2 = data['root'].split(' ')

    # We need two trials to get the difference numbers. It doesn't matter which trials we select,
    # as long as they're consecutive. I selected 0 and 1.
    data['humn'] = 0

    # Get answers for both sides of 'root' in trial 0
    t01 = yelling(data,m1)
    t02 = yelling(data,m2)
    # and calculate the difference. 
    diff = t01-t02

    # We only need an answer for the left side of the 'root' monkey in trial 1
    data['humn'] = 1
    t11 = yelling(data,m1)
    # and calculate the difference between the first trial (0) and this one (1).
    # This is the constant we're look for.
    the_constant = t01 - t11

    # The answer is the previous difference (diff) divided by the constant
    ans = diff/the_constant
    return ans
    

if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    # print(data)

    print("part 1:",part1(data))
    print("part 2:",part2(data))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))