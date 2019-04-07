class Player():
    hand = []

    def hit(self, card):
        self.hand.append(card)

    def isBust(self):
        return sum(self.hand) > 21
