from intcode_c import Intcode
from itertools import permutations

IN_File = "07.txt"

def parse():
    with open(IN_File) as f:
        out = f.read().split(',')
    prgm = list(map(int,out))
    return prgm


# p1 = Intcode("part1", [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0], [0,4])
# p1 = Intcode("part1", parse(), [1])
# print(f"Part 1: {p1.run()[1]}")

# testpgrm = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
testpgrm = parse()

phases = list(permutations(range(0,5)))

highestsignal = 0
for phase in phases:
    ampa = Intcode("part1", testpgrm, [phase[0],0])
    ampb = Intcode("part1", testpgrm, [phase[1],ampa.run()[1][0]])
    ampc = Intcode("part1", testpgrm, [phase[2], ampb.run()[1][0]])
    ampd = Intcode("part1", testpgrm, [phase[3], ampc.run()[1][0]])
    ampe = Intcode("part1", testpgrm, [phase[4], ampd.run()[1][0]])
    thrustersignal = ampe.run()[1][0]
    if thrustersignal > highestsignal:
        highestsignal = thrustersignal

print(f"Part 1: {highestsignal}")

testpgrm = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
phase = (9,8,7,6,5)
# phases = list(permutations(range(5,10)))

thrustersignal = 0
ampa = Intcode("ampa", testpgrm, [phase[0],0])
while True:
    ampb = Intcode("ampb", testpgrm, [phase[1],ampa.run()[1][0]])
    ampc = Intcode("ampc", testpgrm, [phase[2], ampb.run()[1][0]])
    ampd = Intcode("ampd", testpgrm, [phase[3], ampc.run()[1][0]])
    ampe = Intcode("ampe", testpgrm, [phase[4], ampd.run()[1][0]])
    thrustersignal = ampe.run()[1][0]
    if thrustersignal ==139629729:
        break
    else:
        ampa = Intcode("ampa", testpgrm, [phase[0], thrustersignal])

print(thrustersignal)
