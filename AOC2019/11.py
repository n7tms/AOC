"""Advent of Code 2019, day 11

AOC puzzle, 2019, day 11 -- Paint Robot
"""
import logging
import getaoc as ga
import intcode_c as ic

def get_input():
    """Using the get_input from my getaoc module, read the input from the web
    for the current year and day.
    This particular input parses the input, splits it on the commas, and
    converts it to integers. It then returns a list of ints."""
    data = ga.get_input(11,2019).splitlines()
    data = [int(line) for line in data[0].split(',')]
    return data



def part1(program):
    """Solve part 1"""
    logging.info(f"Entering part1()...")

    code = ic.Intcode('Paint Robot',program,[1])
    print(code.run())

    return None



def part2() -> None:
    """Solve part 2"""
    ...

def main():
    """solve each part and print the solutions"""

    # Instantiate the logger  (Look at this for color: https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output)
    log_level = logging.DEBUG
    # log_level = logging.INFO
    # log_level = logging.WARNING
    log_format = '%(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=log_level, format=log_format)


    # program = get_input()
    program = ""
    part1(program)
    part2()

if __name__ == "__main__":
    main()
