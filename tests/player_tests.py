import unittest
from card import *
from player import Player
from deck import Deck

class PlayerTest(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        self.hugh = Player(1000)
        self.hugh.hand = [deck.draw(), deck.draw()]

    def test_player_bank(self):
        self.assertEqual(self.hugh.bank, 1000)

    def test_deal_hand(self):
        self.assertEqual(self.hugh.hand[0].suit, Suit['Clubs'])
        self.assertEqual(self.hugh.hand[0].value, Value['Two'])

    def test_bet(self):
        self.hugh.bet(50)
        self.assertEqual(self.hugh.bank, 950)

    def test_bet_with_insufficient_funds(self):
        with self.assertRaises(Exception):
            self.hugh.bet(1001)

    def test_all_in(self):
        all_in = self.hugh.all_in()
        self.assertEqual(all_in, 1000)
        self.assertEqual(self.hugh.bank, 0)

    def test_attributes(self):
        self.hugh.hello = 10
