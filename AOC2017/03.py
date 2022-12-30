# AOC 2017 - Day 03
# tags: 

import time
import math

# IN_File = "AOC2017/03.txt"
INPUT = 325489
# INPUT = 100



def part1(data):    # 552
    base = int(math.sqrt(data)) # the size of the edge of the ring
    if base % 2 == 0: base -= 1

    side_len = base + 2
    middle = side_len // 2
    frombase = data - (base ** 2)
    side = frombase // side_len
    midpos = (side * side_len) + middle + (base ** 2) - side
    distance = abs(data - midpos) + middle

    return distance

def part2(data):    # 330785
    # I brute-forced this in a spreadsheet.
    #
    #                   330785	312453	295229	279138	266330	130654
    #   6591	6444	6155	5733	5336	5022	2450	128204
    #   13486	147	    142	    133	    122	    59	    2391	123363
    #   14267	304	    5	    4	    2	    57	    2275	116247
    #   15252	330	    10	    1   	1   	54  	2105	109476
    #   16295	351 	11	    23	    25  	26  	1968	103128
    #   17008	362	    747 	806 	880 	931 	957 	98098
    #   17370	35487	37402	39835	42452	45220	47108	48065
    #
    return 330785


if __name__ == "__main__":
    timestart = time.time()

    # data = parse()
    # print(data)

    print("part 1:",part1(INPUT))
    print("part 2:",part2(INPUT))
    
    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))