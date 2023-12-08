def card_value(card):
    values = '23456789TJQKA'
    return values.index(card)

def rank_hand(hand):
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1

    # Sort the cards by count and value
    sorted_cards = sorted(hand, key=lambda x: (counts[x], card_value(x)), reverse=True)

    # Check for different hand types
    if len(set(counts.values())) == 1:  # All cards have the same count
        if counts[sorted_cards[0]] == 5:
            return 8, sorted_cards  # Five of a kind
        elif counts[sorted_cards[0]] == 4:
            return 7, sorted_cards  # Four of a kind
        elif counts[sorted_cards[0]] == 3 and counts[sorted_cards[3]] == 2:
            return 6, sorted_cards  # Full house
        elif counts[sorted_cards[0]] == 3:
            return 3, sorted_cards  # Three of a kind
    elif len(set(counts.values())) == 2:  # Two different counts
        if 3 in counts.values():
            return 4, sorted_cards  # Two pair
        elif 2 in counts.values():
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

# Sample hands
hands = ['32T3K', 'T55J5', 'KK677', 'KTJJT', 'QQQJA']

# Sort hands in descending order of strength
sorted_hands = sorted(hands, key=lambda x: rank_hand(x), reverse=True)

# Print the result
for i, hand in enumerate(sorted_hands):
    print(f'{i+1}. {hand}')
