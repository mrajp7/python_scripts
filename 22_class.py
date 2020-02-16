# class - keyword to create a class

# syntax


class NameOfClass():  # camel casing

    # constructor method
    # used to create an instance of the class
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    # methods
    def some_method(self):
        # perform some actions
        print(self.param1)
        print(self.param2)


# Example of declaring a user defined object i.e., class

class Dog():

    # CLASS OBJECT ATTRIBUTE.
    # SAME FOR ANY INSTANCE OF THIS CLASS
    species = 'mammal'

    def __init__(self, breed, name, have_spots):
        # Attributes
        # We take in the arguments and
        # Assign it the instance's self.attribute_name
        self.breed = breed
        self.name = name

        # Expect boolean
        self.spots = have_spots

    # Operations or Actions on the attributes ---> Methods
    def bark(self):
        print(f"{self.name} ({self.breed}) barks - Woof! Woof!")


# my_dog = Dog() - TypeError: __init__() missing 3 required positional argument: 'breed'

my_dog = Dog(breed="Lab", name="Chomin", have_spots=False)

# my_dog has three attributes

print(my_dog.breed)
print(my_dog.species)
print(type(my_dog))
my_dog.bark()


# another more appropriate example
class Circle():

    # CLASS LEVEL ATTRIBUTE
    pi = 3.14

    # init for class
    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi
        # Circle.pi can also represented as self.pi since pi is shared for all the instances
        # however the notation Circle.pi should be preferred for better readability and clarity

    def get_circumference(self):
        return self.radius * Circle.pi * 2


my_circle = Circle()

another_circle = Circle(5)

print(
    f'Circle 1 "area" - {my_circle.area} "circumference - {my_circle.get_circumference()}"')

print(
    f'Circle 2 "area" - {another_circle.area} "circumference - {another_circle.get_circumference()}"')
