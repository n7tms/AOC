
def part1():
    with open("201503.txt", "r") as f:
        data = f.read()
        size = len(data)
        x,y = size,size
        houses = [ [0] * size * 2 for _ in range(size * 2)]
        houses[x][y] = 1
        # a = {'^': 'N','>': 'E','v': 'S','<': 'W',}

        for direction in data:
            if direction == '^':
                y -= 1
            elif direction == '>':
                x += 1
            elif direction == 'v':
                y += 1
            else:
                x -= 1
            houses[x][y] += 1

        print(sum(1 for x in houses for i in x if i))

def part2():
    with open("201503.txt", "r") as f:
        data = f.read()
        size = len(data)
        xs,ys = size,size
        xr,yr = size,size
        houses = [ [0] * size * 2 for _ in range(size * 2)]
        houses[xs][ys] = 2
        # a = {'^': 'N','>': 'E','v': 'S','<': 'W',}

        turn = 0
        for direction in data:
            if direction == '^':
                y = -1
                x = 0
            elif direction == '>':
                x = 1
                y = 0
            elif direction == 'v':
                y = 1
                x = 0
            else:
                x = -1
                y = 0
            if turn == 0:
                xs += x
                ys += y
                houses[xs][ys] += 1
                turn = 1
            else:
                xr += x
                yr += y
                houses[xr][yr] += 1
                turn = 0

        print(sum(1 for x in houses for i in x if i))

part1()  # => 2081
part2()  # => 2341

    

