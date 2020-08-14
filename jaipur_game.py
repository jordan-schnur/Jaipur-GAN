from enum import IntEnum
import random


class CardType(IntEnum):
    CAMEL = 0
    LEATHER = 1
    SPICE = 2
    CLOTH = 3
    SILVER = 4
    GOLD = 5
    DIAMOND = 6


class TokenType(IntEnum):
    LEATHER = 0
    SPICE = 1
    CLOTH = 2
    SILVER = 3
    GOLD = 4
    DIAMOND = 5
    THREE_BONUS = 6
    FOUR_BONUS = 7
    FIVE_BONUS = 8

class TokenPile:
    Tokens = {}
    i = 0
    def __init__(self):
        self.Tokens = {}
        TokenPile.i += 1
        self.i = TokenPile.i
        for name, member in TokenType.__members__.items():
            self.Tokens[member] = 0

    def add_token(self, i):
        self.Tokens[i] += 1

    def read_cards(self):
        print("Hand " + self.i.__str__() + ": " + self.Tokens.__str__())

    def setup_tokens(self):
        self.Tokens = {}
        for name, member in TokenType.__members__.items():
            self.Cards[member] = 0

    def score(self):
        i = 0
        for name, member in TokenType.__members__.items():
            i += self.Cards[member]
        return i

def getenumfromint_card(i):
    if i == 0:
        return CardType.CAMEL
    elif i == 1:
        return CardType.LEATHER
    elif i == 2:
        return CardType.SPICE
    elif i == 3:
        return CardType.CLOTH
    elif i == 4:
        return CardType.SILVER
    elif i == 5:
        return CardType.GOLD
    elif i == 6:
        return CardType.DIAMOND


class Pile:
    Cards = {}
    i = 0
    def __init__(self):
        self.Cards = {}
        Pile.i += 1
        self.i = Pile.i
        for name, member in CardType.__members__.items():
            self.Cards[member] = 0

    def add_card(self, i):
        self.Cards[i] += 1

    def read_cards(self):
        print("Hand " + self.i.__str__() + ": " + self.Cards.__str__())

    def setup_cards(self):
        self.Cards = {}
        for name, member in CardType.__members__.items():
            self.Cards[member] = 0

    def num_cards(self):
        i = 0
        for name, member in CardType.__members__.items():
            i += self.Cards[member]
        return i


class Card:
    Card_Type = -1

    def __init__(self, card_type):
        self.Card_Type = card_type


class Deck(Pile):

    def __init__(self):
        for name, member in CardType.__members__.items():
            self.Cards[member] = 0
        self.Cards[CardType.CAMEL] = 8
        self.Cards[CardType.LEATHER] = 10
        self.Cards[CardType.SPICE] = 8
        self.Cards[CardType.CLOTH] = 8
        self.Cards[CardType.SILVER] = 6
        self.Cards[CardType.GOLD] = 6
        self.Cards[CardType.DIAMOND] = 6
        random.seed()

    def deal_hand(self, hand):

        i = 0
        active_cards = []
        i = 0
        for name, member in CardType.__members__.items():
            if self.Cards[member] != 0:
                active_cards.append(member)
                i += 1
        for x in range(5):
            t = random.randint(0, i-1)
            toInt = getenumfromint_card(t)
            self.Cards[toInt] -= 1
            hand.add_card(toInt)


class Hand(Pile):
    pass


class MiddlePile(Pile):

    def __init__(self):
        Pile.__init__(self)
        self.Cards[CardType.CAMEL] = 3



