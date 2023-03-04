# AOC 20215 - Day 14

import time
from collections import defaultdict

# IN_FILE = "AOC2015\\201514.txt"
IN_FILE = "AOC2015\\201514.sample.txt"

 

def parse():
    with open(IN_FILE) as f:
        out = [line for line in f.read().split('\n')]

    reindeers = defaultdict(dict)
    for line in out:
        name, speed, duration, rest = line.split(' ')[0], int(line.split(' ')[3]), int(line.split(' ')[6]), int(line.split(' ')[13])
        reindeers[name]={"speed":speed, "duration":duration, "rest":rest, "resting":False, "time": duration, "distance": 0, "score": 0}
    return reindeers


def one_second(reindeers):
    for reindeer in reindeers:
        # print(reindeer)
        if reindeers[reindeer]["resting"] and reindeers[reindeer]["time"] == 0:
            reindeers[reindeer]["resting"] = False
            reindeers[reindeer]["time"] = reindeers[reindeer]["duration"]
        elif not reindeers[reindeer]["resting"] and reindeers[reindeer]["time"] == 0:
            reindeers[reindeer]["resting"] = True
            reindeers[reindeer]["time"] = reindeers[reindeer]["rest"]
        elif not reindeers[reindeer]["resting"]:
            reindeers[reindeer]["distance"] += reindeers[reindeer]["speed"]
            reindeers[reindeer]["time"] -= 1
        else:
            reindeers[reindeer]["time"] -= 1

    return reindeers


def part1(reindeers):          # -> 2640
    race = one_second(reindeers)
    for i in range(2502):
        race = one_second(race)
    print(reindeers)
    
    winner = [None,0]
    for r in race:
        if race[r]["distance"] > winner[1]:
            winner = [r,race[r]["distance"]]
    return winner


def part2(reindeers):          # -> 1102
    # for i in range(2503):
    for i in range(1000):
        reindeers = one_second(reindeers)

        winning = [None,0]
        for r in reindeers:
            if reindeers[r]["distance"] > winning[1]:
                winning = [r,reindeers[r]["distance"]]
    
        for r in reindeers:
            if reindeers[r]["distance"] == winning[1]:
                reindeers[r]["score"] += 1

    print(reindeers)
    
    winner = [None,0]
    for r in reindeers:
        if reindeers[r]["score"] > winner[1]:
            winner = [r,reindeers[r]["score"]]
    return winner

if __name__ == "__main__":
    timestart = time.time()
    
    reindeers = parse()
    reindeers2 = parse()
    # print(reindeers)


    print("part 1:",part1(reindeers))
    print("part 2:",part2(reindeers2))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))




