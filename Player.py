from functools import reduce


class Player():
    def __init__(self, name):
        self.hand = []
        self.name = name

    def hit(self, card):
        self.hand.append(card)

    def isBust(self):
        return sum(self.hand) > 21

    def getTotal(self):
        # order for addition needs to be card, then integer or it errors
        # with `TypeError: unsupported operand type(s) for +: 'int' and 'Card'`
        total = reduce(lambda x, y: y + x, self.hand)

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

    def hasAce(self):
        for card in self.hand:
            if card.cardType == 'A':
                return True

        return False
