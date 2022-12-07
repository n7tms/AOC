IN_FILE = "AOC2015/201507.txt"

def parse():
    """Parse input."""
    with open(IN_FILE) as f:
        out = [(line) for line in f.read().split('\n')]
    return out

commands =  parse()


# Adapted from 'Tryneus' code

calc = dict()
results = dict()

# separate the operands from the results
for command in commands:
    (ops, res) = command.split('->')
    calc[res.strip()] = ops.strip().split(' ')

def calculate(name):
    try:
        return int(name)
    except ValueError:
        pass

    if name not in results:
        ops = calc[name]
        if len(ops) == 1:
            res = calculate(ops[0])
        else:
            op = ops[-2]
            if op == 'AND':
              res = calculate(ops[0]) & calculate(ops[2])
            elif op == 'OR':
              res = calculate(ops[0]) | calculate(ops[2])
            elif op == 'NOT':
              res = ~calculate(ops[1]) & 0xffff
            elif op == 'RSHIFT':
              res = calculate(ops[0]) >> calculate(ops[2])
            elif op == 'LSHIFT':
              res = calculate(ops[0]) << calculate(ops[2])
        results[name] = res
    return results[name]

print("a: %d" % calculate('a'))

# part 1: 3176
# part 2: 14710