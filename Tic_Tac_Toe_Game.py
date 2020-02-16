from random import randint

# Step 1 - Breakdown the rules / sequence of the game
'''
    Welcome Message

    Hint to Play!

    Display hint help

    Choose marker for Players

    Player [1 or 2]'s Turn

        Enter a number 1 - 9 to fill the position on the board
            allow only 1 - 9
            if the number is already taken again get a another valid number.

        Fill the position with the Player's marker

        Check the Player wins
            (No) continue
            (Congratulate the winner) break

        Check for the game is tie [No more space to fill the position]
            (No) continue
            (Game is Tie) break
'''

# Step 2 - Write sudo code for 'Step 1'

'''

function: display_board(parameter: board)
    just use print statements to print the board in the following pattern

     1 | 2 | 3
    ---|---|---
     4 | 5 | 6
    ---|---|---
     7 | 8 | 9

    return: None

function: is_position_free(parameter: board, position)
    return: space == board[position - 1] (since the matching position is always mapped to index of the list)

function: get_position_from_user(parameter: board)
    while True: [continue prompting user to enter a valid input]
        position = <user input> "Please enter a position between - 1 .. 9"
        if not number
            "only number from 1 .. 9 is allowed!"
            continue
        if call: not is_position_free(arguments: board, position)
            "Sorry, the position is already taken!"
            continue
        else
            return: position

function: fill_position_on_board(parameter: board, position, marker)
    board[position - 1] = marker
    return: board

function: is_board_full(parameter: board)
    return board not contains ' ' (space)

function: verify_player_wins(parameter: board, marker):
    combination_lists = all possible combinations that call it a win

        1 | 2 | 3
        4 | 5 | 6
        7 | 8 | 9

        i.e.,
        combination_lists is equal to
        [1, 2, 3] [4, 5, 6] [7, 8, 9]  - Horizontal combinations
        [1, 4, 7] [2, 5, 8] [3, 6, 9]  - Vertical combinations
        [1, 5, 9] [3, 5, 7]            - Diagonal combinations

    foreach successful_combination in combination_lists:
        return: if [marker, marker, marker] == successful_combination
        (if any the combination is matched then return true)
    return: False (if not all combination is met, the if block will not get executed and hence returning False at the last)

main:

    initialize: [board & players marker choice]
        hint_board = [ 1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ,  8 ,  9 ]
        game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    call: display_board(argument: hint_board)

    "Welcome to Tic Tac Toe Game!"
    "Two player shall play this game [ 'Player 1' and 'Player 2' ]"


    initialize: [Ready to play?]
        game_on = <user input> True or False
        if random(0,1): [0 - False, 1 - True]
            "Player 1 starts the game."
            player_dictionary = {"Player 1" : 'X', "Player 2" : 'O'}
        else:
            "Player 2 starts the game."
            player_dictionary = {"Player 1" : 'O', "Player 2" : 'X'}

    "Player 1 choice - " + player_dictionary["Player 1"]
    "Player 2 choice - " + player_dictionary["Player 2"]

    while game_on: [run until any player Wins | Tie]
        foreach PLAYER in ["PLAYER 1", "PLAYER 2"]

            MARKER = player_dictionary[PLAYER]

            if: call: verify_board_is_full(argument: game_board)
                "The game is Tie!"
                game_on = False (stop the game | while loop ends)
                break

            PLAYER + "'s turn!"

            initialize: [get position to fill]
                position = call: get_position_from_user(arguments: game_board)

            call: fill_position_on_board(arguments: game_board, position, MARKER)

            call: display_board(argument: game_board)

            if: call: verify_player_wins(argument: board)
                "Congratulations! " + PLAYER + " wins the game!"
                game_on = False
                break

'''

# Step 3 - Implement the sudo code from step 2


def display_board(board):
    '''
    Print the given board in the following model
     1 | 2 | 3
    ---|---|---
     4 | 5 | 6
    ---|---|---
     7 | 8 | 9
    '''
    # To clear up the terminal's printing area with 100 new line
    # this gives an illusion of refreshing the screen with updated board
    # print('\n'*100)
    # print [erase scrollback] [reset cursor position] [erase screen].
    # print("\33[3J\33[H\33[2J")
    line_break = "---"
    print(f' {board[0]} | {board[1]} | {board[2]}')
    print(f'{line_break}|{line_break}|{line_break}')
    print(f' {board[3]} | {board[4]} | {board[5]}')
    print(f'{line_break}|{line_break}|{line_break}')
    print(f' {board[6]} | {board[7]} | {board[8]}')


