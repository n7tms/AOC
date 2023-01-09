# AOC 2017 - Day 22
# tags: #coords

import time

IN_File = "AOC2017/22.txt"
grid_size = 1001
DIRS = [[-1,0],[0,1],[1,0],[0,-1]]

def parse():
    with open(IN_File) as f:
        out = f.read().split('\n')

    the_map = []
    brdr_size = (grid_size - len(out)) // 2
    for i in range(brdr_size):
        the_map.append("." * grid_size)

    for line in out:
        row = "." * brdr_size
        row += line
        row += "." * brdr_size
        the_map.append(row)
        

    for i in range(brdr_size):
        the_map.append("." * grid_size)

    # print("map size: ",len(the_map[0]),"x",len(the_map))

    # now convert everything to a lists of lists
    final_map = []
    for row in the_map:
        final_map.append(list(row))

    return final_map
        

def part1(data):    # 5565
    infected = 0
    pos = [grid_size//2,grid_size//2]
    dir = 0

    # walk the map
    for _ in range(10000):
        cur_node = data[pos[0]][pos[1]]
        if cur_node == '#':
            dir += 1    # turn right
            data[pos[0]][pos[1]] = '.'
        elif cur_node == '.':
            dir -= 1    # turn left
            data[pos[0]][pos[1]] = '#'
            infected += 1
        dir = dir % 4
        pos = [sum(i) for i in zip(pos,DIRS[dir])]

        # test for off the map
        if pos[0] < 0 or pos[1] < 0 or pos[0] > grid_size or pos[1] > grid_size:
            print("off the map:",pos)
            break

    return infected



def part2(data):    # 2511978
    infected = 0
    pos = [grid_size//2,grid_size//2]
    dir = 0

    # walk the map
    for _ in range(10000000):
        cur_node = data[pos[0]][pos[1]]
        if cur_node == '#':
            dir += 1    # turn right
            data[pos[0]][pos[1]] = 'f'
        elif cur_node == '.':
            dir -= 1    # turn left
            data[pos[0]][pos[1]] = 'w'
        elif cur_node == 'w':
            # dir -= 1    # continue straight
            data[pos[0]][pos[1]] = '#'
            infected += 1
        elif cur_node == 'f':
            dir += 2    # reverse
            data[pos[0]][pos[1]] = '.'

        dir = dir % 4
        pos = [sum(i) for i in zip(pos,DIRS[dir])]

        # test for off the map
        if pos[0] < 0 or pos[1] < 0 or pos[0] > grid_size or pos[1] > grid_size:
            print("off the map:",pos)
            break

    return infected

if __name__ == "__main__":
    timestart = time.time()

    data = parse()
    data2 = parse()

    print("part 1:",part1(data))
    print("part 2:",part2(data2))

    timeend = time.time()
    print("Execution time: ", "{:.4f}".format(round(timeend-timestart,7)))