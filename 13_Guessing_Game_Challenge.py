'''

The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!

'''

from random import randint

number_to_find = randint(1, 100)
user_guesses = []


# iteration one
while True:
    user_guesses.append(int(input("Guess a number: ")))
    recent_guess = user_guesses[0]
    # check if the value is with the boundary 1 to 100
    if recent_guess < 1 or recent_guess > 100:
        print("OUT OF BOUND!")
    # if matches
    elif recent_guess == number_to_find:
        print(
            f"You've guessed correctly and took {len(user_guesses)} attempts")
        break
    # if the previous guess has a absolute difference between 10 then say WARM!
    elif abs(recent_guess-number_to_find) <= 10:
        print("WARM!")
        break
    else:
        print("COLD!")
        break


while True:
    user_guesses.append(int(input("Again guess a number: ")))

    recent_guess = user_guesses[-1]
    previous_guess = user_guesses[-2]

    # check if the value is with the boundary 1 to 100
    if recent_guess < 1 or recent_guess > 100:
        print("OUT OF BOUND!")
    # if guess matches
    elif recent_guess == number_to_find:
        print(
            f"You've guessed correctly and took {len(user_guesses)} attempts")
        break
    # if the recent guess is closer to the number_to_find than the previous guess
    # print WARMER. Ensure to print WARMER if user enters the same previous guess
    elif abs(previous_guess - number_to_find) >= abs(recent_guess - number_to_find):
        print("WARMER!")
    # if the recent guess is far to the number_to_find than the previous guess
    # print COLDER. if the previous guess is same as recent guess it will be handled in the previous elif
    elif abs(previous_guess - number_to_find) < abs(recent_guess - number_to_find):
        print("COLDER!")
