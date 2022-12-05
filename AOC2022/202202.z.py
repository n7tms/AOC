def score(p1, p2):
    if (p1 - 1) % 3 == p2:
        return p2 + 1
    elif (p2 - 1) % 3 == p1:
        return p2 + 7
    return p2 + 4


with open("202202.sample.txt", "r") as f:
    data = f.read().splitlines()
    print(data)
    data = [line.split() for line in data]
    print(data)
    data = [(ord(p1) - ord("A"), ord(p2) - ord("X")) for p1, p2 in data]
    print(data)

moves = [(p1, (p1 + p2 - 1) % 3) for p1, p2 in data]

print(sum(score(p1, p2) for p1, p2 in data))
print(sum(score(p1, p2) for p1, p2 in moves))


def day2(s, part2=False):  
  total = 0  
  for line in s.strip('\n').split('\n'):  
    i, j = ord(line[0]) - ord('A'), ord(line[2]) - ord('X')  
    total += j * 3 + (i + j + 2) % 3 + 1 if part2 else (j - i + 1) % 3 * 3 + j + 1  
  return total
  