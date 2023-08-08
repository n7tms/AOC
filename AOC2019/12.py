""" Advent of Code 2019, day 12

    AOC puzzle, 2019, day 12 -- The N-Body Problem
"""
import logging
import getaoc as ga
import intcode_c as ic

def get_input():
    """Using the get_input from my getaoc module, read the input from the web
    for the current year and day.
    This particular input parses the input, splits it on the commas, and
    converts it to integers. It then returns a list of ints."""
    data = ga.get_input(12,2019).splitlines()
    data = [int(line) for line in data[0].split(',')]
    return data

class Moon:

    def __init__(self,px, py, pz):
        self.posx = px
        self.posy = py
        self.posz = pz
        self.velx = 0
        self.vely = 0
        self.velz = 0
        self.states = list()

    def compare(self, other_moon):
        """ Compare 'this' moon to the other moon.
            Returns the other moon."""
        if self.posx < other_moon.posx:
            self.velx += 1
            other_moon.velx -= 1
        elif self.posx > other_moon.posx:
            self.velx -= 1
            other_moon.velx += 1

        if self.posy < other_moon.posy:
            self.vely += 1
            other_moon.vely -= 1
        elif self.posy > other_moon.posy:
            self.vely -= 1
            other_moon.vely += 1

        if self.posz < other_moon.posz:
            self.velz += 1
            other_moon.velz -= 1
        elif self.posz > other_moon.posz:
            self.velz -= 1
            other_moon.velz += 1
        
        return other_moon
    
    def update_positions(self):
        self.posx += self.velx
        self.posy += self.vely
        self.posz += self.velz

    def save_state(self):
        self.states.append(self.state)

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
    
    def previous_state(self) -> bool:
        return True if self.state in self.states else False
            

    def __str__(self):
        return f"{self.posx},{self.posy},{self.posz} ({self.velx},{self.vely},{self.velz})"


def compare_moons(moon1, moon2) -> list:
    """"""

def apply_velocities(moon) -> dict:
    """"""

def part1():        # -> 9958
    """"""
    m1 = Moon(7,10,17)
    m2 = Moon(-2,7,0)
    m3 = Moon(12,5,12)
    m4 = Moon(5,-8,6)

    for _ in range(1000):
        m2 = m1.compare(m2)
        m3 = m1.compare(m3)
        m4 = m1.compare(m4)
        m3 = m2.compare(m3)
        m4 = m2.compare(m4)
        m4 = m3.compare(m4)

        m1.update_positions()
        m2.update_positions()
        m3.update_positions()
        m4.update_positions()

    print(m1)
    print(m2)
    print(m3)
    print(m4)

    total_energy = m1.total_energy() + m2.total_energy() + m3.total_energy() + m4.total_energy()
    return total_energy
    
    

def part2():
    """"""
    m1 = Moon(7,10,17)
    m2 = Moon(-2,7,0)
    m3 = Moon(12,5,12)
    m4 = Moon(5,-8,6)

    steps = 0
    while True:
        m2 = m1.compare(m2)
        m3 = m1.compare(m3)
        m4 = m1.compare(m4)
        m3 = m2.compare(m3)
        m4 = m2.compare(m4)
        m4 = m3.compare(m4)

        m1.update_positions()
        m2.update_positions()
        m3.update_positions()
        m4.update_positions()

        if m1.previous_state():
            break

        m1.save_state()
        m2.save_state()
        m3.save_state()
        m4.save_state()
        
        steps += 1

    return steps


def main():
    """solve each part and print the solutions"""

    # Instantiate the logger
    # log_level = logging.DEBUG
    # log_level = logging.INFO
    log_level = logging.WARNING
    log_format = '%(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=log_level, format=log_format)

    # program1 = get_input()
    # program2 = get_input()

    # part1(program1)
    # part2(program2)

    print(f"Total Energy: {part1()}")
    print(f"Steps: {part2()}")

if __name__ == "__main__":
    main()
