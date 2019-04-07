from random import randint


class Card():
    def __init__(self, suite, cardType):
        self.suite = suite
        self.cardType = cardType

    def __str__(self):
        return '{}{}'.format(self.suite, self.cardType)

    def getValue():
        pass


class Deck():
    def getFreshDeck():
        suites = ['❤️', '♣️', '♦️', '♠️']
        cardTypes = ['A', *list(range(2, 11)), 'J', 'Q', 'K']

        return [
            Card(suite, cardType)
            for suite in suites
            for cardType in cardTypes
        ]

    cards = getFreshDeck()

    def getCard(self):
        randomNumber = randint(0, len(self.cards) - 1)
        return self.cards.pop(randomNumber)
