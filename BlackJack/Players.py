'''
This module explains the properties of a Player
It acts on both on both
 - Dealer
 - Human player
'''

# Bottom up approach

# 2 Players
#   1 - Dealer      -  1000
#   2 - Human Player - 500
#
# Deal the cards
#   - 1 open and 1 close for dealer
#   - 2 open for human player
#
# Human starts the game
from random import choice


class Player():

    def __init__(self, balance, card_list):
        self.balance = balance
        self.card_list = card_list
        self.win_counter = 0

    def withdraw(self, amount):
        self.balance -= amount


class Human(Player):

    def show_cards(self):
        return self.card_list

    def deposit(self, amount):
        self.win_counter += 1
        self.balance += amount


class Dealer(Player):

    def show_initial_cards(self):
        return self.card_list[0]

    def show_all_cards(self):
        return self.card_list


class Deal():
    def __init__(self, player1, dealer, bet_amount):
        self.current_bet = bet_amount * 2
        self.current_player = player1
        self.current_player.withdraw(bet_amount)
        self.dealer = dealer
        self.dealer.withdraw(bet_amount)

    def hit(self):
        return Deck.fetch_random_card()


class Deck():

    def reset(cls):
        suites = ['Clubs', 'Hearts', 'Diamond', 'Spade']
        card_numbers = ['A', '2', '3', '4', '5', '6',
                        '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        cls.card_deck = [(c, s) for c in card_numbers for s in suites]

    def fetch_random_card(cls):
        card = choice(cls.card_deck)
        cls.card_deck.pop(cls.card_deck.index(card))
        return card


def fetch_count(card_list):
    card_value = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                  '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
    total = 0
    a_count = 0
    for cards in card_list:
        if cards[0] == 'A':
            a_count += 1
        total += card_value[cards[0]]

    while a_count > 0 and total > 21:
        total -= 10
        a_count -= 1

    return total


if __name__ == "__main__":
    # Initialize the deck of cards
    Deck.reset()

    deal_obj = Deal(card_deck, bet)

    dealer_init_card_list = [deal_obj.hit(), deal_obj.hit()]
    player_init_card_list = [deal_obj.hit(), deal_obj.hit()]

    dealer = Dealer(1000, dealer_init_card_list)
    player = Human(500, player_init_card_list)

    print("Initial bank balance")
    print(f"Dealer - {dealer.balance}")
    print(f"Player - {player.balance}")
    print(dealer.show_initial_cards())
    print(player.show_cards())
    # print(len(deal_obj.deck))

    print("Player1's turn!")
    while True:

        user_option = int(input("Enter 1 for Hit 0 for stay!"))

        if user_option:
            player.card_list.append(deal_obj.hit())
            print(player.show_cards())
            if fetch_count(player.card_list) > 21:
                print("Player 1 loses! Its a Bust!")
                dealer.deposit(deal_obj.current_bet)
                break

        else:
            deal_obj.stay(player)
            print("Dealers turn")
            break

        print("Dealers Turn")

        print(dealer.show_all_cards())
        dealer_count = fetch_count(dealer.card_list)
        player_count = fetch_count(player.card_list)
        if dealer_count > player_count:
            print("Dealer wins!")
            dealer.deposit(deal_obj.current_bet)
            break
        else:
            print("Dealer hits.")
            dealer.card_list.append(deal_obj.hit())
            print(dealer.show_all_cards())
            dealer_count = fetch_count(dealer.card_list)
            if dealer_count > 21:
                print("Player1 wins!")
                player.deposit(deal_obj.current_bet)
                break

    print("Initial bank balance")
    print(f"Dealer - {dealer.balance}")
    print(f"Player - {player.balance}")
