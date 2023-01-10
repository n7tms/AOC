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
            if i+1 < len(pwd) and pwd[i] == pwd[i+1]:
                if i+2 < len(pwd) and pwd[i] == pwd[i+2]:
                    repeating = True
                    i += 2
                else:
                    repeating = False
            repeating = True


    return repeating & increasing & length

def part1(data):    # 925
    count = 0
    for x in range(data[0],data[1]+1):
        if valid_pwd(str(x)):
            count += 1
    return count

def part2(data):    # 607
    count = 0
    for x in range(data[0],data[1]+1):
        if valid_pwd2(str(x)):
            count += 1
    return count

def other_solution():
    # This solution is from @sanjithpk and I do not understand for sure
    # how it works. 
    # I've tried to add comments for some sort of explanation.

    import collections

    low = 271973
    high = 785961
    a1 = []
    a2 = []

    t = low

    while True:
        d = list(str(t))
        
        # If the i+1 digit is less than the i digit, then
        # this number (t) doesn't work. 
        # Then fill the rest of the digits with the i+1 digit
        # and break out of the for loop.
        for i in range(5):
            if d[i] > d[i+1]:
                d[i + 1:6] = d[i] * (5-i)
                t = int("".join(d))
                d = list(str(t))
                break
        
        # If we're past the upper limit, break out of the while.
        if t > high:
            break

        # (This is where things get iffy.)
        # I think this is checking for at least a double digit
        if(collections.Counter(str(t)).most_common(1)[0][1] > 1):
            # if true, add this pwd to the part1 group.
            a1.append(t)
            
        # I think this is checking for a least two double digits.
        if(2 in collections.Counter(str(t)).values()):
            # if true, add this pwd to the part2 group.
            a2.append(t)
        t += 1
        
    print(len(a1), len(a2))


if __name__ == "__main__":
    timestart = time.time()

    data = parse()

    print("part 1:",part1(data))
    print("part 2:",part2(data))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))