def is_position_free(board, position):
    '''
    Verify a given position in the board list is free are not
    i.e., filled with ' '
    so user can fill with a given marker

    return: True if ' ' (free)
    '''
    return ' ' == board[position - 1]


def get_position_from_user(board):
    '''
    Run a loop until user selects a valid position between 1 to 9
    Conditions:
    1. user input should be 1 to 9
    2. and the given position is free

    return position (selected by user)
    '''
    while True:
        position = get_only_numbers(
            input("Please enter a position between - 1 to 9: "))
        if position not in range(1, 10):
            print("Only numbers from  1 to 9 is allowed!")
            continue
        if not is_position_free(board, position):
            print("Sorry, the position is already taken!")
            continue
        return position


def get_only_numbers(word=""):
    '''
    Check a given word can be converted to number.
    If not return 0
    '''
    if word.isdigit():
        return int(word)
    else:
        return 0


def fill_position_on_board(board, position, marker):
    '''
    Fill a position on the given board.
    board - game board represented in list
    position - position - 1 refers to the index in the list
    marker - any value/object to replace in the given position

    Note: By default list is passed by reference the original value also will be modified
          Hence we are not returning the modified list back to the caller.

    returns None
    '''
    board[position - 1] = marker


def is_board_full(board):
    '''
    If any ' ' (space) found in the board then return False (the board in not full)
    return True if no ' ' (space) found in the given board

    board - game board represented in list

    return - True | False
    '''
    return ' ' not in board


def verify_player_wins(board, marker):
    '''
    0 | 1 | 2
    3 | 4 | 5
    6 | 7 | 8

    successful combination_lists are
    [0, 1, 2] [3, 4, 5] [6, 7, 8]  - Horizontal combinations
    [0, 3, 6] [1, 4, 7] [2, 5, 8]  - Vertical combinations
    [0, 4, 8] [2, 4, 6]            - Diagonal combinations

    foreach successful_combination in combination_lists:
        return: if [marker, marker, marker] == successful_combination
        (if any of the combination is matched then the player wins)
    return: False (if not all combination is met)
    '''
    combination_lists = [board[0:3], board[3:6], board[6:],
                         board[0:7:3], board[1:8:3], board[2::3],
                         board[0::4], board[2:7:2]]
    for comb in combination_lists:
        if [marker, marker, marker] == comb:
            return True
    return False


def welcome_to_the_game():
    display_board(list(range(1, 10)))  # hint board
    print("Welcome to Tic Tac Toe Game!")
    print("Two player shall play this game [ 'Player 1' and 'Player 2' ]")


print("A random print")


def main():
    '''

    The Game starts here

    '''
    game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    welcome_to_the_game()

    game_on = get_only_numbers(
        input("Lets begin the game? options (0 - False, 1 - True) - "))

    if randint(0, 1):  # 0 - False, 1 - True
        print("Player 1 starts the game.")
        player_dictionary = {"Player 1": 'X', "Player 2": 'O'}
        player_list = ["Player 1", "Player 2"]
    else:
        print("Player 2 starts the game.")
        player_dictionary = {"Player 1": 'O', "Player 2": 'X'}
        player_list = ["Player 2", "Player 1"]

    print("Player 1 choice - " + player_dictionary["Player 1"])
    print("Player 2 choice - " + player_dictionary["Player 2"])

    while game_on:
        for PLAYER in player_list:

            MARKER = player_dictionary[PLAYER]

            if is_board_full(game_board):
                print("The game is Tie!")
                game_on = False
                break

            print(f"{PLAYER}'s turn!")

            position = get_position_from_user(game_board)

            fill_position_on_board(game_board, position, MARKER)

            display_board(game_board)

            if verify_player_wins(game_board, MARKER):
                print(f"Congratulations! {PLAYER} wins the game!")
                game_on = False
                break

    print(" -- The End --")


if __name__ == "__main__":
    main()
else:
    print("The game is being imported!")
