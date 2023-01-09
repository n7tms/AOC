# @obijywk
f = open("AOC2017/24.txt", "r")
all_comps = []
for line in f:
  all_comps.append(tuple([int(x) for x in line.strip().split("/")]))

def pick_next_port(a, b):
  if b[0] == a[0] or b[0] == a[1]:
    return b[1]
  return b[0]

def score_bridge(bridge):
  s = 0
  for c in bridge:
    # s += c[0]
    # s += c[1]
    s += sum(c)
  return s

strongest_bridge = []
strongest_bridge_score = 0

longest_bridge = []
longest_bridge_score = 0

def check(comps, bridge):
  global strongest_bridge, strongest_bridge_score, longest_bridge, longest_bridge_score
  if len(bridge) >= 2:
    next_port = pick_next_port(bridge[-2], bridge[-1])
  elif len(bridge) == 1:
    next_port = pick_next_port((0,0), bridge[-1])
  else:
    next_port = 0
  found_a_bridge = False
  for comp in comps:
    if next_port in list(comp):
      found_a_bridge = True
      next_bridge = bridge[:]
      next_bridge.append(comp)
      next_comps = comps[:]
      next_comps.remove(comp)
      check(next_comps, next_bridge)
  if not found_a_bridge:
    s = score_bridge(bridge)
    if s > strongest_bridge_score:
      strongest_bridge = bridge
      strongest_bridge_score = s
    if len(bridge) >= len(longest_bridge):
      if s > longest_bridge_score:
        longest_bridge = bridge
        longest_bridge_score = s

check(all_comps, [])
print(strongest_bridge_score)
print(longest_bridge_score)