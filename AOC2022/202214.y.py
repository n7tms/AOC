# https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day14p2.py

b = set()

abyss = 0
# IN_FILE = "AOC2022\\202214.txt"
IN_FILE = "AOC2022/202214.sample.txt"
with open(IN_FILE) as f:
    out = f.read().split('\n')
# for line in open(0):
for line in out:
    x = [list(map(int, p.split(","))) for p in line.strip().split(" -> ")]
    for (x1, y1), (x2, y2) in zip(x, x[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                b.add(x + y * 1j)
                abyss = max(abyss, y + 1)

t = 0

while 500 not in b:
    s = 500
    while True:
        if s.imag >= abyss:
            break
        if s + 1j not in b:
            s += 1j
            continue
        if s + 1j - 1 not in b:
            s += 1j - 1
            continue
        if s + 1j + 1 not in b:
            s += 1j + 1
            continue
        break
    b.add(s)
    t += 1

print(t)
