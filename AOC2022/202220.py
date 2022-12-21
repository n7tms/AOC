# AOC 2022 - Day 20

# possible linked list implementation: https://realpython.com/linked-lists-python/
# or https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm

import time

IN_FILE = "AOC2022/inputs/202220.txt"
# IN_FILE = "AOC2022/inputs/202220.sample.txt"


def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        out = list([int(x),0] for x in f.read().split('\n'))
    return out

# calc the new position
# remove the num at the old pos (1,2)
# insert the num at the new pos (1,4)
# for num,idx in list[:4+1]:
#    list[idx] = (num,idx+1)

def mixing(data):
    mixed = data.copy()
    length = len(mixed)

    for i in range(length):
        num,status = data[i]
        idx = mixed.index([num,0])
        # if status == 1:
        #     continue

        if num < 0:
            new_idx = (idx + num) % length - 1
        else: 
            new_idx = (idx + num) % (length - 1)
        if new_idx < 0:
            new_idx += length
        mixed.remove([num,0])
        mixed.insert(new_idx,list((num,1)))
        # print("mixed:",mixed)


        # if num < 0:
        #     new_idx = (mixed.index(num) + num) % len(data) - 1
        # else: 
        #     new_idx = (mixed.index(num) + num) % (len(data) - 1)
        # if new_idx < 0:
        #     new_idx += len(data)
        # mixed.remove(num)
        # mixed.insert(new_idx,num)
        # print("mixed:",mixed)
    return mixed



def part1(data):            # => 16533
    """Solve part 1."""

    mixed = mixing(data)
    print(mixed)
    x = (mixed.index([0,1]) + 1000) % len(mixed)
    y  = (mixed.index([0,1]) + 2000) % len(mixed)
    z  = (mixed.index([0,1]) + 3000) % len(mixed)
    
    return mixed[x][0] + mixed[y][0] + mixed[z][0]
            
    



def part2(data):            # => 4789999181006
    """Solve part 2."""

if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    # print("length (raw, set):", len(data),len(set(data)))
    # print(data)

    print("part 1:",part1(data))
    print("part 2:",part2(data))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))