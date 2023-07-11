from intcode_c import Intcode


program = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0]
p = Intcode("A",program)
print(f"Part 1: {p.run()}")

# Part 2

found = False
for i in range(75):
    if found:
        break
    for j in range(80):
        program[1] = i
        program[2] = j
        q = Intcode("Part2",program)

        if q.run() == 19690720:
            out = (i * 100) + j
            print(f"Part 2: {out}")
            found = True
            break

