# Main program

# Deal cards to computer
# Deal cards to human

# Ask Human hit/stick

# Case stick go to computer

# Case hit >
# if over computer wins
# if under Ask Human to hit or stick

# Computer
# Check if computer has won
# if not hit & repeat
# if over player wins
# If win then win

from functools import reduce

from Card import Card
from Deck import Deck
from Player import Player


def getTotal(hand):
    # order for addition needs to be card, then integer or it errors
    # with `TypeError: unsupported operand type(s) for +: 'int' and 'Card'`
    return reduce(lambda x, y: y + x, hand)


deck = Deck()
dealer = Player()
human = Player()

# Deal cards to dealer
dealer.hit(deck.getCard())
dealer.hit(deck.getCard())

# Deal cards to human
human.hit(deck.getCard())
human.hit(deck.getCard())

# Check if human won
# sum(human.hand)

card1 = deck.getCard()
card2 = deck.getCard()

print(card1)
print(card2)

print(getTotal([card1, card2, card1, card2]))
