import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = []

    def generate(self):
        # 13 cards in each suit
        for i in range(1, 14):
            # 4 suits of cards
            for j in range(4):
                # add generated cards to self.cards list
                self.cards.append(Card(i, j))

    def draw(self, iteration):
        # create empty list in which we add player's hand
        cards = []
        for i in range(iteration):
            # pick a random card from deck
            card = random.choice(self.cards)
            # remove said card from deck
            self.cards.remove(card)
            # add said card to hand
            cards.append(card)
        return cards
