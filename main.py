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
    dealer = Player('Dealer')
    human = Player('Human')

    # Deal cards to dealer
    dealer.hit(deck.getCard())
    dealer.hit(deck.getCard())

    # Deal cards to human
    human.hit(deck.getCard())
    human.hit(deck.getCard())

    # Show cards
    print('Dealer Hand: ', '[]', dealer.hand[1])
    human.showHand()

    # Check if human has won naturally
    if human.has21():
        return '21 already, you\'ve won'

    # Ask Human hit/stick
    while(input('Hit or stick?') == 'hit'):
        # TODO: validation
        human.hit(deck.getCard())
        human.showHand()

        # Game ends if human has won with 21
        if human.has21():
            return '21 already, you\'ve won'
        # Game ends if human is bust
        elif human.isBust():
            return 'Tough luck, you are bust'

    # Reveal dealer hand
    dealer.showHand()

    # Game ends if dealer has a higher total than the player
    if human.getTotal() < dealer.getTotal():
        return 'Sorry dealer has a better hand, you loose'

    # If the dealer has less than 17 he gets more cars
    while(dealer.getTotal() < 17):
        dealer.hit(deck.getCard())
        dealer.showHand()

        # Game ends if human is bust
        if dealer.isBust():
            return 'Dealer went bust, you win'
        # Game ends if dealer has a higher total than the human
        elif human.getTotal() < dealer.getTotal():
            return 'Sorry dealer has a better hand, you loose'

    # Game ends and player wins when his total is more than the dealers
    return f'Dealer sticks at {dealer.getTotal()}, you win'


print(play())


# TODO:
# 1. rename human to player
# 2. Implement ace logic
# 3. Implement wallet/pot
