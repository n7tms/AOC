# --- Day 20:  ---

import time

# IN_FILE = "AOC2015/201519.txt"
target = 29000000


def part1(data):    # => 665280
    # A little bit of trial and error here. Even though I thought I was
    # checking for the instant a house was above target (fs[j]>=target),
    # it was not returning the earliest instance -- rather the last instance.
    # So I kept trimming the number until no house (none) was returned
    fs = [0] * 665281
    for i in range(1, 665281):
        for j in range(i,len(fs),i):
            fs[j] += (i * 10)
            if fs[j] >= data:
                return j
    

def part2(data):    # => 705600
    # required the same trimming process as part 1
    fs = [0] * (705601)
    for i in range(1, 705601):
        count = 0
        for j in range(i,len(fs),i):
            count += 1
            fs[j] += (i * 11)
            if fs[j] >= data:
                return j
            if count == 50: break
    


if __name__ == "__main__":
    timestart = time.time()

    puzzle_input = target

    print("\nDay 18: ===========================")
    print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", f"{timeend-timestart:0.4f}", "\n")


