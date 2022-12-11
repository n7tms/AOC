# AOC 2022 - Day 11
# https://github.com/xconnected/adventofcode/blob/main/2022/day11.py

from math import lcm


def display_monkey(monkey_nb, monkeys):

    print('nb: ', monkeys[monkey_nb]['nb'])
    print('items: ', monkeys[monkey_nb]['item'])
    print('operation: ', monkeys[monkey_nb]['operation'])
    print('test: ', monkeys[monkey_nb]['test'])
    print('test_true: ', monkeys[monkey_nb]['test_true'])
    print('test_false: ', monkeys[monkey_nb]['test_false'])
    print('counter: ', monkeys[monkey_nb]['counter'])


def display_levels(monkeys):
    for nb in range(len(monkeys)):
        print('Monkey ' + str(nb) + ' item: ', monkeys[nb]['item'])


def display_counter(monkeys):
    for nb in range(len(monkeys)):
        print('Monkey ' + str(nb) + ' counter: ', monkeys[nb]['counter'])


def load_monkeys(fn):
    monkey = {}
    monkeys = []

    with open(fn) as f:
        lines = f.readlines()

        for line in lines:
            line_stripped = line.strip()

            if line_stripped.startswith("Monkey"):
                monkey_nb = int(line_stripped.split(" ")[1][:-1])

            elif line_stripped.startswith("Starting"):
                monkey_items = line_stripped.split(":")[1].split(",")
                monkey_items = [int(s.strip()) for s in monkey_items]

            elif line_stripped.startswith("Operation"):
                monkey_operation = (line_stripped.split("=")[1]).split(" ")

            elif line_stripped.startswith("Test"):
                monkey_divider = int(line_stripped.split("by")[1].strip())

            elif line_stripped.startswith("If true"):
                monkey_test_throw_true = int(line_stripped.split("monkey")[1])

            elif line_stripped.startswith("If false"):
                monkey_test_throw_false = int(line_stripped.split("monkey")[1])
                monkey['nb'] = monkey_nb
                monkey['items'] = monkey_items
                monkey['operation'] = monkey_operation
                monkey['divider'] = monkey_divider
                monkey['test_true'] = monkey_test_throw_true
                monkey['test_false'] = monkey_test_throw_false
                monkey['counter'] = 0
                monkeys.append(monkey.copy())
    return monkeys


def operation(old, operand):

    if operand[3].strip() == 'old':
        param = old
    else:
        param = int(operand[3])

    if operand[2].strip() == '+':
        new = old + param

    if operand[2].strip() == '*':
        new = old * param

    return new


def process(rounds, monkeys, worry_relief, limiter):

    for _ in range(rounds):
        for monkey_nb in range(len(monkeys)):

            # Iterate items
            for item in monkeys[monkey_nb]['items']:

                # Update inspection counter
                monkeys[monkey_nb]['counter'] += 1

                # Perform operation
                new = operation(item, monkeys[monkey_nb]['operation'])

                # Handle worry relief or alternative
                if worry_relief:
                    new = new // 3
                elif new > limiter:
                    new = new % limiter

                # Throw item
                if new % monkeys[monkey_nb]['divider'] == 0:
                    to_monkey = monkeys[monkey_nb]['test_true']
                else:
                    to_monkey = monkeys[monkey_nb]['test_false']

                monkeys[to_monkey]['items'].append(int(new))

            # Clear items
            monkeys[monkey_nb]['items'].clear()

    return monkeys


def get_level_of_monkey_business(monkeys):

    activities = []
    for monkey in monkeys:
        activities.append(monkey['counter'])
    activities.sort(reverse=True)
    return activities[0] * activities[1]


if __name__ == '__main__':

    print("Part 1")
    monkeys = load_monkeys(r"AOC2022\\202211.txt")
    limiter = lcm(*[monkey['divider'] for monkey in monkeys])
    print("limiter ", limiter)
    process(20, monkeys, True, limiter)
    display_counter(monkeys)
    print(get_level_of_monkey_business(monkeys))

    print()
    print("Part 2")
    monkeys = load_monkeys(r"AOC2022\\202211.txt")
    limiter = lcm(*[monkey['divider'] for monkey in monkeys])
    print("limiter ", limiter)
    process(10000, monkeys, False, limiter)
    display_counter(monkeys)
    print(get_level_of_monkey_business(monkeys))