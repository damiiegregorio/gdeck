import unittest
from gdeck import Deck

test_list = ['Ace of Clubs', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Diamonds', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Hearts', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', 'Ace of Spades', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades']
test_length = "208"
test_item = "2 of Clubs"
actual_slice = ['Ace of Clubs', '2 of Clubs']


class TestGdeck(unittest.TestCase):
    def test_instance(self):
        deck = Deck()
        result = isinstance(deck, Deck)
        self.assertTrue(result)

    def test_deck(self):
        deck = Deck()
        result = Deck.show_deck(deck)
        self.assertNotEqual(result, test_list)

    def test_len(self):
        deck = Deck()
        result = deck.__len__()
        self.assertNotEqual(result, test_length)

    def test_slice(self):
        deck = Deck()
        test_slice = deck[0:2]
        assert test_slice == actual_slice, "Should be ['Ace of Clubs', '2 of Clubs']"

    def test_item(self):
        deck = Deck()
        result = deck.__getitem__(1)
        assert result == test_item, "Should 2 of Clubs"

    def test_choice(self):
        deck = Deck()
        result = Deck.choice(deck)
        self.assertTrue(result)

