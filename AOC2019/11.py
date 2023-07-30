# Advent of Code 2019: day 11
import getaoc as ga
import intcode_c as ic



def get_input():
    data = ga.get_input(11,2019).splitlines()
    data = [int(line) for line in data[0].split(',')]
    return data



def part1(program):
    code = ic.Intcode('Paint Robot',program,[1])
    print(code.run())

    return None



def part2() -> None:
    ...

def main():
    program = get_input()
    part1(program)
    part2()

if __name__ == "__main__":
    main()