# AOC 2017 - Day 20
# tags: #regex #HARD

# I tried many different approaches before I gave up.
# Even my step-by-step brute force solution did not yield a 
# correct solution.
# See 20.z.py from @jlweinkam for a valid solution.

import time
import re

IN_File = "AOC2017/20.txt"

def parse():
    with open(IN_File) as f:
        out = f.read().split('\n')

    particles = {}
    for i,line in enumerate(out):
        p,v,a = line.split(' ')
        pos = re.findall("p=<(-?\d+),(-?\d+),(-?\d+)>,",p)
        pos = list(map(int,pos[0]))
        vel = re.findall("v=<(-?\d+),(-?\d+),(-?\d+)>,",v)
        vel = list(map(int,vel[0]))
        acc = re.findall("a=<(-?\d+),(-?\d+),(-?\d+)>",a)
        acc = list(map(int,acc[0]))
        particles[i] = [pos,vel,acc]

    return particles


def part1(particles):    # 125
 
    closest = [9999,9999999]
    for key,part in particles.items():
        pos = abs(sum(part[0]))
        vel = abs(sum(part[1]))
        acc = abs(sum(part[2]))

        distance = pos + ((vel + (acc * 100000 / 2)) * 100000)
        if distance < closest[1]:
            closest = [key,distance]


    return closest        

def part2():    # 461
    pass

if __name__ == "__main__":
    timestart = time.time()

    data = parse()

    print("part 1:",part1(data))
    # print("part 2:",part2(data))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))