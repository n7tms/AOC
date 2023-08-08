""" Advent of Code 2019, day 11

    AOC puzzle, 2019, day 11 -- Paint Robot
"""
import logging
import getaoc as ga
import intcode_c as ic
import numpy as np
from matplotlib import pyplot as plt

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


def part12(program, start_tile_color) -> None:
    """ Solves part 1 and 2.
        Part 1 only needs to output the number of painted tiles.
        Part 2 only needs to plot the painted ship.
        This functions does both for both parts."""
    
    logging.info(f"Entering part2()...")

    # define the ship, a 100x100 array
    ship = np.zeros((200,200),dtype=int)
    pixel = (50,50)             # the robot's starting location (middle)
    painted = set()             # set of all the pixels that have been painted
    facing = 0                  # facing direction 0=U, 1=R, 2=D, 3=L
    moves = [(-1,0),(0,1),(1,0),(0,-1)]

    ship[pixel] = start_tile_color

    # initialize the robot
    code = ic.Intcode('Paint Robot',program,[1])
    while True:
        code.inputs = [ship[pixel]]
        _, output = code.run()
        color, direction = output
        if color == 1:
            painted.add(pixel)
        
        # paint the current position (tile)
        ship[pixel] = color

        # move the robot
        facing += 1 if direction else -1
        facing = facing % 4
        pixel = tuple(map(lambda x,y: x+y, pixel,moves[facing]))

        # clear the outputs and prep the robot to continue execution        
        code.output = []    
        code.waiting = False

        # If the robot (program) hits opcode=99, then it is really done!
        if code.done:
            break

    # print the number of painted tiles
    print(f"Painted Tiles: {len(painted)}")

    # plot the painted ship
    plt.imshow(ship, interpolation='none')
    plt.show()
    
    return None

def main():
    """solve each part and print the solutions"""

    # Instantiate the logger  (Look at this for color: https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output)
    # log_level = logging.DEBUG
    # log_level = logging.INFO
    log_level = logging.WARNING
    log_format = '%(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=log_level, format=log_format)

    program1 = get_input()
    program2 = get_input()

    part12(program1,0)
    part12(program2,1)


if __name__ == "__main__":
    main()
