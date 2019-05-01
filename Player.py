from functools import reduce


class Player():
    def __init__(self):
        self.hand = []

    def hit(self, card):
        self.hand.append(card)

    def isBust(self):
        return sum(self.hand) > 21

    def getTotal(self):
        # order for addition needs to be card, then integer or it errors
        # with `TypeError: unsupported operand type(s) for +: 'int' and 'Card'`
        return reduce(lambda x, y: y + x, self.hand)

    def has21(self):
        return self.getTotal() == 21

    def isBust(self):
        return self.getTotal() > 21

    def showHand(self):
        cardString = ' '.join([str(card) for card in self.hand])
        return print(f'{cardString}\tTotal: {self.getTotal()}')
