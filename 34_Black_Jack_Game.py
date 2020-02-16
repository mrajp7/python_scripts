'''
In this milestone project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:

You need to create a simple text-based BlackJack game
The game needs to have one player versus an automated dealer.
The player can stand or hit.
The player must be able to pick their betting amount.
You need to keep track of the player's total money.
You need to alert the player of wins, losses, or busts, etc...
And most importantly:

You must use OOP and classes in some portion of your game. You can not just use functions in your game. Use classes to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!
Feel free to expand this game. Try including multiple players. Try adding in Double-Down and card splits! Remember to you are free to use any resources you want and as always:
'''
import random

suits = ('Clubs', 'Hearts', 'Diamond', 'Spade')
ranks = ('A', '2', '3', '4', '5', '6',
         '7', '8', '9', '10', 'Jack', 'Queen', 'King')

card_value = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
              '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

playing = True


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + deck_comp
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand():
    def __init__(self, name):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
        self.name = name

    def add_card(self, card):
        # adding a card to the hand [refer: Deck().deal ---> pulls a card from deck]
        self.cards.append(card)

        # calculating the value of the hand
        self.value += card_value[card.rank]

        # trace 'A'
        if card.rank == 'A':
            self.aces += 1

    def adjust_for_ace(self):
        # check for value is greater than 21
        # and run through a loop for reducing the value by replacing the value of 'A' to 1 [i.e., -10]
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips():
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Only numbers are allowed")
        else:
            if chips.bet > chips.total:
                print(f"You only have {chips.total}")
            else:
                break


def hit(deck, hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input("Hit or Stand? Enter 'h' for hit 's' for stand. ")
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands Dealer's Turn")
            playing = False
        else:
            print("Sorry! wrong input")
            continue

        break

# each rules of the game to be handled


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player, dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("PLAYER WINS! DEALER BUSTS!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lose_bet()


def push(player, dealer, chips):
    print("Dealer and player Tie! PUSH")


# Set the players chips
player_chips = Chips(500)

while True:
    # Print an Opening statement
    print("WELCOME TO BLACKJACK!")

    # Create and shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand("Player")
    dealer_hand = Hand("Dealer")

    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Prompt the player for the bet
    take_bet(player_chips)

    # show cards but keep 1 hidden for dealer
    show_some(player_hand, dealer_hand)

    while playing:  # from global

        #  Prompt for player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # show cards but keep 1 hidden for dealer since the player is still playing
        show_some(player_hand, dealer_hand)

        # if player's hand exceeds 21, run player_busts() break out of the loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:

            hit(deck, dealer_hand)

        # show all hands
        show_all(player_hand, dealer_hand)

        # run all winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand, player_chips)

    # total chips od user
    print("Current player chips {}".format(player_chips.total))

    # play_again?
    new_game = input("Do you want to play again? (y/n) ")
    if new_game[0].lower() == 'y':
        playing = True
    else:
        break
