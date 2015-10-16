from enum import Enum

class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Suit(Enum):
    Clubs = 1
    Spades = 2
    Hearts = 3
    Diamonds = 4

class Value(Enum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14
