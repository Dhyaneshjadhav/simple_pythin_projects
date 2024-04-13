import random


class Card:

    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 10,
              'Queen': 10, 'King': 10, 'Ace': 11}
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.values[self.rank]

    def __str__(self):
        return self.suit + self.rank


class Deck:

    def __init__(self):

        self.cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)


class Players:

    def __init__(self,name):
        self.name = name
        self.hand = []
        self.hand_value = 0

    def ace_or_not(self):
        if self.hand_value > 21:
            for card in self.hand:
                if card.value == 11:
                    self.hand_value = self.hand_value - 10



class Dealer:

    def __init__(self, cards):
        self.cards = cards
        self.hand = []
        self.hand_value = 0

    def deal(self):
        return self.cards.pop(0)

    def ace_or_not(self):
        if self.hand_value > 21:
            for card in self.hand:
                if card.value == 11:
                    self.hand_value = self.hand_value - 10


class Game:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Players('Jack')
        self.dealer = Dealer(self.deck.cards)

        for card in range(3):
            self.player.hand.append(self.dealer.deal())
            self.dealer.hand.append(self.dealer.deal())

        for card in self.dealer.hand:
            self.dealer.hand_value = self.dealer.hand_value + card.value

        for card in self.player.hand:
            self.player.hand_value = self.player.hand_value + card.value


if __name__ == '__main__':
    game = Game()
    print(game.player.hand_value)
    print(game.dealer.hand_value)

    for card in game.player.hand:
        print(card)
    print('.'*10)
    for card in game.dealer.hand:
        print(card)
    print('.' * 10)
    game.player.ace_or_not()
    game.dealer.ace_or_not()
    print(game.player.hand_value)
    print(game.dealer.hand_value)