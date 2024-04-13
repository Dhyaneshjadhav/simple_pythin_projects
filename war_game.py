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
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        self.cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def split(self, player1, player2):
        for card in range(26):
            player1.cards.append(self.cards.pop(0))
            player2.cards.append(self.cards.pop(0))


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def remove_card(self):
        return self.cards.pop(0)

    def take_card(self, cards):
        self.cards.extend(cards)


class Game:
    def __init__(self):
        table_card = []
        game_round = 0
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player('Jack')
        self.player2 = Player('sparrow')
        self.deck.split(self.player2, self.player)
        while True:
            game_round += 1
            if len(self.player2.cards) == 0:
                print('Player 1 wins')
                print(len(table_card))
                break
            elif len(self.player.cards) == 0:
                print('Player 1 wins')
                print(len(table_card))
                break
            else:
                if self.player.cards[0].value > self.player2.cards[0].value:
                    self.player.cards.append(self.player.remove_card())
                    self.player.cards.append(self.player2.remove_card())
                    self.player.cards.extend(table_card)
                    print(game_round)
                    table_card = []
                elif self.player2.cards[0].value > self.player.cards[0].value:
                    self.player2.cards.append(self.player2.remove_card())
                    self.player2.cards.append(self.player.remove_card())
                    self.player2.cards.extend(table_card)
                    print(game_round)
                    table_card = []
                else:
                    if len(self.player.cards) < 5:
                        print('Player 2 wins')
                        print(len(table_card))
                        break
                    elif len(self.player2.cards) < 5:
                        print('Player 1 wins')
                        print(len(table_card))
                        break
                    else:
                        print(f'war in the game round {game_round}')
                        for card in range(5):
                            table_card.append(self.player2.remove_card())
                            table_card.append(self.player.remove_card())


if __name__ == '__main__':
    game = Game()