""" Advent of Code 2019, day 12

    AOC puzzle, 2019, day 12 -- The N-Body Problem
"""
import logging
import getaoc as ga
import intcode_c as ic

def get_input():
    """ Using the get_input from my getaoc module, read the input from the web
        for the current year and day.

        Retrieve the data and parse it using regex. 
        It creates a Moon object for each line and returns a list of Moons.

        <x=7, y=10, z=17>
    """
    moons = list()
    data = ga.get_input(12,2019).splitlines()
    
    for line in data:
        match = re.search(r'<x=(-*\d+), y=(-*\d+), z=(-*\d+)', line)
        logging.info(f"Matched Moon: {match.group(1)} {match.group(2)} {match.group(3)}")
        # print(match.group(1), match.group(2), match.group(3))
        m = Moon(match.group(1), match.group(2), match.group(3))
        moons.append(m)

    return moons

class Moon:

    def __init__(self,px, py, pz):
        self.posx = px
        self.posy = py
        self.posz = pz
        self.velx = 0
        self.vely = 0
        self.velz = 0
        # self.states = list()
        # self.save_state()

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

    # def save_state(self):
    #     self.states.append(self.state())

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
    
    # def previous_state(self) -> bool:
    #     return True if self.state() in self.states else False

    def __str__(self):
        return self.state()


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
    # m1 = Moon(-1,0,2)
    # m2 = Moon(2,-10,-7)
    # m3 = Moon(4,-8,8)
    # m4 = Moon(3,5,-1)
    m1 = Moon(7,10,17)
    m2 = Moon(-2,7,0)
    m3 = Moon(12,5,12)
    m4 = Moon(5,-8,6)

    states = list()
    states.append(f"{m1} {m2} {m3} {m4}")
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

        steps += 1
        if steps % 1000000 == 0:
            print(steps // 1000000, end=" ")

        current_state = f"{m1} {m2} {m3} {m4}"
        if current_state in states:
            print(current_state)
            return steps

        # if m1.previous_state():
        #     print(f"m1 after {steps} steps. State: {m1}")
        # if m2.previous_state():
        #     print(f"m2 after {steps} steps. State: {m2}")
        # if m3.previous_state():
        #     print(f"m3 after {steps} steps. State: {m3}")
        # if m4.previous_state():
        #     print(f"m4 after {steps} steps. State: {m4}")

        # if m1.previous_state() and m2.previous_state() and m3.previous_state() and m4.previous_state():
        #     print(f"all at previous state after {steps}")
        #     break

        # m1.save_state()
        # m2.save_state()
        # m3.save_state()
        # m4.save_state()
        
    return steps


def main():
    """solve each part and print the solutions"""

    # Instantiate the logger
    log_level = logging.DEBUG
    # log_level = logging.INFO
    # log_level = logging.WARNING
    log_format = '%(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=log_level, format=log_format)

    program1 = get_input()
    # program2 = get_input()

    # part1(program1)
    # part2(program2)

    # print(f"Total Energy: {part1()}")

    st = time.time()    # start time
    print(f"Steps: {part2()}")
    et = time.time()    # end time
    print(f"Execution time: {et - st} seconds")

if __name__ == "__main__":
    main()
