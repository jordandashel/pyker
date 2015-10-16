from card import *
import random

class Deck(object):

    def __init__(self):
        self.cards = [Card(v, s) for v in Value for s in Suit]

    def draw(self):
        return self.cards.pop(0)

    def shuffle(self):
       random.shuffle(self.cards)
