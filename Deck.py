from random import randint
from Card import Card


class Deck():
    def getFreshDeck():
        suits = ['❤️', '♣️', '♦️', '♠️']
        cardTypes = ['A', *list(range(2, 11)), 'J', 'Q', 'K']

        return [
            Card(suit, cardType)
            for suit in suits
            for cardType in cardTypes
        ]

    cards = getFreshDeck()

    def getCard(self):
        randomNumber = randint(0, len(self.cards) - 1)
        return self.cards.pop(randomNumber)
