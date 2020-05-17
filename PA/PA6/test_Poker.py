import pytest
from poker import *

def test_Card_init_exception():
    for illegals in ["10Q", "3U", "JK"]:
        with pytest.raises(ValueError):
            PKCard(illegals)

def test_Card_repr():
    assert repr(PKCard("3H")) == "3H"


@pytest.fixture
def all_card_set():
    return [r+s for r in ranks for s in suits]

@pytest.fixture
def c3C():
    return PKCard("3C")

@pytest.fixture
def c3S():
    return PKCard("3S")

@pytest.fixture
def c4S():
    return PKCard("4S")

def test_Card_compare(c3C, c3S, c4S):
    assert c3C == c3C and c3C == c3S
    assert c3C < c4S and c3S < c4S
    assert c3C <= c3S <= c4S
    assert c4S > c3S and c4S > c3C
    assert c4S >= c3S >= c3C
    assert c3C != c4S and c3S != c4S

def test_Deck_sort(all_card_set):
    import random
    all_cards = [PKCard(i) for i in all_card_set]
    random.shuffle(all_cards)
    all_cards.sort()
    check_sort1 = set([a.value() for a in all_cards])
    check_sort2 = set([i+2 for s in suits for i in range(len(ranks))])
    assert check_sort1 == check_sort2

@pytest.fixture
def deck():
    return Deck(PKCard)

def test_shuffle(all_card_set):
    all_cards = [PKCard(i) for i in all_card_set]
    return random.shuffle(all_cards)

def test_Deck_len_pop(deck):
    assert len(deck.deck) == 52
    deck.pop()
    assert len(deck.deck) == deck.__len__() == len(deck) == 52 - 1

def test_deck():
    deck = Deck(PKCard)  # deck of poker cards
    deck.shuffle()
    c = deck[0]
    print('A deck of', c.__class__.__name__)
    print(deck)
  
    # testing __getitem__ method
    print(deck[-5:])

    while len(deck) >= 10:
        my_hand = []
        your_hand = []
        for i in range(5):
            for hand in (my_hand, your_hand):
                card = deck.pop()
                hand.append(card)
        my_hand.sort(reverse=True)
        your_hand.sort(reverse=True)
        print(my_hand, '>', your_hand, '?', my_hand > your_hand)
    


# Testing data
non_flush_suit = "SDHCH"
flush_suit = "DDDDD"
test_case = {
    # make with dictionary {"Ranking" : (tuple)}
    Ranking.Straight_flush : (
        tuple(zip("AKQJT", flush_suit)),
        tuple(zip("KQJT9", flush_suit)),
        tuple(zip("T9876", flush_suit)),
        tuple(zip("76543", flush_suit)),
        tuple(zip("65432", flush_suit)),
    ),
    
    Ranking.Four_of_a_kind: (
        tuple(zip("KKKKT", non_flush_suit)),
        tuple(zip("QQQQ8", non_flush_suit)),
        tuple(zip("QQQQ2", non_flush_suit)),
        tuple(zip("TTTT2", non_flush_suit)),
        tuple(zip("66663", non_flush_suit)),
        tuple(zip("33332", non_flush_suit)),
    ),

    Ranking.Full_house: (
        tuple(zip("KKK88", non_flush_suit)),
        tuple(zip("JJJ99", non_flush_suit)),
        tuple(zip("JJJ77", non_flush_suit)),
        tuple(zip("66644", non_flush_suit)),
        tuple(zip("55533", non_flush_suit)),
    ),

    Ranking.Flush: (
        tuple(zip("AT862", flush_suit)),
        tuple(zip("KJ953", flush_suit)),
        tuple(zip("KT642", flush_suit)),
        tuple(zip("J8643", flush_suit)),
        tuple(zip("96532", flush_suit)),
    ),

    Ranking.Straight: (
        tuple(zip("AKQJT", non_flush_suit)),
        tuple(zip("T9876", non_flush_suit)),
        tuple(zip("98765", non_flush_suit)),
        tuple(zip("76543", non_flush_suit)),
        tuple(zip("65432", non_flush_suit)),
    ),

    Ranking.Three_of_a_kind: (
        tuple(zip("KKK72", non_flush_suit)),
        tuple(zip("KKK53", non_flush_suit)),
        tuple(zip("TTT75", non_flush_suit)),
        tuple(zip("99942", non_flush_suit)),
        tuple(zip("88852", non_flush_suit)),
    ),

    Ranking.Two_pairs: (
        tuple(zip("KKTT8", non_flush_suit)),
        tuple(zip("KK994", non_flush_suit)),
        tuple(zip("TT554", non_flush_suit)),
        tuple(zip("88552", non_flush_suit)),
        tuple(zip("77443", non_flush_suit)),
        tuple(zip("77442", non_flush_suit)),
    ),

    Ranking.One_pair: (
        tuple(zip("KK973", non_flush_suit)),
        tuple(zip("JJ952", non_flush_suit)),
        tuple(zip("88543", non_flush_suit)),
        tuple(zip("77642", non_flush_suit)),
        tuple(zip("66532", non_flush_suit)),
        tuple(zip("66432", non_flush_suit)),
    ),

    Ranking.High_card: (
        tuple(zip("A8642", non_flush_suit)),
        tuple(zip("KT752", non_flush_suit)),
        tuple(zip("JT753", non_flush_suit)),
        tuple(zip("98742", non_flush_suit)),
        tuple(zip("87543", non_flush_suit)),
    ),
}

