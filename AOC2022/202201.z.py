import time
import numpy as np
import re

start=time.time()

# =========================================================================================================================
# with open("2201.sample.txt") as f:
#         (sol1, sol2) = [(totalcal[0], np.sum(totalcal[:3])) for totalcal in [sorted([np.sum([int(cal) for cal in elf.split('\n')]) for elf in f.read().split('\n\n')],reverse=True)]][0]
# print('Solution 1:', sol1)
# print('Solution 2:', sol2)


# =========================================================================================================================
# without numpy
# with open("2201.sample.txt") as f:
#         (sol1, sol2) = [(totalcal[0], sum(totalcal[:3])) for totalcal in [sorted([sum([int(cal) for cal in elf.split('\n')]) for elf in f.read().split('\n\n')],reverse=True)]][0]
# print('Solution 1:', sol1)
# print('Solution 2:', sol2)

# =========================================================================================================================
# with open("2201.sample.txt") as f:
#     cals = f.read().rstrip()

# elves = [sum(int(c) for c in e.split("\n")) for e in cals.split("\n\n")]
# print(max(elves))
# print(sum(sorted(elves, reverse=True)[:3]))


# =========================================================================================================================
# with open("2201.sample.txt") as f:
#         sol1 = [(totalcal[0]) 
#         for totalcal in 
#         [sorted([sum([int(cal) for cal in elf.split('\n')]) for elf in f.read().split('\n\n')],reverse=True)]][0]

# =========================================================================================================================
# with open("2201.sample.txt") as f:
#     elfs = [(elf) for elf in f.read().split('\n\n')]
#     print(elfs)

#     cals = sorted([sum([int(cal) for cal in elf.split('\n')]) for elf in elfs], reverse=True)
#     print(cals)


# =========================================================================================================================
data = open('2201.sample.txt').read()

data = sorted([sum([int(i) for i in re.split(r'\D+', x)]) for x in data.split('\n\n')], reverse=True)
print(data[0])        # day1_part1
print(sum(data[0:3])) # day1_part2

# =========================================================================================================================

end=time.time()
print("time: ", end-start)

