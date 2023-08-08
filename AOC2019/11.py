"""Advent of Code 2019, day 11

AOC puzzle, 2019, day 11 -- Paint Robot
"""
import logging
import getaoc as ga
import intcode_c as ic
import numpy as np

def get_input():
    """Using the get_input from my getaoc module, read the input from the web
    for the current year and day.
    This particular input parses the input, splits it on the commas, and
    converts it to integers. It then returns a list of ints."""
    data = ga.get_input(11,2019).splitlines()
    data = [int(line) for line in data[0].split(',')]
    return data


# (color, direction)
# color:     0=black; 1=white
# direction: 0=left;  1=right

def part1(program):
    """Solve part 1"""
    logging.info(f"Entering part1()...")

    # define the ship, a 100x100 array
    ship = np.zeros((100,100),dtype=int)
    pixel = (50,50)             # the robot's starting location (middle)
    painted = set()             # set of all the pixels that have been painted
    facing = 0                  # facing direction 0=U, 1=R, 2=D, 3=L
    moves = [(0,-1),(1,0),(0,1),(-1,0)]

    # initialize the robot
    code = ic.Intcode('Paint Robot',program,[1])
    while True:
        code.inputs = [ship[pixel]]
        _, output = code.run()
        color, direction = output
        if color == 1:
            painted.add(pixel)
        
        # paint the current position
        ship[pixel] = color

        # move the robot
        if direction == 0:
            facing -= 1
        else:
            facing += 1
        
        facing = facing % 4
        pixel = list(pixel)
        pixel[0] += moves[facing][0]
        pixel[1] += moves[facing][1]
        pixel = tuple(pixel)
        
        code.output = []    # clear the current outputs
        code.waiting = False   # prep the robot to continue execution

        # out clause
        if code.done:
            break


    return len(painted)



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


    program = get_input()

    part1(program)
    part2()

if __name__ == "__main__":
    main()
