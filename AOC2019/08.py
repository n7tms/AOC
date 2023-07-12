

# IN_File = "08.txt"
IN_File = "AOC2019/08.txt"

def parse():
    with open(IN_File) as f:
        out = f.read()
    pwd = [digit for digit in out]
    prgm = list(map(int,pwd))
    return prgm

def makelayers(input, width, height):
    layersize = width * height
    image = []
    for i in range(0,len(input),layersize):
        image.append(list(input[i:(i+layersize)]))
    return image

def countelements(lst, target):
    return lst.count(target)

def part1():
    data = parse()
    image = makelayers(data,25,6)

    zeros = 151
    zerolayer = 0
    for idx, layer in enumerate(image):
        z = countelements(layer,0)
        if z < zeros:
            zeros = z
            zerolayer = idx

    return countelements(image[zerolayer],1) * countelements(image[zerolayer],2)

def part2():
    data = parse()
    image = makelayers(data,25,6)

    message = []
    for idx in range(150):
        for p in range(len(image)):
            if image[p][idx] < 2:
                # message.append(image[p][idx])
                if image[p][idx] == 0:
                    message.append(" ")
                else:
                    message.append("#")
                break

    # message = []
    # for line in image:
    #     for row in range(6):
    #         for col in range(25):
    #             print(line[row*col],end="")
    #         print("")
    #     print("")
    

    # print message
    for row in range(6):
        for col in range(25):
            pixel = (row * col) + col
            print(message[pixel],end=" ")
        print("")


import numpy as np

def zedrdave():
    digits = [int(i) for i in open(IN_File, 'r').read().strip()]

    layers = np.array(digits).reshape((-1,6,25))
    composite = np.apply_along_axis(lambda x: x[np.where(x != 2)[0][0]], axis=0, arr=layers)

    print("Part 2:")
    print("\n".join(''.join(u" ♥️"[int(i)] for i in line) for line in composite))



def eastballz():
    def split(lst, size):
        return [lst[i:i+size] for i in range(0, len(lst), size)]

    def count(l, v):
        return sum(map(lambda x: 1 if x == v else 0, l))

    def collapse(layers):
        return [next(filter(lambda v: v != 2, lay)) for lay in zip(*layers)]

    def draw(img):
        for r in img: print(*['#' if x == 1 else ' ' for x in r])

    lenx, leny = 25, 6
    data = [int(x) for x in open(IN_File).read().strip('\n')]

    # Part 1
    layers = split(data, lenx*leny)
    best = min(layers, key=lambda l: count(l, 0))
    # print(count(best, 1) * count(best, 2))

    # Part 2
    img = split(collapse(layers), lenx)
    draw(img)

def main():
    print(f"Part 1: {part1()}")     # 1572
    print(f"Part 2: ")
    # print(f"Part 2: {part2()}")
    # zedrdave()
    eastballz()

if __name__ == "__main__":
    main()