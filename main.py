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
from Player import Player

deck = Deck()
computer = Player()
human = Player()

# Deal cards to computer
computer.hit(deck.getCard())
computer.hit(deck.getCard())

# Deal cards to human
human.hit(deck.getCard())
human.hit(deck.getCard())
