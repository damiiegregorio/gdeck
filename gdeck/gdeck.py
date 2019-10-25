import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return "{} of {}".format(self.rank, self.suit)


class Deck:
    suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank = ['Ace', "2", "3", "4", "5", "6", "7", "8", "9", "10", 'Jack', 'Queen', 'King']
    card_list = []

    def __init__(self):
        self.build()

    def build(self):
        """Merging suit and rank"""
        return [self.card_list.append(repr(Card(s, v))) for s in self.suit for v in self.rank]

    def show_deck(self):
        """Show deck in list form"""
        return self.card_list

    def choice(self):
        """Built in choice function"""
        random_card = random.choice(self.card_list)
        return random_card

    def __len__(self):
        return len(self.card_list)

    def __getitem__(self, item):
        return self.card_list[item]


deck = Deck()

"""Print commands"""
# print(deck[0:2])
# print(deck.choice())
# print(deck.show_deck())
# print(deck.__len__())
# print(deck.__getitem__(1))
