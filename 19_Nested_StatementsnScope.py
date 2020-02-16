'''
Python always geos with the following rule on Scope of a variable/member

LEGB rule:

L (Local):
    ALways python first searches for a given variable in the scope of enclosed area
    ex: def, lamda etc.,
E (Enclosing function locals):
    The second level of scope. When a variable not found in a immediate enclosed area
    it looks for its parent enclosed area.
    ex: 
    def: 
        variable 
        for
            <usage of variable> here
G (Global):
    When a variable when used in a statement python will look for in the above two orders
    and checks for globally declared value of it, if not found in the above areas
B (Build in):
    These are all the keywords of Python and cannot be used in any other scope of a program
    ex: open, range, list, bin, abs, min, max, sum etc.,


'''

# Example of Local
lambda num: print(num ** 2)  # num is local

# Example of Enclosed
name = 'I AM DECLARED IN GLOBAL'


def greet():

    # name is overridden in this scope [a new string is created and the global 'name' is immutable as we all know]
    # and the new value only persists on in this scope
    name = "Mohan"

    def hello():
        # the referenced variable name is from the previous enclosed function greet()
        # and not the global variable name.
        print("Hello %s!" % name)

    hello()


greet()

# Example of Global
print(name)

# Exaple of BuiltIn
# len is builtin keyword
print(len(name))


# global - keyword

x = 2


def set_x():
    # referring to global
    '''
    Disclaimer - not to use unless really necessary to avoid the control of variable flow.
    its hard to debug when the global value expected is not found.

    Rather accept a variable as argument, return a value in the function
    and re-assign in the main scope

    example: x = set_x(value) [In main scope]
    '''
    global x
    x = 50


set_x()
print(x)


# (1) Lets check the scope of a List on the below function

list1 = ["I am gonna change", "Oh no i am not"]
print(list1)  # Output - ["I am gonna change", "Oh no i am not"]


def change_list(receive_list):
    receive_list[1] = 'Oh i have changed'


change_list(list1)
print(list1)  # Output - ['I am gonna change', 'Oh i have changed']

# -- The above happens so, because in Python the objects are always passed by reference.
# -- this is true for any Objects List, dictionary, class object etc.,
# -- and these are all stored in heap memory (since the memory size can vary on any given point)
# -- Its not the same for the case of int, bool, float and string
# -- int, bool, float are stored on stock [since the size is fixed].
# -- strings are immutable and hence a new string will be created when a write operation is made

# (2) Lets check the scope of a string as the above example (1)

string1 = "I am not gonna change, coz i am immutable"


def change_string(s):
    # Here it seems like it worked as pass by value.
    # however, as any other case it is pass by reference.
    # we wonder why the value has not changed for string1
    # the reason is only read operations on a string could happen on the reference of the passed argument
    # the moment an assignment happens, python create a new string and assigns the value.
    # However the scope remains in the enclosed function
    # its the same for tuple (since tuple is also immutable)
    s = "I have changed but i retain my scope in this enclosed function"


change_string(string1)
print(string1)

# (3) Lets check the scope of a int as the above example (1)

int1 = 40
bool1 = False
float1 = 100.555


def change_int(i):
    i = 100


def change_bool(b):
    b = True


def change_float(fv):
    fv = 0.0


change_int(int1)
change_bool(bool1)
change_float(float1)
print(int1)
print(bool1)
print(float1)
