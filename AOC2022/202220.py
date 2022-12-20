# AOC 2022 - Day 20

import time

# IN_FILE = "AOC2022/inputs/202220.txt"
IN_FILE = "AOC2022/inputs/202220.sample.txt"


def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        out = f.read().split('\n')

    coords = list(map(int,out))
    return coords


def mixing(data):
    mixed = data.copy()
    
    for idx,num in enumerate(data):
        if num < 0:
            new_idx = (mixed.index(num) + num) % len(data) - 1
        else: 
            new_idx = (mixed.index(num) + num) % (len(data) - 1)
        if new_idx < 0:
            new_idx += len(data)
        mixed.remove(num)
        mixed.insert(new_idx,num)
        # print("mixed:",mixed)
    return mixed



def part1(data):            # => 
    """Solve part 1."""

    mixed = mixing(data)
    x = (mixed.index(0) + 1000) % len(mixed)
    y = (mixed.index(0) + 2000) % len(mixed)
    z = (mixed.index(0) + 3000) % len(mixed)
    
    return mixed[x] + mixed[y] + mixed[z]
            
    



def part2(data):            # => 
    """Solve part 2."""

if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    print("length", len(data))
    print("set length",len(set(data)))
    # print(data)

    print("part 1:",part1(data))
    print("part 2:",part2(data))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))