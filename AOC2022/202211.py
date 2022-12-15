# AOC 2022 - Day 11
# https://github.com/xconnected/adventofcode/blob/main/2022/day11.py

import time

IN_FILE = "AOC2022\\inputs\\202211.txt"
# IN_FILE = "AOC2022\\inputs\\202211.sample.txt"

class Monkey:
    def __init__(self, id, items, operation, test, throwT, throwF):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.throwT = throwT
        self.throwF = throwF
        self.inspct = 0
        self.lcm = 0


def calc_lcm(Monkeys):
    lcm = 1
    for x in Monkeys:
        lcm *= x.test
    for x in Monkeys:
        x.lcm = lcm

    return Monkeys        


def parse():
    Monkeys = []
    with open(IN_FILE) as f:
        monkey_data = [monkeys for monkeys in f.read().split('\n\n')]

        for monkey in monkey_data:
            m = monkey.split('\n')

            # id
            id = int(m[0].split()[1][0])

            # items
            itms = m[1].split(':')
            items = [int(i) for i in itms[1].strip().split(',')]

            # operation
            operation = m[2].split()[4:]

            # test
            test = int(m[3].split()[3])
            throwT = int(m[4].split()[5])
            throwF = int(m[5].split()[5])

            x = Monkey(id,items,operation,test,throwT,throwF)
            Monkeys.append(x)
    return Monkeys

def throw_items(Monkeys):
    for k in range(len(Monkeys)):
        m = Monkeys[k]
        m_copy = m.items.copy()
        for i in m_copy:
            m.inspct += 1
            worry = i
            op,val = m.operation
            if val == 'old':
                val = worry
            if op == '*':
                worry = worry * int(val)
            elif op == '+':
                worry = worry + int(val)
            worry = worry // 3
            
            if worry % (int(m.test)) == 0:
                target_monkey = m.throwT
            else:
                target_monkey = m.throwF
                
            for tm in Monkeys:
                if tm.id == target_monkey:
                    tm.items.append(worry)
                    break
            m.items.remove(i)
    return Monkeys

def throw_items2(Monkeys):
    for k in range(len(Monkeys)):
        m = Monkeys[k]
        m_copy = m.items.copy()
        for i in m_copy:
            m.inspct += 1
            worry = i
            op,val = m.operation
            if val == 'old':
                val = worry
            if op == '*':
                worry = worry * int(val)
            elif op == '+':
                worry = worry + int(val)
            
            worry = worry % m.lcm
            if worry % m.test == 0:
                target_monkey = m.throwT
            else:
                target_monkey = m.throwF
                
            for tm in Monkeys:
                if tm.id == target_monkey:
                    tm.items.append(worry)
                    break
            m.items.remove(i)
    return Monkeys

def active_monkeys(Monkeys):
    am = []
    for m in Monkeys:
        am.append(m.inspct)

    # sort am
    am.sort()
    print(am)
    return am[6] * am[7]
    # return am[2] * am[3]


def part1(data):            # => 111210
    """Solve part 1."""
    x = throw_items(data)
    for j in range(19):
        x = throw_items(x)

    return active_monkeys(x)

def part2(data):            # => 15447387620
    """Solve part 2."""
    data = calc_lcm(data)
    x = throw_items2(data)
    for j in range(10000):
        # print(j)
        x = throw_items2(x)

    return active_monkeys(x)

if __name__ == "__main__":
    timestart = time.time()

    puzzle_input = parse()
    # print(puzzle_input)

    # print("part 1:",part1(puzzle_input))
    print("part 2:",part2(puzzle_input))
    
    timeend = time.time()
    print("Execution time: ", "{:.7f}".format(round(timeend-timestart,7)))

