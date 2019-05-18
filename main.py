from Card import Card
from Deck import Deck
from Dealer import Dealer
from Human import Human
from Wallet import Wallet
from GameResult import GameResult


def play(wallet):
    deck = Deck()
    dealer = Dealer()
    human = Human(wallet)

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
        return GameResult(True, '21 already, you\'ve won')

    # Ask Human hit/stick
    while(input('Hit or stick?') == 'hit'):
        human.hit(deck.getCard())
        human.showHand()

        # Game ends if human has won with 21
        if human.has21():
            return GameResult(True, '21 already, you\'ve won')

        # Game ends if human is bust
        elif human.isBust():
            return GameResult(False, 'Tough luck, you are bust')

    # Reveal dealer hand
    dealer.showHand()

    # Game ends if dealer has a higher total than the human
    if human.getTotal() < dealer.getTotal():
        return GameResult(False, 'Sorry dealer has a better hand')

    # If the dealer has less than 17 he gets more cars
    while(dealer.getTotal() < 17):
        dealer.hit(deck.getCard())
        dealer.showHand()

        # Game ends if human is bust
        if dealer.isBust():
            return GameResult(True, 'Dealer went bust, you win')

        # Game ends if dealer has a higher total than the human
        elif human.getTotal() < dealer.getTotal():
            return GameResult(False, 'Sorry dealer has a better hand')

    # Game ends and human wins when his total is more than the dealers
    return GameResult(True, f'Dealer sticks at {dealer.getTotal()}')


def game():
    print("\033[1;35;40m Welcome!!! \n")

    wallet = Wallet()

    while (input("\033[1;36;40m Play (y/n)?") == 'y'):
        bet = int(input(
            f"You have {wallet.currentValue}, how much would you like to bet?"
        ))

        while (bet > wallet.currentValue):
            bet = int(input(
                f"You have {wallet.currentValue}, but you bet {bet}, please do not enter more than you have!"
            ))

        result = play(wallet)

        if(result.humanHasWon):
            wallet.win(bet)
        else:
            wallet.loose(bet)

        print(result)


game()

# TODO:
# 3. Implement wallet/pot
