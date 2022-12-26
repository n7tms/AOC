# AOC 2022 - Day 25

import time

IN_FILE = "AOC2022\\inputs\\202225.txt"
# IN_FILE = "AOC2022\\inputs\\202225.sample.txt"

def toDecimal(base5):
    txt = base5[::-1]
    for i in range(len(txt)):
        dig = txt[i]
        if dig == '-':
            mult = -1
        elif dig == '=':
            mult = -2
        else:
            mult = int(dig)
        
        if i == 0:
            converted = (5**i) * mult
        else:
            converted += (5**i) * mult
    return converted
        

    pass

# if quot = 3, then return '=' and add one to next digit

def toBase5(base10):
    result = ""
    quot = base10
    mod1 = quot % 5
    while quot > 0:
        if mod1 == 3:
            result += '='
            quot = (quot // 5) + 1
        elif mod1 == 4:
            result += '-'
            quot = (quot // 5) + 1
        else:
            result += str(mod1)
            quot = quot // 5
        mod1 = quot % 5
        
    return result[::-1]


def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        out = f.read().split('\n')
    return out


def part1(data):        # => 
    total = 0
    for i in data:
        total += toDecimal(i)
    return toBase5(total)


def part2(data):        # => 
    pass

if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    # print(data)

    print("part 1:",part1(data))
    print("part 2:",part2(data))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))