import random


def display_board(board):
    print('\n'*100)
    board3x3 = [board[1:4], board[4:7], board[7:]]
    for index, dim in enumerate(board3x3):
        print("   |   |   ")
        print(" {} | {} | {} ".format(dim[0], dim[1], dim[2]))
        if index != len(board3x3) - 1:
            print("___|___|___")
        else:
            print("   |   |   ")


def player_input():
    marker = input("Please pick a marker 'X' or 'O': ").upper()
    while 'X' not in marker and 'O' not in marker:
        marker = input("Please pick a marker 'X' or 'O': ").upper()
    return marker


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    matching_list = [board[1:4], board[4:7], board[7:],
                     board[1:8:3], board[3::3], board[3:8:2], board[1::4], board[2:9:3]]
    for comb in matching_list:
        if [mark, mark, mark] == comb:
            return True
    return False


def choose_first():
    if random.randint(0, 1):
        return "Player 1 to Start!"
    return "Player 2 to Start!"


def space_check(board, position):
    return ' ' == board[position]


def full_board_check(board):
    return ' ' not in board


def player_choice(board):
    while True:
        position = int(input('Please enter a number 1 - 9:  '))
        if space_check(board, position):
            return position
        else:
            print("Sorry! the position is already taken by {}".format(
                board[position]))


def replay():
    if (input("Do you want to play again (Any key for Yes or type 0)") != '0'):
        return True
    return False


while True:
    # Set the game up here
    game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    hint_board = ['#'] + list(range(1, 10))
    display_board(hint_board)
    print('Welcome to Tic Tac Toe!')
    print("Hint: Please input the number with the above mentioned position")
    print(choose_first())

    player1_choice = player_input()
    player2_choice = '$'
    if 'X' in player1_choice:
        player2_choice = '0'
    else:
        player2_choice = 'X'

    game_on = True

    while game_on:
        # Player 1 Turn
        if(full_board_check(game_board)):
            print("No more space! Game Over!")
            break
        print('Player1 Turn')
        p1_position = player_choice(game_board)
        place_marker(game_board, player1_choice, p1_position)
        display_board(game_board)
        if(win_check(game_board, player1_choice)):
            print('Congratulations! Player1 wins!')
            break

        # Player2's turn.
        print('Player2 Turn')
        if(full_board_check(game_board)):
            print("No more space! Game Over!")
            break
        p2_position = player_choice(game_board)
        place_marker(game_board, player2_choice, p2_position)
        display_board(game_board)
        if(win_check(game_board, player2_choice)):
            print('Congratulations! Player2 wins!')
            break

    if not replay():
        break
