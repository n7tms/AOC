# AOC 2017 - Day 15
# tags: #binary #large

import time

IN_File = "AOC2017/15.txt"

def parse():
    with open(IN_File) as f:
        out = f.read().split('\n')
    
    generators = {}
    for line in out:
        x = line.strip().split(' ')
        generators[x[1]] = int(x[4])
    
    return generators


def part1(generators):    # 619
    a = generators['A']
    b = generators['B']

    matches = 0
    for _ in range(40000000):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647
        x = f'{a:0>32b}'
        y = f'{b:0>32b}'
        if x[-16:] == y[-16:]:
            matches += 1

    return matches        

def part2(generators):    # 290
    a = generators['A']
    b = generators['B']

    matches = 0
    for _ in range(5000000):
        a = (a * 16807) % 2147483647
        b = (b * 48271) % 2147483647
        while a % 4 != 0:
            a = (a * 16807) % 2147483647
        while b % 8 != 0:
            b = (b * 48271) % 2147483647

        x = f'{a:0>32b}'
        y = f'{b:0>32b}'
        if x[-16:] == y[-16:]:
            matches += 1

    return matches        

if __name__ == "__main__":
    timestart = time.time()

    generators = parse()

    print("part 1:",part1(generators))
    print("part 2:",part2(generators))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))