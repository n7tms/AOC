# AOC 2017.20
# solution courtesy of @jlweinkam

import time
import math
current_milli_time = lambda: int(round(time.time() * 1000))
start = current_milli_time()

inputdata=open("AOC2017/20.txt", 'r').read()

lines = inputdata.splitlines()

def compute_time_to_same_direction(i):
  (px, py, pz, vx, vy, vz, ax, ay, az) = part[i]
  tmax = 0
  if (ax > 0 and vx < 0) or (ax < 0 and vy > 0):
    t = math.ceil(-vx / ax)
    if t > tmax:
      tmax = t
  if (ay > 0 and vy < 0) or (ay < 0 and vy > 0):
    t = math.ceil(-vy / ay)
    if t > tmax:
      tmax = t
  if (az > 0 and vz < 0) or (az < 0 and vz > 0):
    t = math.ceil(-vz / az)
    if t > tmax:
      tmax = t

  px += vx * tmax + ax * tmax * (tmax + 1) / 2
  py += vy * tmax + ay * tmax * (tmax + 1) / 2
  pz += vz * tmax + az * tmax * (tmax + 1) / 2

  vx += ax * tmax
  vy += ay * tmax
  vz += az * tmax

  tmax2 = 0
  if (vx > 0 and px < 0) or (vx < 0 and py > 0):
    t = math.ceil(-px / vx)
    if t > tmax2:
      tmax2 = t
  if (vy > 0 and py < 0) or (vy < 0 and py > 0):
    t = math.ceil(-py / vy)
    if t > tmax2:
      tmax2 = t
  if (vz > 0 and pz < 0) or (vz < 0 and pz > 0):
    t = math.ceil(-pz / vz)
    if t > tmax2:
      tmax2 = t

  return tmax + tmax2

def compare(i, o, t):
  (px, py, pz, vx, vy, vz, ax, ay, az) = part[i]
  px += vx * t + ax * t * (t+1)/2
  py += vy * t + ay * t * (t+1)/2
  pz += vz * t + az * t * (t+1)/2
  pi = abs(px) + abs(py) + abs(pz)
  
  vx += ax * t
  vy += ay * t
  vz += az * t
  vi = abs(vx) + abs(vy) + abs(vz)
  
  ai = abs(ax) + abs(ay) + abs(az)

  (px, py, pz, vx, vy, vz, ax, ay, az) = part[o]
  px += vx * t + ax * t * (t+1)/2
  py += vy * t + ay * t * (t+1)/2
  pz += vz * t + az * t * (t+1)/2
  po = abs(px) + abs(py) + abs(pz)
  
  vx += ax * t
  vy += ay * t
  vz += az * t
  vo = abs(vx) + abs(vy) + abs(vz)
  
  ao = abs(ax) + abs(ay) + abs(az)

  if (ai < ao):
    return True
  if (ai == ao):
    if (vi < vo):
      return True
    if (pi < po):
      return True
  return False

i = 0
part = {}
for line in lines:
  col = line.split("<")
  p = col[1]
  v = col[2]
  a = col[3]
  col = p.split(">")[0].split(",")
  px = int(col[0])
  py = int(col[1])
  pz = int(col[2])
  col = v.split(">")[0].split(",")
  vx = int(col[0])
  vy = int(col[1])
  vz = int(col[2])
  col = a.split(">")[0].split(",")
  ax = int(col[0])
  ay = int(col[1])
  az = int(col[2])
  part[i] = (px, py, pz, vx, vy, vz, ax, ay, az)
  i += 1

tmax = 0
best = None
for i in part.keys():
  if (best is None):
    best = i
    continue

  t = compute_time_to_same_direction(i)
  if t > tmax:
    tmax = t

  if compare(i, best, tmax):
    best = i

print("part 1:",best)


def solve(a, v, p):
  A = a/2.0
  B = v + A
  C = p
  if A != 0:
    sq = B*B - 4*A*C
    if sq <= 0:
      return []
    sq = math.sqrt(sq)
    t1 = math.floor((-B - sq) / (2.0 * A) + 0.5)
    t2 = math.floor((-B + sq) / (2.0 * A) + 0.5)
    if (t1 >= 0):
      if (t2 >= 0):
        return [t1, t2]
      return [t1]
    if (t2 >= 0):
      return [t2]
    return []
  if B != 0:
    t = math.floor(C / (1.0 * B) + 0.5)
    if t >= 0:
      return [t]
    return []
  if C != 0:
    return []
  return None

def test(a, v, p, t):
  A = a/2.0
  B = v + A
  C = p
  if A*t*t + B*t + C == 0:
    return True
  return False

collisiontimes = {}
for i in range(len(lines)):
  for o in range(i+1,len(lines)):
    a = part[i][6] - part[o][6]
    v = part[i][3] - part[o][3]
    p = part[i][0] - part[o][0]
    result = solve(a, v, p)
    if result is None:
      a = part[i][7] - part[o][7]
      v = part[i][4] - part[o][4]
      p = part[i][1] - part[o][1]
      result = solve(a, v, p)
      if result is None:
        a = part[i][8] - part[o][8]
        v = part[i][5] - part[o][5]
        p = part[i][2] - part[o][2]
        result = solve(a, v, p)
    if result is not None:
      for t in result:
        a = part[i][7] - part[o][7]
        v = part[i][4] - part[o][4]
        p = part[i][1] - part[o][1]
        if test(a, v, p, t):
          a = part[i][8] - part[o][8]
          v = part[i][5] - part[o][5]
          p = part[i][2] - part[o][2]
          if test(a, v, p, t):
            if t not in collisiontimes.keys():
              collisiontimes[t] = set()
            collisiontimes[t].add((i,o))
            break
k = list(collisiontimes.keys())
k.sort()
s = 0
part_remain = set(range(len(lines)))
for i in k:
  part_remove = set()
  for (i,o) in collisiontimes[i]:
    if i in part_remain and o in part_remain:
      part_remove.add(i)
      part_remove.add(o)
  part_remain = part_remain - part_remove

print("part 2:",len(part_remain))

print((current_milli_time() - start) / 1000.0)