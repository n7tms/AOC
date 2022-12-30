# AOC 2017 - Day 03
# tags: 

import time

IN_File = "AOC2017/04.txt"

def parse():
    """Parse input."""
    with open(IN_File) as f:
        out = f.read().split('\n')

    return list([words for words in line.split(' ')] for line in out)


def part1(data):    # 451
    return sum(list(1 for words in data if len(words) == len(set(words))))

def part2(data):    # 223
    valid = 0

    # sort the letters in each word
    newdata = []
    for words in data:
        sortedwords = []
        for w in words:
            a = list(w)
            a.sort()
            a = "".join(a)
            sortedwords.append(a)
        newdata.append(sortedwords)
    
    # compare words to other words in the list
    for words in newdata:
        idx = 0
        for word in words:
            idx += 1
            found = False
            if word in words[idx:]:
                found = True
                break
        if not found:
            valid += 1

    return valid


if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    # print(data)

    print("part 1:",part1(data))
    print("part 2:",part2(data))
    
    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))