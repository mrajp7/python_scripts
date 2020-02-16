'''
Module contains functions that helps in capitalize any part 
of a given string
'''


def start_letter(word):
    return word.title()


def middle_letter(word):
    if len(word) % 2 == 0:
        mid_index = len(word)//2 - 1
    else:
        mid_index = len(word)//2
    return word[:mid_index] + word[mid_index:].capitalize()


print(middle_letter("python"))
