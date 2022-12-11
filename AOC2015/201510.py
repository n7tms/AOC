# AOC 2015 - Day 10

import time

input = "1113122113"

def look_and_say(x):
    out = ''

    cnt = 1
    for i in range(len(x)):
        if i+1 < len(x) and x[i] == x[i+1]:
            cnt += 1
        else:
            out += str(cnt) + str(x[i])
            cnt = 1
    return out


def part1(data):            # => 
    """Solve part 1."""
    x = look_and_say(data)
    for i in range(39):
        x = look_and_say(x)
    return len(x)

def part2(data):            # => 
    """Solve part 2."""
    x = look_and_say(data)
    for i in range(49):
        print(i)
        x = look_and_say(x)
    return len(x)


if __name__ == "__main__":
    timestart = time.time()

    print("part 1:",part1(input))
    print("part 2:",part2(input))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))

