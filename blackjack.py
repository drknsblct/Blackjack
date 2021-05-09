from deck import Deck
from player import Player

games = []


class Blackjack:
    def __init__(self):
        # create deck instance variable
        self.deck = Deck()
        # call deck's generate function
        self.deck.generate()
        # create player
        self.player = Player(False, self.deck)
        # create dealer
        self.dealer = Player(True, self.deck)

    def play(self, num):
        global games
        player_status = self.player.deal()
        dealer_status = self.dealer.deal()

        if player_status == 1:
            # if player draws 21 first try
            games.append('Wins')

            if dealer_status == 1:
                # if dealer draws 21 first try
                games.append('Losses')
            return 1

        while self.player.score <= num:
            # if player's score is below num then we add
            bust = 0

            if self.player.score <= num:
                bust = self.player.hit()
            if bust == 1:
                # if player has cards with values > 21
                games.append('Losses')
                return 1

        if dealer_status == 1:
            # if dealer's cards have value == 21
            games.append('Losses')
            return 1

        while self.dealer.check_score() <= 17:
            # dealer must have at least 17 card value according to the rules
            if self.dealer.hit() == 1:
                # if dealer's cards have value > 21 then we win
                games.append('Wins')
                return 1

        if self.dealer.check_score() == self.player.check_score():
            games.append('Losses')
        elif self.dealer.check_score() > self.player.check_score():
            games.append('Losses')
        elif self.dealer.check_score() < self.player.check_score():
            games.append('Wins')
