# AOC 2022 - Day 16
# @CorvusCalvaria

import re
 
IN_FILE = "AOC2022\\inputs\\202216.txt"

class Valve:
    def __init__(self, id, name, flow):
        self.name = name
        self.id = id
        self.flow = flow
        self.out_dir = []
 
foo, valves, valves_of_interest = [], [], []
start_valve = None
with open(IN_FILE, 'r') as inp:
    foo = inp.read().split('\n')
 
for f in range(len(foo)):
    foo[f] = re.split(' |=', foo[f].replace(',','').replace(';',''))
    valves.append(Valve(f, foo[f][1], int(foo[f][5])))
    if foo[f][1] == 'AA':
        start_valve = valves[-1]
    elif int(foo[f][5]) > 0:
        valves_of_interest.append(valves[-1])
for f in range(len(foo)):
    for v in range(len(foo)):
        if f != v and valves[v].name in foo[f][10:]:
            valves[v].out_dir.append(valves[f])
 
dist = [[1000 for x in range(len(valves))] for y in range(len(valves))]
for v in valves:
    dist[v.id][v.id] = 0
    check = [v]
    n = 1
    while len(check) > 0:
        for c in range(len(check)):
            for o in check[0].out_dir:
                if dist[v.id][o.id] > n:
                    dist[v.id][o.id] = n
                    check.append(o)
            check = check[1:]
        n += 1
 
solutions = []
def max_pressure(current_valve, score, elapsed, visited, turn_count, record_sols):
    if record_sols:
        global solutions
        solutions.append([score, visited])
    vals = []
    for v in valves_of_interest:
        time_after = dist[current_valve.id][v.id]+elapsed+1
        if v is not current_valve and time_after <= turn_count and v.id not in visited:
            vals.append(max_pressure(v, score+(v.flow*(turn_count-time_after)), time_after, visited + [v.id], turn_count, record_sols))
    if len(vals) == 0:
        return score
    return max(vals)
 
print(max_pressure(start_valve, 0, 0, [], 30, False)) 
 
m = 0
count = 0
max_pressure(start_valve, 0, 0, [], 26, True)
for s in solutions:
    second_go = max_pressure(start_valve, s[0], 0, s[1], 26, False)
    if second_go > m:
        m = second_go
print(m)