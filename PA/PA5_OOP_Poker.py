import random
import sys
from collections import defaultdict
from abc import ABCMeta, abstractmethod

# Constants
suits = 'CDHS'
ranks = '23456789TJQKA'

class Card(metaclass=ABCMeta):
    """Abstact class for playing cards
    """
    def __init__(self, rank_suit):
        if rank_suit[0] not in ranks or rank_suit[1] not in suits:
            raise ValueError(f'{rank_suit}: illegal card')
        self.card = rank_suit

    def __repr__(self):
        return self.card

    @abstractmethod
    def value(self):
        """Subclasses should implement this method
        """
        raise NotImplementedError("value method not implemented")


    # card comparison operators
    def __gt__(self, other):
        return self.value() > other.value()

    def __ge__(self, other):
        return self.value() >= other.value()

    def __lt__(self, other):
        return self.value() < other.value()

    def __le__(self, other):
        return self.value() <= other.value()

    def __eq__(self, other):
        return self.value() == other.value()

    def __ne__(self, other):
        return self.value() != other.value()

#  0,   1,   2,   3,   4,   5,   6,   7,   8,    9,   10,  11,  12
# '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
#  2,   3,   4 ,  5,   6,   7,   8,   9,   10,   11,  12,  13,  14
class PKCard(Card):
    """Card for Poker game
    """
    def value(self):
        return ranks.index(self.card[0]) + 2

    def suit_value(self):
        return self.card[1]
    pass


class Deck:
    def __init__(self, cls):
        """Create a deck of 'cls' card class
        """
        self.deck = [cls(r + s) for s in suits for r in ranks]

    def __str__(self):
        return f'{self.deck}'

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, index):
        return self.deck[index]

    def shuffle(self):
        return random.shuffle(self.deck)

    def pop(self):
        return self.deck.pop()

    pass


