# AOC 2023 day 7: 
#

import aoc_utils as aoc
import time
import os
from collections import defaultdict

# IN_FILE = os.path.join("AOC2023","inputs","202307.in")
IN_FILE = os.path.join("AOC2023","inputs","202307.sample.txt")

def parse(puzzle_input):
    """
    Parse
    """
    # aoc.get_input(2023,7,False)

    with open(IN_FILE) as fp:
        data = fp.read().splitlines()

    hands = []
    for line in data:
        hand, bid = line.split(" ")
        hands.append((hand,int(bid)))

    return hands


def card_value(card):
    values = '23456789TJQKA'
    return values.index(card)

def rank_hand(hand):
    # print(hand)
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1

    # Sort the cards by count and value
    sorted_cards = sorted(hand, key=lambda x: (counts[x], card_value(x)), reverse=True)

    # Check for different hand types
    if counts[sorted_cards[0]] == 5: 
        return 7, sorted_cards  # Five of a kind
    elif counts[sorted_cards[0]] == 4:
        return 6, sorted_cards  # Four of a kind
    elif counts[sorted_cards[0]] == 3 and counts[sorted_cards[3]] == 2:
        return 5, sorted_cards  # Full house
    elif counts[sorted_cards[0]] == 3:
        return 4, sorted_cards  # Three of a kind
    elif len(set(counts.values())) == 2:  # Two different counts
        if len(counts.values()) == 3:
            return 3, sorted_cards  # Two pair
        else:
            return 2, sorted_cards  # One pair
    else:
        return 1, sorted_cards  # High card

def compare_hands(hand1, hand2):
    type1, cards1 = rank_hand(hand1)
    type2, cards2 = rank_hand(hand2)

    if type1 != type2:
        return type1 - type2

    for card1, card2 in zip(cards1, cards2):
        if card_value(card1) != card_value(card2):
            return card_value(card1) - card_value(card2)

    return 0  # Hands are identical

def part1(hands):        # => 252052080
    """
    Solve part 1
    
    """
    # Sort hands in descending order of strength
    sorted_hands = sorted(hands, key=lambda x: rank_hand(x[0]), reverse=False)

    # Calculate the total winnings
    total_winnings = 0
    for m,hand in enumerate(sorted_hands,1):
        total_winnings += m * hand[1]
    
    return total_winnings

def part2(hands):            # => 
    """
    Solve part 2
    """
    return 


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)

    start_time = time.time()
    p1 = str(part1(data))
    exec_time = time.time() - start_time
    print(f"part 1: {p1} ({exec_time:.4f} sec)")

    start_time = time.time()
    p2 = str(part2(data))
    exec_time = time.time() - start_time
    print(f"part 2: {p2} ({exec_time:.4f} sec)")



if __name__ == "__main__":
    solve(IN_FILE)
        