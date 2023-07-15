# AOC 2019 Day 9
#
import getaoc as ga
from intcode_c import Intcode


def get_input():
    # data = ga.get_input(9,2019).splitlines()
    data = ['109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99']    # SAMPLE DATA
    # data =['1102,34915192,34915192,7,4,7,99,0']                             # SAMPLE DATA
    # --- do other parsing here if necessary ---
    # convert the lines of strings to list of numbers
    data = [int(line) for line in data[0].split(',')]


    # return the parsed data
    return data


def part1(data):
    ic = Intcode('BOOST',data)
    print(ic.run())


def part2(data):
    ...



if __name__ == "__main__":
    part1(get_input())
    part2(get_input())