class Hands:
    def __init__(self, cards):
        if len(cards) != 5:
            raise ValueError('not 5 cards')
        self.cards = sorted(cards, reverse=True)


    def is_flush(self, cards):  # suits가 같고 rank만 다른것
        # """"return: bool
        # """
        check_suit = []
        for i in range(len(cards)):
            check_suit.append(PKCard.suit_value(cards[i]))
        # print(check_suit)
        if len(set(check_suit)) == 1:
            return "Flush", sorted([PKCard.value(i) for i in cards], reverse= True)
        else:
            return None
        pass

    def is_straight(self, cards):  # suits는 달라도 rank가 순차적
        """:return: the cards making flush in decreasing order if found,
                None, otherwise
        """
        rank_values = sorted([PKCard.value(i) for i in cards], reverse= True)
        # print("rank_values", rank_values)
        for i in range(len(rank_values) - 1):
            if rank_values[i] - rank_values[i + 1] == 1:
                continue
            else:
                return None


        # value = sorted(cards, reverse= True)
        return "Straight", rank_values[0]

    def classify_by_rank(self, cards):
        """Classify the cards by ranks.

        :return: dict of the form { rank: [card, ...], ...}
            None if same ranks not found
        """
        classify_list = defaultdict(list)
        for i in cards:
            classify_list[PKCard.value(i)].append(PKCard.suit_value(i))

        if len(classify_list) >= 0:
            return classify_list

        pass

    def find_a_kind(self, cards):
        """Find if one pair, two pair, or three, four of a kind, or full house

        :return: hand-ranking name including 'Full house'
        """
        cards_by_ranks = self.classify_by_rank(cards)
        # print(cards_by_ranks)
        dictkey = list(cards_by_ranks.keys())
        dictvalue = list(cards_by_ranks.values())
        # print(dictkey)
        # print(dictvalue)


        # one pair
        if len(cards_by_ranks) == 4:
            newlist = []
            for i in range(len(dictvalue)):
                if len(dictvalue[i]) == 2:
                    newlist.append(dictkey[i])
                    newlist += sorted((dictkey[0:i] + dictkey[i+1:]), reverse= True)

            return "One pair", newlist

        # Two pair || Three of a kind
        elif len(cards_by_ranks) == 3:
            for i in range(len(dictvalue)):
                # Two pair
                if len(dictvalue[i]) == 2:
                    newlist = []
                    for i in range(len(dictvalue)):
                        if len(dictvalue[i]) == 2:
                            newlist.insert(0, dictkey[i])
                        elif len(dictvalue[i]) == 1:
                            newlist.append(dictkey[i])

                    if newlist[0] < newlist[1]:
                        temp = newlist[1]
                        newlist[1] = newlist[0]
                        newlist[0] = temp

                    return "Two pair", newlist

                # Three of a kind
                elif len(dictvalue[i]) == 3:
                    newlist = []
                    for i in range(len(dictvalue)):
                        if len(dictvalue[i]) == 3:
                            newlist.insert(0, dictkey[i])
                            newlist += sorted((dictkey[0:i] + dictkey[i+1:]), reverse= True)

                    return "Three of a kind", newlist

        # Full house || Four of a kind
        elif len(cards_by_ranks) == 2:
            for i in range(len(dictvalue)):
                # Full house
                if len(dictvalue[i]) == 3:
                    newlist = []
                    for i in range(len(dictvalue)):
                        if len(dictvalue[i]) == 3:
                            newlist.insert(0, dictkey[i])
                        else:
                            newlist.append(dictkey[i])

                    return "Full house", newlist

                # Four of a kind
                elif len(dictvalue[i]) == 4:
                    newlist = []
                    for i in range(len(dictvalue)):
                        if len(dictvalue[i]) == 4:
                            newlist.insert(0, dictkey[i])
                        else:
                            newlist.append(dictkey[i])

                    return "Four of a kind", newlist
        # High card
        elif len(cards_by_ranks) == 5:
            return "High card", sorted(dictkey, reverse= True)

        pass

    def tell_hand_ranking(self, cards):
        straight_val = self.is_straight(cards)
        flush_val = self.is_flush(cards)
        find_val = self.find_a_kind(cards)

        if straight_val and (find_val[0] == "High card") and not flush_val:
            return straight_val
        elif straight_val and flush_val:
            return "Straight flush", self.is_straight(cards)[1]
        elif (find_val[0] == "High card") and flush_val:
            return flush_val
        elif find_val[0] == "High card":
            return find_val
        elif find_val and not straight_val:
            return find_val

        pass

    def tie_break(self, other):
        rank_list = {"High card" : 0, "One pair" : 1, "Two pair" : 2, "Three of a kind" : 3, "Straight" : 4,
                     "Flush" : 5, "Full house" : 6, "Four of a kind" : 7, "Straight flush" : 8}
        player1 = self.tell_hand_ranking(self.cards)
        player2 = other.tell_hand_ranking(other.cards)

        if rank_list[player1[0]] > rank_list[player2[0]]:
            return True
        elif rank_list[player1[0]] == rank_list[player2[0]]:

            # High card
            if rank_list[player1[0]] == 0:
                for i in range(len(player1[1])):
                    if player1[1][i] > player2[1][i]:
                        return True
                    elif player1[1][i] < player2[1][i]:
                        return False

            # One pair
            elif rank_list[player1[0]] == 1:
                if player1[1][0] > player2[1][0]:
                    return True
                elif player1[1][0] < player2[1][0]:
                    return False
                elif player1[1][0] == player2[1][0]:
                    for i in range(1, len(player1[1])):
                        if player1[1][i] > player2[1][i]:
                            return True
                        elif player1[1][i] < player2[1][i]:
                            return False

            # Two pair
            elif rank_list[player1[0]] == 2:
                if player1[1][0] > player2[1][0]:
                    return True
                elif player1[1][0] < player2[1][0]:
                    return False
                elif player1[1][0] == player2[1][0]:
                    if player1[1][1] > player2[1][1]:
                        return True
                    elif player1[1][1] < player2[1][1]:
                        return False
                    elif player1[1][1] == player2[1][1]:
                        if player1[1][2] > player2[1][2]:
                            return True
                        elif player1[1][2] < player2[1][2]:
                            return False

            # Three of a kind
            elif rank_list[player1[0]] == 3:
                if player1[1][0] > player2[1][0]:
                    return True
                elif player1[1][0] < player2[1][0]:
                    return False
                elif player1[1][0] == player2[1][0]:
                    for i in range(1, len(player1)):
                        if player1[1][i] > player2[1][i]:
                            return True
                        elif player1[1][i] < player2[1][i]:
                            return False

            # Straight
            elif rank_list[player1[0]] == 4:
                if player1[1] > player2[1]:
                    return True
                elif player1[1] < player2[1]:
                    return False

            # Flush
            elif rank_list[player1[0]] == 5:
                if player1[1][0] > player2[1][0]:
                    return True
                elif player1[1][0] < player2[1][0]:
                    return False
                elif player1[1][0] == player2[1][0]:
                    for i in range(1, len(player1)):
                        if player1[1][i] > player2[1][i]:
                            return True
                        if player1[1][i] < player2[1][i]:
                            return False

            # Full house
            elif rank_list[player1[0]] == 6:
                if player1[1][0] > player2[1][0]:
                    return True
                elif player1[1][0] < player2[1][0]:
                    return False
                elif player1[1][0] == player2[1][0]:
                    if player1[1][1] > player2[1][1]:
                        return True
                    elif player1[1][1] < player2[1][1]:
                        return False

            # Four of a kind
            elif rank_list[player1[0]] == 7:
                if player1[1][0] > player2[1][0]:
                    return True
                elif player1[1][0] < player2[1][0]:
                    return False
                elif player1[1][0] == player2[1][0]:
                    if player1[1][1] > player2[1][1]:
                        return True
                    elif player1[1][1] < player2[1][1]:
                        return False

            # straight flush
            elif rank_list[player1[0]] == 8:
                if player1[1] > player2[1]:
                    return True
                elif player1[1] < player2[1]:
                    return False
        else:
            return False

        pass

