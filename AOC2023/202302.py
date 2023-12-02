# AOC 2023 day 2: Cube Conundrum
#

import numpy as np

IN_FILE = "AOC2023\\inputs\\202302.in"
# IN_FILE = "AOC2023\\inputs\\202302.sample.in"

# IN_FILE = "./inputs/202302.in"
# IN_FILE = "./inputs/202302.sample.in"


def parse(puzzle_input):
    """
    Part Parse
    """
    with open(IN_FILE) as fp:
        out = []
        data = fp.read().splitlines()
    return data
           

def part1(data):            # => 2278
    """
    Solve part 1
    Given the number of each colored cube in the bag, determine
    which games are possible. If it is possible, store that game's
    ID in possible_games[].
    The solution is the sum of the ID's in possible_game[].
    """
    game_tokens = {"red":12,"green":13,"blue":14}       
    possible_games = []

    for game in data:
        id, drawn = game.split(":")
        id = int(id.split(" ")[1])
        
        draws = drawn.split(";")
        valid = True
        for x in draws:
            cubes = x.split(",")
            for cube in cubes:
                n,c = cube.strip().split(" ")
                if int(n) > game_tokens[c]:
                    valid = False
                    break
        if valid:
            possible_games.append(id)

    return sum(possible_games)


def part2(data):            # => 67953
    """
    Solve part 2
    Iterate through each game, generating a dictionary of the minimun qty of cubes required to play each game.
    At the end of each game, multiply the quantities of each color together and append product to powers[].
    The solution is the sum of all of the powers[].
    """
    powers = []

    for game in data:
        rgb = {"red":0, "green":0, "blue":0}
        id, drawn = game.split(":")
        id = int(id.split(" ")[1])
        
        draws = drawn.split(";")
        valid = True
        for x in draws:
            cubes = x.split(",")
            for cube in cubes:
                n,c = cube.strip().split(" ")
                if rgb[c] < int(n):
                    rgb[c] = int(n)
        
        powers.append(np.prod(list(rgb.values())))

    return sum(powers)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    print(f"part 1: {str(part1(data))}")

    # data = parse2(puzzle_input)
    print(f"part 2: {str(part2(data))}")


if __name__ == "__main__":
    solve(IN_FILE)
        