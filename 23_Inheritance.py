# Benefits of Inheritance - to reuse code and reduce the complexity of a program


class Animal():

    def __init__(self):
        print("Animal Created!")

    def who_am_i(self):
        print("I am animal")

    def eat(self):
        print("I am eating")


animal = Animal()
animal.who_am_i()
animal.eat()


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created!")

    def who_am_i(self):
        print("I am a dog")


dog = Dog()
dog.who_am_i()
dog.eat()
