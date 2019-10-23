import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def show_card(self):
        print("{} of {}".format(str(self.rank), str(self.suit)))
        # return "{} of {}".format(str(self.rank), str(self.suit))

    def __repr__(self):
        return "{} of {}".format(str(self.rank), str(self.suit))


class Deck:
    card_list = []
    card_category = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    card_range = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

    def __init__(self):
        self.build()

    def build(self):
        for s in self.card_range:
            for v in self.card_category:
                self.card_list.append(Card(v, s))

    def show_deck(self):
        for c in self.card_list:
            c.show_card()

    def choice(self):
        print("-----YOUR CARD IS-----")
        random_card = random.choice(self.card_list)
        return random_card

    def __len__(self):
        return len(self.card_list)

    def __getitem__(self, item):
        return self.card_list[item]


# deck = Deck()
# print(deck[0:7])