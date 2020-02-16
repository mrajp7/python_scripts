# Creating clean repeatable code
# Functions are block of codes
# starts with 'def'

# Basic Syntax


def name_of_function():
    '''
    doc string : information about the function
    input: parameter details
    output: return details
    '''
    pass  # statement ...

# (1) PIG LATIN example
# If a word start with vowel then add 'ay' at the last
# If a word doesn't start with vowel then place the first letter to last and followed by 'ay'


def pig_latin(word):
    if word[0].lower() in "aeiou":
        return word + "ay"
    else:
        return word[1:] + word[0] + "ay"


print(pig_latin("zemon"))  # Output - emonzay
print(pig_latin("Orange"))  # Output - Orangeay


# (2) usage of *args and **kwargs
# args - arguments
# kwargs - keyword arguments
# - to receive an arbitrary number of arguments and keyword arguments

def my_func(*args):
    return sum(args)


print(my_func(2, 3, 4, 5, 6, 7, 7, 8))


def price_of_juices(**kwargs):
    for item, price in kwargs.items():
        print(f"The price of {item} is {price}")


price_of_juices(Lemon=30, Watermelon=40, Lemon_Mint=40)


def get_even_list(*args):
    even_list = [num for num in args if num % 2 == 0]
    return even_list


print(get_even_list(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 12, 42, 13, 12, 2, 1, 5, 41))

# (3) skyline


def myfunc(word):
    new_word = ""
    for index, letter in enumerate(word):
        if index % 2 == 0:
            new_word += letter.upper()
        else:
            new_word += letter.lower()
    return new_word


print(myfunc("mohanraj"))


# (4) Prime number count on given input

def count_primes(num):
    prime_list = [2]
    for n in range(3, num+1):
        is_Prime = True
        for div in prime_list:
            if div > int(n ** (0.5)):
                break
            if n % div == 0:
                is_Prime = False
        if is_Prime:
            prime_list.append(n)

    return len(prime_list)


print(count_primes(100))

"""
Just for fun:
PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
print_big('a')

out:   *  
      * *
     *****
     *   *
     *   *
HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
For purposes of this exercise, it's ok if your dictionary stops at "E".
"""


def print_big(letter):
    letter_dictionary = {
        'a': [4, 10, 31, 17, 17],
        'b': [30, 17, 31, 17, 30],
        'c': [31, 16, 16, 16, 31],
        'd': [30, 17, 17, 17, 30],
        'e': [31, 16, 31, 16, 31],
    }
    for val in letter_dictionary[letter.lower()]:
        binary_val = '0' * (5 - len(bin(val)[2:])) + bin(val)[2:]
        print(binary_val.replace("0", " ").replace("1", "*"))


for c in 'abcDe':
    print_big(c)


# Prime Numbers

def again_prime_count(num):
    if num < 2:
        return 0

    prime_list = [2]
    # since we know even numbers are not primes skipping them
    for number in range(3, num + 1, 2):
        for primes in prime_list:
            if number % primes == 0:
                break
        else:
            prime_list.append(number)

    print(prime_list)
    print(len(prime_list))


again_prime_count(1)
again_prime_count(2)
again_prime_count(3)
again_prime_count(100)
