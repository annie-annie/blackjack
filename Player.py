from functools import reduce


class Player():
    hand = []

    def hit(self, card):
        self.hand.append(card)

    def isBust(self):
        return sum(self.hand) > 21

    def getTotal(self):
        # order for addition needs to be card, then integer or it errors
        # with `TypeError: unsupported operand type(s) for +: 'int' and 'Card'`
        return reduce(lambda x, y: y + x, self.hand)

    def hasNaturalWin(self):
        return self.hand[0] + self.hand[1] == 21
