# Main program

# Deal cards to computer
# Deal cards to human

# Check if human has won naturally

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


def play():
    deck = Deck()
    dealer = Player()
    human = Player()

    # Deal cards to dealer
    dealer.hit(deck.getCard())
    dealer.hit(deck.getCard())

    # Deal cards to human
    human.hit(deck.getCard())
    human.hit(deck.getCard())

    # Show cards
    print('Dealer Hand: ', '[]', dealer.hand[1])
    print('Your Hand: ', human.hand[0], human.hand[1])

    # Check if human has won naturally
    if human.hasNaturalWin():
        return '21 already, you\'ve won'


print(play())
