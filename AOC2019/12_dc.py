""" Advent of Code 2019, day 12

    AOC puzzle, 2019, day 12 -- The N-Body Problem
"""

# This is 2019.12 all over again, but I just learned about dataclasses
# and want to write this Moon class using dataclasses.

from dataclasses import dataclass, field
from itertools import combinations
import getaoc as ga
import logging
import re
import time

def get_input():
    """ Using the get_input from my getaoc module, read the input from the web
        for the current year and day.

        Retrieve the data and parse it using regex. 
        It creates a Moon object for each line and returns a list of Moons.

        <x=7, y=10, z=17>
    """
    data = ga.get_input(12,2019).splitlines()
    
    for line in data:
        match = re.search(r'<x=(-*\d+), y=(-*\d+), z=(-*\d+)', line)
        logging.info(f"Matched Moon: {match.group(1)} {match.group(2)} {match.group(3)}")
        m = Moon(int(match.group(1)), int(match.group(2)), int(match.group(3)))
    return Moon.get_moons()

@dataclass
class Moon:
    posx: int
    posy: int
    posz: int
    velx: int = field(init=False)
    vely: int = field(init=False)
    velz: int = field(init=False)

    moons = []

    def __post_init__(self):
        self.velx = 0
        self.vely = 0
        self.velz = 0
        self.moons.append(self)

    @classmethod
    def get_moons(cls):
        return list(Moon.moons)
    
    @classmethod
    def clear_moons(cls):
        Moon.moons.clear()

    @classmethod
    def compare(cls) -> None:
        """ Compare 'this' moon to the other moon.
            Returns the other moon."""
        for pair in combinations(Moon.moons,2):
            m1,m2 = pair
            if m1.posx < m2.posx:
                m1.velx += 1
                m2.velx -= 1
            elif m1.posx > m2.posx:
                m1.velx -= 1
                m2.velx += 1

            if m1.posy < m2.posy:
                m1.vely += 1
                m2.vely -= 1
            elif m1.posy > m2.posy:
                m1.vely -= 1
                m2.vely += 1

            if m1.posz < m2.posz:
                m1.velz += 1
                m2.velz -= 1
            elif m1.posz > m2.posz:
                m1.velz -= 1
                m2.velz += 1

    @classmethod
    def update_positions(cls):
        for moon in Moon.moons:
            moon.posx += moon.velx
            moon.posy += moon.vely
            moon.posz += moon.velz
    
    def potential_energy(self) -> int:
        """sum of abs of postions"""
        return abs(self.posx) + abs(self.posy) + abs(self.posz)
    
    def kinetic_energy(self) -> int:
        """sum of abs of velocities"""
        return abs(self.velx) + abs(self.vely) + abs(self.velz)

    def total_energy(self) -> int:
        return self.potential_energy() * self.kinetic_energy()

    def state(self) -> str:
        return f"{self.posx},{self.posy},{self.posz} ({self.velx},{self.vely},{self.velz})"
          
    def __str__(self):
        return f"{self.posx},{self.posy},{self.posz} ({self.velx},{self.vely},{self.velz})"


def part1(moons):        # -> 9958
    """"""

    for _ in range(1000):
        # compare pairs of moons to each other and update velocities
        Moon.compare()

        # based on new velocities, update each moon's position
        Moon.update_positions()

    total_energy = sum([m.total_energy() for m in moons])
    return total_energy
    
    

def part2(moons):   # -> 318382803780324
    """ This is a brute-force solution!
        By my calculations, it would take ~96,000 days to solve.
        The answer was generated using Kresimir Lukin's LCM solution.
    """

    states = list()

    # save the initial state
    state = list()
    for m in moons:
        state.append(f"{m}")
    states.append(state)

    steps = 0
    while True:
        # compare pairs of moons to each other and update velocities
        for pair in combinations(moons,2):
            m1,m2 = pair
            m2 = m1.compare(m2)

        # based on new velocities, update each moon's position
        for m in moons:
            m.update_positions()

        # save the current state
        state = list()
        for m in moons:
            state.append(f"{m}")
        
        if state in states:
            return steps
        else:
            states.append(state)       
            steps += 1



def main():
    """solve each part and print the solutions"""

    # Instantiate the logger
    # log_level = logging.DEBUG
    # log_level = logging.INFO
    log_level = logging.WARNING
    log_format = '%(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=log_level, format=log_format)

    moons = get_input()
    st = time.time()
    print(f"Total Energy: {part1(moons)}")
    et = time.time()
    print(f"Elapsed time: {et - st} seconds")

    # start over for part2
    Moon.clear_moons()
    moons = get_input()

    st = time.time()
    # print(f"Steps: {part2(moons)}")
    et = time.time()
    print(f"Elapsed time: {et - st} seconds")

if __name__ == "__main__":
    main()
