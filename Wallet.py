class Wallet():
    initialWalletAmount = 100

    def __init__(self):
        self.currentValue = self.initialWalletAmount

    def win(self, amount):
        self.currentValue += amount

    def loose(self, amount):
        self.currentValue -= amount
