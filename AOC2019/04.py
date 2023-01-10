# AOC 2019 - Day 4
# tags: 

import time

IN_File = "271973-785961"

def parse():
    return list(map(int,IN_File.split('-')))


def valid_pwd(pwd):
    repeating = False
    increasing = True
    length = False

    if len(pwd) >= 6: length = True
    for i in range(1,len(pwd)):
        if pwd[i] < pwd[i-1]: increasing = False
        if pwd[i] == pwd[i-1]: repeating = True

    return repeating & increasing & length

def valid_pwd2(pwd):
    repeating = False
    increasing = True
    length = False
    group = False

    if len(pwd) >= 6: length = True
    for i in range(1,len(pwd)):
        if pwd[i] < pwd[i-1]: increasing = False
        if pwd[i] == pwd[i-1]: 
            repeating = True
            if not group:
                group = True
                

    return repeating & increasing & length

def part1(data):    # 925
    count = 0
    for x in range(data[0],data[1]+1):
        if valid_pwd(str(x)):
            count += 1
    return count

def part2(data):    # 
    count = 0
    for x in range(data[0],data[1]+1):
        if valid_pwd2(str(x)):
            count += 1
    return count

if __name__ == "__main__":
    timestart = time.time()

    data = parse()

    print("part 1:",part1(data))
    print("part 2:",part2(data))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))