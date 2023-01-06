# AOC 2017 - Day 17
# tags: 

import time

INPUT = 380

def part1():    # 
    spinlock = [0]
    pos = 0
    for i in range(1,2018):
        pos = INPUT % (i) # - 1
        spinlock.insert(pos,i)

    return spinlock[pos+1]


    

def part2():    # 
    pass

if __name__ == "__main__":
    timestart = time.time()

    print("part 1:",part1())
    print("part 2:",part2())

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))