class Card():
    def __init__(self, suite, cardType):
        self.suite = suite
        self.cardType = cardType

    def __str__(self):
        return '{}{}'.format(self.suite, self.cardType)

    def getValue(self):
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
        # self?
        if not isinstance(other, Card):
            # get type of other / instance if object
            raise Exception(
                'object of type Card expected, you should only sum cards with other cards'
            )

        return self.getValue() + other.getValue()
