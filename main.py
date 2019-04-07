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

from Card import Card
from Deck import Deck
deck = Deck()

card = deck.getCard()
print(card, card.getValue())
card = deck.getCard()
print(card, card.getValue())
card = deck.getCard()
print(card, card.getValue())
card = deck.getCard()
print(card, card.getValue())
card = deck.getCard()
print(card, card.getValue())
card = deck.getCard()
print(card, card.getValue())
card = deck.getCard()
print(card, card.getValue())
card = deck.getCard()
print(card, card.getValue())
card = deck.getCard()
print(card, card.getValue())


broken = Card('$', 't')
broken.getValue()