def cases(*rankings):
    if not rankings:
        rankings = test_case.keys()
    return \
        [([r+s for r, s in case], ranking) 
        for ranking in rankings for case in test_case[ranking]
        ]


@pytest.mark.parametrize("faces, expected", cases(Ranking.Straight))
def test_is_straight(faces, expected):
    hand_org = [PKCard(c) for c in faces]
    random.shuffle(faces)
    hand = Hands([PKCard(c) for c in faces])
    cards = [PKCard(c) for c in faces]
    result = hand.is_straight(cards)
    assert result[0] == "Straight"
    assert Ranking[result[0]] == expected 
    assert hand.cards == hand_org

@pytest.mark.parametrize("faces, expected", cases(Ranking.Flush))
def test_is_flush(faces, expected):
    hand_org = [PKCard(c) for c in faces]
    random.shuffle(faces)
    hand = Hands([PKCard(c) for c in faces])
    cards = [PKCard(c) for c in faces]
    result = hand.is_flush(cards)
    assert result[0] == "Flush"
    assert Ranking[result[0]] == expected
    assert hand.cards == hand_org

@pytest.mark.parametrize("faces, expected", \
    cases(Ranking.Four_of_a_kind, Ranking.Three_of_a_kind, Ranking.Two_pairs, Ranking.One_pair))
def test_find_a_kind(faces, expected):
    hand_org = [PKCard(c) for c in faces]
    random.shuffle(faces)
    hand = Hands([PKCard(c) for c in faces])
    cards = [PKCard(c) for c in faces]
    result = hand.find_a_kind(cards)
    assert result[0] == "Four_of_a_kind" or "Three_of_a_kind" or "Two_pairs" or "One_pair"
    assert Ranking[result[0]] == expected
    assert hand.cards == hand_org

@pytest.mark.parametrize("faces, expected", cases(Ranking.High_card))
def test_find_a_kind_none(faces, expected):
    hand_org = [PKCard(c) for c in faces]
    random.shuffle(faces)
    hand = Hands([PKCard(c) for c in faces])
    cards = [PKCard(c) for c in faces]
    result = hand.find_a_kind(cards)
    assert result[0] == "High_card"
    assert Ranking[result[0]] == expected
    assert hand.cards == hand_org

@pytest.mark.parametrize("faces, expected", cases())
def test_evaluate_rankings(faces, expected):
    random.shuffle(faces)
    hand = Hands([PKCard(c) for c in faces])
    cards = [PKCard(c) for c in faces]
    result = hand.tell_hand_ranking(cards)
    assert Ranking[result[0]] == expected

@pytest.mark.parametrize("faces, expected", cases())
def test_tie_break(faces, expected):
    hand_cases = [Hands([PKCard(i) for i in faces]) for faces, ranking in cases()]
    cards = [PKCard(c) for c in faces]
    count1 = 0
    for i in range(len(hand_cases) -1):
        if hand_cases[i].tie_break(hand_cases[i+1]) == True:
            count1 +=1
    count2 = 0
    for i in range(len(hand_cases) -1):
        if hand_cases[i+1].tie_break(hand_cases[i]) == False:
            count2 += 1
    assert count1 == count2 
    print("\nHigh to low order : ")
    for i, hand in enumerate(hand_cases):
        print(i, hand)

