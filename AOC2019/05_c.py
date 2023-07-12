from intcode_c import Intcode

IN_File = "05.txt"

def parse():
    with open(IN_File) as f:
        out = f.read().split(',')
    prgm = list(map(int,out))
    return prgm



# p1 = Intcode("part1", [3,3,1105,-1,9,1101,0,0,12,4,12,99,1], [1])
p1 = Intcode("part1", parse(), [1])
print(f"Part 1: {p1.run()}")

p2 = Intcode("part2", parse(), [5])
print(f"Part 2: {p2.run()}")
