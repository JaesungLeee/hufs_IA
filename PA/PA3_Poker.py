# import random
from collections import defaultdict

suits = 'CDHS'
ranks = '23456789TJQKA'
values = dict(zip(ranks, range(2, 2 + len(ranks))))
print(values)
deck = [(r, s) for s in suits for r in ranks]

def is_flush(hands):    #suits가 같고 rank만 다른것
    # """"return: bool
    # """
    check_suit = []
    for i in range(len(hands)):
        check_suit.append(hands[i][1])
    # print(check_suit)
    if len(set(check_suit)) == 1:
        return True
    else:
        return False
    pass

def is_straight(hands):     # suits는 달라도 rank가 순차적
    """:return: the cards making flush in decreasing order if found,
            None, otherwise
    """
    check_values = [i[0] for i in hands]
    # print(check_values)
    rank_values = sorted([values[i] for i in check_values], reverse= True)
    # print(rank_values)
    for i in range(len(rank_values) - 1):
        if rank_values[i] - rank_values[i + 1] == 1:
            continue
        else:
            return None

    return hands

    pass

def classify_by_rank(hands):
    """Classify the cards by ranks.

    :return: dict of the form { rank: [card, ...], ...}
        None if same ranks not found
    """
    classify_list = defaultdict(list)
    for r, s in hands:
        classify_list[r].append(s)

    if len(classify_list) >= 0:
        return classify_list

    pass

def find_a_kind(hands):
    """Find if one pair, two pair, or three, four of a kind, or full house

    :return: hand-ranking name including 'Full house'
    """
    cards_by_ranks = classify_by_rank(hands)

    if len(cards_by_ranks) == 4:
        return 'One Pair'
    elif len(cards_by_ranks) == 3:
        return 'Two Pair'
    elif len(cards_by_ranks) == 2:
        return 'Three of a kind'
    elif len(cards_by_ranks) == 1:
        return 'Four of a kind'
    elif len(cards_by_ranks) == 0:
        value_counts = defaultdict(lambda: 0)
        print(value_counts)
        for i in values:
            value_counts[i] += 1
        if sorted(value_counts.values()) == [2, 3]:
            return 'Full House'
    pass

def tell_hand_ranking(hands):
    """Tell the hand ranking name for the cards in hand

    :return: hand-ranking name
    """
    if is_flush(hands):
        return "Flush"
    elif is_straight(hands):
        return "Straight"
    elif find_a_kind(hands):
        return find_a_kind(hands)

if __name__ == "__main__":    # Only if this script runs as a main,
    hands = [
        [('3', 'D'), ('5', 'D'), ('7', 'C'), ('A', 'D'), ('4', 'D')],
        [('K', 'D'), ('J', 'D'), ('Q', 'C'), ('A', 'D'), ('T', 'D')],
        [('4', 'D'), ('4', 'C'), ('4', 'C'), ('A', 'S'), ('A', 'D')],
        [('2', 'D'), ('3', 'D'), ('4', 'C'), ('5', 'D'), ('6', 'D')],
        [('2', 'D'), ('8', 'D'), ('4', 'D'), ('5', 'D'), ('6', 'D')],
        [('2', 'D'), ('2', 'S'), ('4', 'H'), ('J', 'D'), ('6', 'D')],
        [('4', 'D'), ('A', 'H'), ('A', 'C'), ('A', 'S'), ('A', 'D')],
        [('J', 'H'), ('2', 'S'), ('J', 'S'), ('8', 'H'), ('2', 'H')],
        [('6', 'H'), ('5', 'S'), ('4', 'S'), ('3', 'H'), ('2', 'H')],
        [('A', 'H'), ('5', 'S'), ('4', 'S'), ('3', 'H'), ('2', 'H')],
        [('4', 'D'), ('6', 'H'), ('6', 'C'), ('6', 'S'), ('6', 'D')],
        [('8', 'H'), ('T', 'D'), ('J', 'H'), ('9', 'H'), ('Q', 'H')],
        [('T', 'H'), ('J', 'H'), ('K', 'H'), ('A', 'H'), ('Q', 'H')],
        [('5', 'S'), ('2', 'S'), ('A', 'S'), ('4', 'S'), ('3', 'S')],
    ]

    for i in range(len(hands)):
        print(tell_hand_ranking(hands[i]))

    # print("Player's cards are", hands)
    #
    # print("Is Flush? : ", is_flush(hands))
    #
    # print("Is Straigt? : ", is_straight(hands))
    #
    # print("Check kind? : ", find_a_kind(hands))
    #
    # print("Result is :", tell_hand_ranking(hands))
    #
    # pass  # test code here will run.
    #
