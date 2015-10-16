import unittest
from deck import Deck
from card import *

class DeckTest(unittest.TestCase):
    def setUp(self):
        self.new_deck = Deck()

    def tearDown(self):
        self.new_deck = None

    def test_deck_has_52_cards(self):
        deck_length = len(self.new_deck.cards)
        self.assertEqual(deck_length, 52)

    def test_draw_card_retrieves_first_card_from_deck(self):
        first_card = self.new_deck.draw()
        self.assertEqual(first_card.suit, Suit['Clubs'])
        self.assertEqual(first_card.value, Value['Two'])

    def test_draw_removes_card_from_deck(self):
        first_card = self.new_deck.draw()
        second_card = self.new_deck.draw()

        self.assertEqual(first_card.suit, Suit['Clubs'])
        self.assertEqual(first_card.value, Value['Two'])

        different_suit = first_card.suit != second_card.suit
        different_card = first_card.value != second_card.value

        different_card = different_suit or different_suit

        self.assertTrue(different_card)

    def test_shuffle_deck(self):
        self.new_deck.shuffle()
        first_card = self.new_deck.cards[0]
        suit = first_card.suit
        self.assertFalse(first_card.suit == Suit['Clubs']
                and first_card.value == Value['Two'])
