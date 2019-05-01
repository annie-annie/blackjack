from Player import Player


class Human(Player):
    name = 'Human'

    def __init__(self, wallet):
        super(Human, self).__init__()
        self.wallet = wallet
