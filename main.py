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
dealer = Player()
human = Player()

# Deal cards to human
human.hit(deck.getCard())
human.hit(deck.getCard())

# Check if human won
print(human.hand[0])
print(human.hand[1])


print(human.getTotal())
