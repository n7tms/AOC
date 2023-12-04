# AOC 2023 day 4: 
#

import aoc_utils as aoc
import numpy as np

# IN_FILE = "AOC2023\\inputs\\202304.in"
# IN_FILE = "AOC2023\\inputs\\202304.sample.txt"

IN_FILE = "AOC2023/inputs/202304.in"
# IN_FILE = "AOC2023/inputs/202304.sample.txt"

def parse(puzzle_input):
    """
    Parse

        Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    """
    with open(IN_FILE) as fp:
        out = []
        data = fp.read().splitlines()

    return data


def part1(data):            # => 23941
    """
    Solve part 1

    Points for matching cards....
    """
    cards = []
    total_points = 0
    for card in data:
        _,line = card.split(":")
        winners,mine = line.split("|")

        # add the number to the list if it isn't ""
        w = [x for x in winners.split(" ") if x]
        m = [x for x in mine.split(" ") if x]

        # points for each of my numbers (m) in the winning numbers (w)
        # points double for each matching point ... 2^points
        points = sum(x in m for x in w)
        if points > 0:
            total_points += np.power(2,points-1)

    return total_points

def part2(data):            # => 5571760
    """
    Solve part 2
    
    Now, everything is made up and the points don't matter!
    Win additional cards based on matches.
    """
    count_of_cards = {}

    total_points = 0
    for card in data:
        c,line = card.split(":")

        # get the card number and add it to the dictionary (count_of_cards), if it isn't already there.
        _,s_card_num = c.strip().split("Card ")
        i_card_num = int(s_card_num.strip())
        if not i_card_num in count_of_cards:
            count_of_cards[i_card_num] = 1
        else:
            count_of_cards[i_card_num] += 1

        
        # get the number of matching numbers
        winners,mine = line.split("|")
        w = [x for x in winners.split(" ") if x]
        m = [x for x in mine.split(" ") if x]
        matches = sum(x in m for x in w)

        # increment card numbers for matching cards
        for cn in range(i_card_num+1,i_card_num+matches+1):
            if not cn in count_of_cards:
                count_of_cards[cn] = count_of_cards[i_card_num]
            else:
                count_of_cards[cn] += count_of_cards[i_card_num]

        # count the total number of cards and return
    return sum(count_of_cards.values())


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)

    print(f"part 1: {str(part1(data))}")
    print(f"part 2: {str(part2(data))}")


if __name__ == "__main__":
    solve(IN_FILE)
        