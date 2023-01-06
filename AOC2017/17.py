# AOC 2017 - Day 17
# tags: #deque #large #repeating

import time
from collections import deque

# ####################################################################################
# Note to future-self:
# deque is WAAAAAY faster than the built-in python list.
# part2 using a list took over 2 minutes to process the first million iterations.
# deque took less than 50 seconds to process all 50 million.
# ####################################################################################


INPUT = 380
# INPUT = 3

# def part1():    # 204
#     spinlock = [0]
#     pos = 0
#     for i in range(1,2018):
#         pos = ((pos + INPUT) % len(spinlock)) + 1
#         spinlock.insert(pos,i)
#     return spinlock[pos+1]

def part1():    # 204
    spinlock = deque([0])
    pos = 0
    for i in range(1,2018):
        spinlock.rotate(-INPUT)
        spinlock += i,
    return spinlock[0]
    

def part2():    # 28954211
    spinlock = deque([0])
    pos = 0
    for i in range(1,50000001):
        spinlock.rotate(-INPUT)
        spinlock += i,
    return spinlock[spinlock.index(0) + 1]



# here is another solution from @mcpower_
# instead of building the whole list, just keep track of the number that 
# falls into position 1 -- ingenious!
# completes in 26 seconds.
#
# I made a couple of modifications and got it down to 19 seconds.

def part2b():
    pos = 0
    out = 0
    for i in range(1,50000001):
        to_ins = i+1
        new = ((pos + INPUT) % i) + 1
        if new == 1:
            out = to_ins
        pos = new
    print(out)


if __name__ == "__main__":
    timestart = time.time()

    # print("part 1:",part1())
    # print("part 2:",part2())

    part2b()

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))