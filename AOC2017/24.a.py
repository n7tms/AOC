# @mkeeter
data = []
with open('AOC2017/24.txt', 'r') as f:
    for line in f.readlines():
        a, b = line.split('/')
        data.append((int(a), int(b)))
    # data = [tuple(map(int, line.split("/"))) for line in f]

bridge = ([], 0)

def run(b, d):
    available = [a for a in d if b[1] in a]
    if len(available) == 0:
        yield b
    else:
        for a in available:
            d_ = d.copy()
            d_.remove(a)
            for q in run((b[0] + [a], a[0] if b[1] == a[1] else a[1]), d_):
                yield q

# part 1
ms = max(map(lambda bridge: sum([a + b for a, b in bridge[0]]), run(bridge, data))) 
print(ms)

# part 2
max_len = max(map(lambda bridge: len(bridge[0]), run(bridge, data)))
long = filter(lambda bridge: len(bridge[0]) == max_len, run(bridge, data))
ml = max(map(lambda bridge: sum([a + b for a, b in bridge[0]]), long)) 
print(ml)