if __name__ == '__main__':
    #
    def test(did_pass):
        """  Print the result of a test.  """
        linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
        if did_pass:
            msg = "Test at line {0} ok.".format(linenum)
        else:
            msg = ("Test at line {0} FAILED.".format(linenum))
        print(msg)

    # your test cases here
    # 1. player1 : 4 One pair // player2 : 5 One pair
    player1 = [PKCard('4D'), PKCard('2C'), PKCard('4H'), PKCard('JD'), PKCard('KD')]
    player2 = [PKCard('5D'), PKCard('3C'), PKCard('8H'), PKCard('5D'), PKCard('KD')]
    hand1 = Hands(player1)
    hand2 = Hands(player2)
    test(hand1.tie_break(hand2) == False)

    #2. player1 : King High card // player2 : J High card
    player1 = [PKCard('KD'), PKCard('2C'), PKCard('4H'), PKCard('JD'), PKCard('KD')]
    player2 = [PKCard('AD'), PKCard('3C'), PKCard('JH'), PKCard('5D'), PKCard('6D')]
    hand1 = Hands(player1)
    hand2 = Hands(player2)
    test(hand1.tie_break(hand2) == True)

    # 3. player1 : 9 high straight // player2 :  6 high straight
    player1 = [PKCard('9D'), PKCard('5C'), PKCard('7H'), PKCard('8D'), PKCard('6D')]
    player2 = [PKCard('6D'), PKCard('3C'), PKCard('2H'), PKCard('5D'), PKCard('4D')]
    hand1 = Hands(player1)
    hand2 = Hands(player2)
    test(hand1.tie_break(hand2) == True)

    # 4. player1 : 4, 6 Two pair // player2 :  3, K Two pair
    player1 = [PKCard('4D'), PKCard('6C'), PKCard('7H'), PKCard('4H'), PKCard('6D')]
    player2 = [PKCard('KD'), PKCard('3C'), PKCard('2H'), PKCard('3D'), PKCard('KC')]
    hand1 = Hands(player1)
    hand2 = Hands(player2)
    test(hand1.tie_break(hand2) == False)

    # 5. player1 : 9 Three of a kind // player2 :  Q Three of a kind
    player1 = [PKCard('9D'), PKCard('9C'), PKCard('9H'), PKCard('3D'), PKCard('6D')]
    player2 = [PKCard('QD'), PKCard('3C'), PKCard('QH'), PKCard('5D'), PKCard('QD')]
    hand1 = Hands(player1)
    hand2 = Hands(player2)
    test(hand1.tie_break(hand2) == False)

    # 6. player1 : 10 high Full house // player2 :  6 high Full house
    player1 = [PKCard('9D'), PKCard('TC'), PKCard('TH'), PKCard('9D'), PKCard('TD')]
    player2 = [PKCard('6D'), PKCard('6C'), PKCard('6H'), PKCard('3D'), PKCard('3D')]
    hand1 = Hands(player1)
    hand2 = Hands(player2)
    test(hand1.tie_break(hand2) == True)

    # 7. player1 : 6 One pair // player2 :  K One pair
    player1 = [PKCard('6D'), PKCard('5C'), PKCard('6H'), PKCard('8D'), PKCard('KD')]
    player2 = [PKCard('8D'), PKCard('3C'), PKCard('KH'), PKCard('KD'), PKCard('3D')]
    hand1 = Hands(player1)
    hand2 = Hands(player2)
    test(hand1.tie_break(hand2) == False)

    # 8. player1 : K Four of a kind // player2 :  6 Four of a kind
    player1 = [PKCard('KD'), PKCard('KC'), PKCard('KH'), PKCard('KS'), PKCard('4D')]
    player2 = [PKCard('6S'), PKCard('6C'), PKCard('6H'), PKCard('5D'), PKCard('6D')]
    hand1 = Hands(player1)
    hand2 = Hands(player2)
    test(hand1.tie_break(hand2) == True)

    # 9. player1 : 9 high straight flush // player2 :  6 high straight flush
    player1 = [PKCard('9D'), PKCard('5D'), PKCard('7D'), PKCard('8D'), PKCard('6D')]
    player2 = [PKCard('6S'), PKCard('3S'), PKCard('2S'), PKCard('5S'), PKCard('4S')]
    hand1 = Hands(player1)
    hand2 = Hands(player2)
    test(hand1.tie_break(hand2) == True)

    # 10. player1 : 10 high flush // player2 :  6 high flush
    player1 = [PKCard('TD'), PKCard('KD'), PKCard('7D'), PKCard('AD'), PKCard('6D')]
    player2 = [PKCard('6C'), PKCard('3C'), PKCard('KC'), PKCard('JC'), PKCard('4D')]
    hand1 = Hands(player1)
    hand2 = Hands(player2)
    test(hand1.tie_break(hand2) == True)

    # 11. player1 : J, K Two pair // player2 :  A, 3 Two pair
    player1 = [PKCard('JD'), PKCard('KC'), PKCard('JH'), PKCard('8D'), PKCard('KD')]
    player2 = [PKCard('AH'), PKCard('3C'), PKCard('3H'), PKCard('6D'), PKCard('AD')]
    hand1 = Hands(player1)
    hand2 = Hands(player2)
    test(hand1.tie_break(hand2) == False)

    # 12. player1 : royal straight flush // player2 :  10 high straight flush
    player1 = [PKCard('KD'), PKCard('JD'), PKCard('TD'), PKCard('QD'), PKCard('AD')]
    player2 = [PKCard('9H'), PKCard('6H'), PKCard('7H'), PKCard('8H'), PKCard('TH')]
    hand1 = Hands(player1)
    hand2 = Hands(player2)
    test(hand1.tie_break(hand2) == True)

    # 13. player1 : Ace high card // player2 :  8 One pair
    player1 = [PKCard('3D'), PKCard('5D'), PKCard('7C'), PKCard('AD'), PKCard('4D')]
    player2 = [PKCard('8D'), PKCard('8S'), PKCard('4H'), PKCard('JD'), PKCard('6D')]
    hand1 = Hands(player1)
    hand2 = Hands(player2)
    test(hand1.tie_break(hand2) == False)

    #14. player1 : 10 high flush // player2 : royal straight flush
    player1 = [PKCard('TD'), PKCard('KD'), PKCard('7D'), PKCard('AD'), PKCard('6D')]
    player2 = [PKCard('KS'), PKCard('JS'), PKCard('TS'), PKCard('QS'), PKCard('AS')]
    hand1 = Hands(player1)
    hand2 = Hands(player2)
    test(hand1.tie_break(hand2) == False)

    #15. player1 : J, Q Two pair // player2 : 3 Three of a kind
    player1 = [PKCard('TD'), PKCard('KD'), PKCard('7D'), PKCard('AD'), PKCard('6D')]
    player2 = [PKCard('KS'), PKCard('JS'), PKCard('TS'), PKCard('QS'), PKCard('AS')]
    hand1 = Hands(player1)
    hand2 = Hands(player2)
    test(hand1.tie_break(hand2) == False)

    #16. player1 : J high straight // player2 : 3 Four of a kind
    player1 = [PKCard('JD'), PKCard('8S'), PKCard('7H'), PKCard('TD'), PKCard('9S')]
    player2 = [PKCard('3S'), PKCard('3H'), PKCard('TD'), PKCard('3C'), PKCard('3D')]
    hand1 = Hands(player1)
    hand2 = Hands(player2)
    test(hand1.tie_break(hand2) == False)

    #17. player1 : K high Full house // player2 : 3 Four of a kind
    player1 = [PKCard('KD'), PKCard('KS'), PKCard('KH'), PKCard('9D'), PKCard('9S')]
    player2 = [PKCard('3S'), PKCard('3H'), PKCard('TD'), PKCard('3C'), PKCard('3D')]
    hand1 = Hands(player1)
    hand2 = Hands(player2)
    test(hand1.tie_break(hand2) == False)

    #18. player1 : J, Q Two pair // player2 : 8 One pair
    player1 = [PKCard('TD'), PKCard('KD'), PKCard('7D'), PKCard('AD'), PKCard('6D')]
    player2 = [PKCard('8D'), PKCard('8S'), PKCard('4H'), PKCard('JD'), PKCard('6D')]
    hand1 = Hands(player1)
    hand2 = Hands(player2)
    test(hand1.tie_break(hand2) == True)

    #19. player1 : 10 high straight flush // player2 : 8 One pair
    player1 = [PKCard('9H'), PKCard('6H'), PKCard('7H'), PKCard('8H'), PKCard('TH')]
    player2 = [PKCard('8S'), PKCard('8H'), PKCard('TD'), PKCard('QD'), PKCard('AC')]
    hand1 = Hands(player1)
    hand2 = Hands(player2)
    test(hand1.tie_break(hand2) == True)

    #20. player1 : 10 high flush // player2 : 8 One pair
    player1 = [PKCard('TD'), PKCard('KD'), PKCard('7D'), PKCard('AD'), PKCard('6D')]
    player2 = [PKCard('8S'), PKCard('8H'), PKCard('TD'), PKCard('QD'), PKCard('AC')]
    hand1 = Hands(player1)
    hand2 = Hands(player2)
    test(hand1.tie_break(hand2) == True)

    pass