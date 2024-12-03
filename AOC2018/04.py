# AOC 2018 day 04: 
#

import aoc_utils as aoc
import time
import os
import re
import numpy as np


DAY = '04'
IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".in")
# IN_FILE = os.path.join("AOC2018","inputs","2018-"+str(DAY)+".sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    aoc.get_input(2018,DAY,False)

    with open(IN_FILE) as fp:
        data = fp.read().strip().splitlines()
    data.sort()

    guards = {}
    asleep = False
    last_min = 0
    last_guard = None
    last_date = None
    activity = [0]*60
    guard_num = -1
    for line in data:
        # breakout timestamp and report
        # is a gaurd beginning a shift?
        #   if the asleep flag is set, make the previous guard asleep until min 59
        #   create a new guard with date, and awake mins
        #   unset asleep flag (asleep = False)
        #   last min = 0
        # is report falls asleep?
        #   set asleep flag

        date, time, report = re.match(r"\[(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2})\] (.+)", line).groups()
        hr, mn = time.split(':')

        if report[0] == 'G':
            if asleep:
                # make the last guard sleep through 59
                for m in range(last_min, 60):
                    activity[m] = 1
                
            if guard_num not in guards and guard_num > -1:
                guards[guard_num] = activity
            elif guard_num > -1:
                # guards[guard_num].append({'timestamp':last_date,'asleep':activity})
                guards[guard_num] = [a + b for a,b in zip(guards[guard_num], activity)]


            # get the new guard number
            guard_num = int(re.findall(r"\d+",report)[0])
            asleep = False
            last_min = 0 if int(hr) == 23 else int(mn)
            activity = [0]*60
            last_date = date
        
        if report == 'falls asleep':
            last_min = int(mn)
            asleep = True

        if report == 'wakes up':
            for m in range(last_min,int(mn)):
                activity[m] = 1
            asleep = False
            


    return guards



def part1(guards):        # => 76357
    # find the guard that slept the most
    max_sleeper = 0
    max_sleep = 0
    for g,v in guards.items():
        if sum(v) > max_sleep:
            max_sleep = sum(v)
            max_sleeper = g
    
    # find the index of the minute he slept the most
    max_min = np.argmax(guards[max_sleeper])

    # return the guard # * the minute
    return max_min * int(max_sleeper)
        

def part2(guards):       # => 41668
    most_freq = 0
    most_guard = 0
    for g,v in guards.items():
        if max(v) > most_freq:
            most_freq = max(v)
            most_guard = g

    return most_guard * np.argmax(guards[most_guard])


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

