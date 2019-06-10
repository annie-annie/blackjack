from functools import reduce


class Player():
    def __init__(self):
        self.hand = []

    def hit(self, card):
        self.hand.append(card)

    def getTotal(self):
        # order for addition needs to be card, then integer or it errors
        # with `TypeError: unsupported operand type(s) for +: 'int' and 'Card'`
        # A card knows how to add an integer and a Card,
        # where as an integer can only add other integers
        total = reduce(
            lambda runningTotal, card: card + runningTotal, self.hand
        )

        # if gone over but has ace count ace as 1, not 11
        if total > 21 and self.hasAce():
            return total - 10

        return total

    def has21(self):
        return self.getTotal() == 21

    def isBust(self):
        return self.getTotal() > 21

    def showHand(self):
        cardString = ' '.join([str(card) for card in self.hand])

        return print(
            f'{self.name} hand: {cardString}\tTotal: {self.getTotal()}'
        )

    # TODO: Hand can have more than 1 ace
    def hasAce(self):
        for card in self.hand:
            if card.cardType == 'A':
                return True

        return False
