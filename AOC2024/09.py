# AOC 2024 day 09: 
#

import aoc_utils as aoc
import time
import os

DAY = '09'
IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2024","inputs","2024-"+str(DAY)+".sample.txt")


def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2024,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()
    
    return data



def part1(data):        # => 6415184586041
    orgdiskmap = [int(c) for c in data[0]]

    diskmap = []

    idx = 0
    id = 0
    while idx < len(orgdiskmap):
        if idx % 2 == 0:
            f = orgdiskmap[idx]
            diskmap.append([id]*f)
            id += 1 
        else: 
            s = orgdiskmap[idx]
            if s > 0:
                diskmap.append(['.']*s)
        idx += 1

    # Flatten the list
    diskmap2 = [item for sublist in diskmap for item in sublist]
    
    diskmap3 = []
    idx = 0
    while diskmap2:
        if diskmap2[0] != '.':
            diskmap3.append(diskmap2.pop(0))
        else:
            c = diskmap2.pop()
            while c == '.' and diskmap2:
                c = diskmap2.pop()
            if c != '.': diskmap3.append(c)

            if diskmap2: diskmap2.pop(0)


    checksum = 0
    for idx, val in enumerate(diskmap3):
        checksum = checksum + (idx * val)

    return checksum


def part2(data):        # => 6436819084274
    orgdiskmap = [int(c) for c in data[0]]

    diskmap = []

    idx = 0
    id = 0
    while idx < len(orgdiskmap):
        if idx % 2 == 0:
            f = orgdiskmap[idx]
            diskmap.append([id]*f)
            id += 1 
        else: 
            s = orgdiskmap[idx]
            if s > 0:
                diskmap.append(['.']*s)
        idx += 1


    # lr_idx = left to right index (from the beginning)
    # rl_idx = right to left index (from the end)
    
    rl_idx = len(diskmap)-1
    while rl_idx > 0:
        if diskmap[rl_idx][0] != '.':
            length = len(diskmap[rl_idx])
            for lr_idx, disk in enumerate(diskmap):
                if lr_idx >= rl_idx: break
                if disk[0] == '.' and len(disk) == length:
                    # if they are the same length, just swap them
                    diskmap[rl_idx], diskmap[lr_idx] = diskmap[lr_idx], diskmap[rl_idx]
                    break
                elif disk[0] == '.' and len(disk) >= length:
                    # insert all of rl into this spot
                    diskmap.insert(lr_idx, diskmap.pop(rl_idx))
                    # slice the "space" and put it in the index at lr
                    diskmap.insert(rl_idx+1, diskmap[lr_idx+1][0:length])
                    diskmap[lr_idx+1] = diskmap[lr_idx+1][0:len(disk)-length]
                    rl_idx += 1
                    break
        rl_idx -= 1
                

    # Flatten the list and calculate the checksup
    diskmap2 = [item for sublist in diskmap for item in sublist]
    checksum = 0
    for idx, val in enumerate(diskmap2):
        if val != '.':
            checksum = checksum + (idx * val)

    return checksum



def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(data))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(data))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        