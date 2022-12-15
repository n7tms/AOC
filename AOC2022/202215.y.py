# https://topaz.github.io/paste/#XQAAAQBCBAAAAAAAAAAyGUj/T2CE9VrzfJp/U5l201IEQlp3fhSdKU3xKaqIR8deQD6EwhHIiw0bSP+7r+07yxKzJ9ynD7G/KfXft0A57vtORsq0A9cpKYkPs29ofLwOi7bmlOZr2Nqg3xQwo8A3cSXZRduaicDs0JBSzcZ8rXDw3jzxP00neE0XZbh/97z/ty2T+89+hiMevkrh7xqUFBZcV7jomS3a0sDjVnTsfpcF/nV+dhg45xoLmvw2tFLrjC0iR8sffyBkdf06GIBp4XyIFXlqP58sBoUVpozyvvkDON9FHq8c0evtEwULg3ayRFLyaw4yircabWaQilH6vwMy9xdGgCtEogOLal7PwxdT+Dy7npJpt+aUkXvizAezcDtYOHtp9weRklymd4+Od9Cf8UbZgZ1MyW0SUaufe0onVriX/VV7YIYYeEzN1uJnAYJY6AfpTEPi/HsC5+p5QQ+SZEzECG5enppkWUYOZsabt/gwt/3D3GbGRAMb1zLb1DdiErwsMGq103iKNs+egmqesYOfqaUqiTNbAqWk3g/Vgd9e3GZd54oI9pBqp9YhCyiON7Iz98OjSbMsOLaU+f79MtiM3WmRZGuolLk+hIhfFlLyvQdH9hUhKByo5w4lAR6KeV4ryzjndKD/mrlqJA==


# part 1 and 2 solutions plagarized from different sources. Part 2 from above linke; part 1 is unknown.
# I need to go back and understand what these are doing and learn from them.
# I selected part 1 because it looked like a similar road I was heading down, but MUCH sleaker!
# part 2 --- I didn't even know where to begin. :(


from collections import defaultdict
import sys, fileinput, re, math

IN_FILE = "AOC2022\\inputs\\202215.txt"
# IN_FILE = "AOC2022\\inputs\\202215.sample.txt"

def part1():
    with open(IN_FILE) as f:
        out = [line for line in f.read().split('\n')]

    i = [ list( map( int, re.findall( "-?\d+", l ) ) ) for l in out]
    s = { ( sx, sy, abs( sx - bx ) + abs( sy - by ) ) for sx, sy, bx, by in i }

    # Part 1
    xl = math.inf
    xh = -math.inf
    for sx, sy, sc in s:
        dx = sc - abs( 2000000 - sy )
        if dx > 0:
            xl = min( xl, sx - dx )
            xh = max( xh, sx + dx )
    print("part1:", xh - xl )


def part2():
    def dist(x, y): return abs(x[0] - y[0]) + abs(x[1] - y[1])
    res = []
    with open(IN_FILE) as f:
        res = f.read().split("\n")
    table = {}
    for line in res:
        a, b = line.split(": ")
        a1, b1 = a.split(", ")
        x1, y1 = int(a1.split("=")[-1]), int(b1.split("=")[-1])
        a2, b2 = b.split(", ")
        beacon1, beacon2 = int(a2.split("=")[-1]), int(b2.split("=")[-1])
        table[(x1, y1)] = (beacon1, beacon2)
    x = 0
    y = 0
    limit = 4000000
    items = list(table.items())
    while y < limit:
        ranges = defaultdict(int)
        for i, j in items:
            highest = dist(i, j) - dist(i, (i[0], y))
            if highest < 0:
                continue
            left = max(0, i[0]-highest)
            right = min(limit, i[0]+highest)
            ranges[left] += 1
            ranges[right+1] -= 1
            cur = 0
        for key in sorted(ranges.keys()):
            cur += ranges[key]
            if cur == 0 and key != limit+1:
                print(key*4000000+y)
                return
        y += 1

part1()  # -> 4873353
part2()  # -> 11600823139120