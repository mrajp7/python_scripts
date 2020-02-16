'''
This is a module describing about Abstract classes in Python
'''
from abc import ABC, abstractmethod


class Liquor(ABC):
    '''
    When a class inherits ABC compiler will not allow to create an instance
    of this class and only allow to inherit.
    Thus allowing true abstraction principle
    '''

    def __init__(self, brand, origin):
        self.brand = brand
        self.origin = origin

    @abstractmethod
    def base(self):
        '''
        note the implementation of raise NotImplementedError is not required in this case
        even 'pass' is not required.

        the purpose is to define it in the derived class
        '''

    @abstractmethod
    def country_of_origin(self):
        '''
        note the implementation of raise NotImplementedError is not required in this case
        even 'pass' is not required.

        the purpose is to define it in the derived class
        '''


class Tequila(Liquor):
    '''
    Inherits the abstract class Liquor and describes Tequila
    '''

    def base(self):
        '''
        Gives the raw material used in Tequila
        '''
        return f"{self.brand} is a TEQUILA brand and it made from Agave!"

    def country_of_origin(self):
        '''
        Gives the origin of the brand
        '''
        return f" {self.brand} Tequila is first originated in {self.origin}"


class Rum(Liquor):
    '''
    Inherits the abstract class Liquor and describes Rum
    '''

    def base(self):
        '''
        Gives the raw material used in Rum
        '''
        return f"{self.brand} is a RUM brand and it made from Sugarcane!"

    def country_of_origin(self):
        '''
        Gives the origin of the brand
        '''
        return f" {self.brand} Rum is first originated in {self.origin}"


def booze_type(liquor):
    '''
    booze_type can take any type of object.
    however, it should have base() method implemented.
    '''
    print(liquor.base())


# unknown_booze = Liquor("unknown") -
# TypeError: Can't instantiate abstract class Liquor with abstract methods base
jose = Tequila("Jose", "Mexico")
bacardi = Rum("Bacardi", "Hawai")

booze_type(jose)
booze_type(bacardi)
