import os

DAY = '08'
# IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+"-sample.txt")
IN_FILE = os.path.join("AOC2025","inputs","2025-"+str(DAY)+".in")

with open(IN_FILE, "r") as puzzleInput:
    boxes = [[int(n) for n in line.strip().split(",")] for line in puzzleInput.readlines()]

distances, circuits, merged_index, box_index, p1_limit = [], [], set(), set(range(0, len(boxes))), 1000

for b1, (x1, y1, z1) in enumerate(boxes):
    for b2, (x2, y2, z2) in enumerate(boxes):
        if b2 <= b1:
            continue
        distances.append((b1, b2, (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2))

for i, (b1, b2, distance) in enumerate(sorted(distances, key=lambda x: x[2])):
    connection = {b1, b2}
    for c, circuit in enumerate(circuits):
        if connection & circuit:
            circuits[c].update(connection)
            # check to see if any circuits can be merged
            if i <= p1_limit - 1 and connection <= merged_index:
                for cc, circuit_check in enumerate(circuits):
                    if c != cc and connection & circuit_check:
                        circuits[c].update(circuit_check)
                        circuits.pop(cc)
                        break
            break
    else:
        circuits.append(connection)
    merged_index.update(connection)
    box_index -= connection
    
    if i == p1_limit - 1:
        circuits.sort(key=len, reverse=True)
        print(f"Part 1: {len(circuits[0]) * len(circuits[1]) * len(circuits[2])}")

    if not box_index:
        print(f"Part 2: {boxes[b1][0] * boxes[b2][0]}")
        break