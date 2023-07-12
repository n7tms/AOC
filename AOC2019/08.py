

IN_File = "08.txt"

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
                message.append(image[p][idx])
                break
    
    # print message
    for _ in range(6):
        for col in range(25):
            print(message[col],end="")
        print("")


def main():
    print(f"Part 1: {part1()}")     # 1572
    print(f"Part 2: {part2()}")

if __name__ == "__main__":
    main()