class Player:
    # init method for player/dealer
    def __init__(self, isDealer, deck):
        self.cards = []
        self.isDealer = isDealer
        self.deck = deck
        self.score = 0

    def hit(self):
        self.cards.extend(self.deck.draw(1))
        self.check_score()
        # ternary operator
        return 1 if self.score > 21 else 0

    def deal(self):
        self.cards.extend(self.deck.draw(2))
        self.check_score()
        # ternary operator
        return 1 if self.score == 21 else 0

    def check_score(self):
        counter = 0
        self.score = 0
        for card in self.cards:
            if card.price() == 11:
                counter += 1
            self.score += card.price()

        while counter != 0 and self.score > 21:
            counter -= 1
            self.score -= 10
        return self.score
