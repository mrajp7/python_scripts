# Polymorphism in python is slightly different from other programming languages.

# Example:
from abc import ABC, abstractmethod


class Tequila():

    def __init__(self, brand):
        self.brand = brand

    def base(self):
        return f"{self.brand} is a tequila brand and it made from Agave!"


class Rum():

    def __init__(self, brand):
        self.brand = brand

    def base(self):
        return f"{self.brand} is a rum brand and it made from Sugarcane!"


jose = Tequila("Jose")
bacardi = Rum("Bacardi")

for booze in [jose, bacardi]:
    print(type(booze))
    print(booze.base())


def booze_type(liquor):
    print(liquor.base())


booze_type(jose)
booze_type(bacardi)

# The below is not allowed in python

'''

def shape(length, breath):
    print("I am a rectangle")


def shape(length):
    print("I am a circle or may be square")


shape(2, 3)
shape(2)


'''
# Lets create an Abstract class [Basically its just a base and override the methods in the child classes]


class Liquor():
    '''

    This can also be done using a 'abc' library

    for more details check - 25_Abstract.py

    '''

    def __init__(self, brand):
        self.brand = brand

    def base(self):
        raise NotImplementedError(
            "sub class must implement this abstract method")


class Tequila(Liquor):

    def base(self):
        return f"{self.brand} is a TEQUILA brand and it made from Agave!"


class Rum(Liquor):

    def base(self):
        return f"{self.brand} is a RUM brand and it made from Sugarcane!"


unknown_booze = Liquor("unknown")
jose = Tequila("Jose")
bacardi = Rum("Bacardi")

booze_type(jose)
booze_type(bacardi)
booze_type(unknown_booze)
