# AOC 20215 - Day 14

import time
from collections import defaultdict

IN_FILE = "AOC2015\\201514.txt"
# IN_FILE = "AOC2015\\201514.sample.txt"

 

def parse():
    with open(IN_FILE) as f:
        out = [line for line in f.read().split('\n')]

    reindeers = defaultdict(dict)
    for line in out:
        name, speed, duration, rest = line.split(' ')[0], int(line.split(' ')[3]), int(line.split(' ')[6]), int(line.split(' ')[13])
        reindeers[name]={"speed":speed, "duration":duration, "rest":rest, "resting":False, "rested": 0, "ran": duration, "distance": 0}
    return reindeers


def one_second(reindeers):
    for reindeer in reindeers:
        # print(reindeer)
        if reindeers[reindeer]["resting"]:
            if reindeers[reindeer]["rested"] == 0:
                reindeers[reindeer]["resting"] = False
                reindeers[reindeer]["ran"] = reindeers[reindeer]["duration"]
                # reindeers[reindeer]["distance"] += reindeers[reindeer]["speed"]
            else:
                reindeers[reindeer]["rested"] -= 1
        else:
            if reindeers[reindeer]["ran"] == 0:
                reindeers[reindeer]["resting"] = True
                reindeers[reindeer]["rested"] = reindeers[reindeer]["rest"]
            else:
                reindeers[reindeer]["distance"] += reindeers[reindeer]["speed"]
                reindeers[reindeer]["ran"] -= 1
    return reindeers


def part1(reindeers):          # -> 2640
    race = one_second(reindeers)
    for i in range(2502):
    # for i in range(999):
        # if i == 136:
        #     t=3
        race = one_second(race)
    
    winner = [None,0]
    for r in race:
        if race[r]["distance"] > winner[1]:
            winner = [r,race[r]["distance"]]
    return winner



def part2(reindeers):          # ->  >1064
    pass

if __name__ == "__main__":
    timestart = time.time()
    
    reindeers = parse()
    # print(reindeers)


    print("part 1:",part1(reindeers))
    print("part 2:",part2(reindeers))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))




