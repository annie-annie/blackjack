class Card():
    def __init__(self, suit, cardType):
        self.suit = suit
        self.cardType = cardType

    def __str__(self):
        return '{}{}'.format(self.suit, self.cardType)

    def __int__(self):
        if(type(self.cardType) == int):
            return self.cardType

        if(self.cardType in ['J', 'Q', 'K']):
            return 10

        if(self.cardType == 'A'):
            return 11

        raise Exception(
            '`{}` is not a valid card in a 52 card deck'
            .format(self.cardType)
        )

    def __add__(self, other):
        return int(self) + int(other)
