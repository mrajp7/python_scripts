# Add on extra functionality with a decorator

'''
Syntax:

@some_decorator
def sone_func():
    # do some stuff

'''

# to understand the underlying concept of decarators let check an example


def hello():
    return "Hello!"


# prints the reference of the hello()
print(hello)

# assigning the reference of hello to another variable
greet = hello
print(greet)  # holds the same reference

print(greet())  # executes the functions at the assigned reference

del hello  # delete the reference pointer to the functions

print(greet())  # however greet still holds the value of the reference to the function and hence executes the function

# (2) Another example on accessing a function within a function


def hello1():
    print("I am return a function!")

    def greet():
        return "\t You will shine one day!"

    return greet


welcome = hello1()

print(welcome())

# (3) Passing a function as arguments


def other(some_func):
    print('I am other')
    print(some_func())


other(welcome)

# CREATING A DECORATOR


def new_decorator(some_func):

    print("Some code before the given function")

    some_func()

    print("Some code after the given function")


def another_decorator(some_func):

    def inside():
        print(" some code in inside() of another_decorator - before ")

        some_func()

        print("some code in inside() of another_decorator - after ")
    return inside


@new_decorator
def func_needs_decorator():
    print("I want to be decorated!")


@another_decorator
def func_needs_another_decorator():
    print("I want another decorator!")


func_needs_decorator
func_needs_another_decorator()
