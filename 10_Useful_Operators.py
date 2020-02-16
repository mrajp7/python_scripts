# import is for example at Line:105
from random import shuffle
from random import randint

#############################################
############### range operators #############
#############################################

# range(start,end,step/jump)

# range through 1 to 11

my_list = []
for num in range(1, 11):
    if not num & 1:
        my_list.append(num)
# my_list to hold even numbers
print(my_list)  # Output: [2, 4, 6, 8, 10]


# range through 2 to 11 and jump between 2 places
my_list = []
for num in range(2, 11, 2):
    my_list.append(num)
# my_list to hold even numbers
print(my_list)


# optimized above for loop example
# range through 2 to 11 and jump between 2 places
my_list = list(range(2, 11, 2))
# my_list to hold even numbers
print(my_list)

###################################################

# enumerate

# helps to get the index of a list in the form of tuples
for val in enumerate("content"):
    print(val)

# unpack the tuples
for index, value in enumerate("content"):
    print(f"the char {value} is at {index}")


###################################################

# zip

# to zip and range on two lists in the form of tuples
# when zipping two lists, it forms a tuple as
# list1 = [0,1,2]
# list2 = [0,1,2]
# zip(list1, list2) = [(0,0),(1,1),(2,2)]
list1 = [1, 2, 3, 4, 5]  # omit the elements if extra while zipping lists
list2 = ['a', 'b', 'c']
list3 = [6, 7, 8]
for obj in zip(list1, list2, list3):
    print(obj)

# unpack the tuples
for val1, val2, val3 in zip(list1, list2, list3):
    print(val1, val2, val3)

# to assign to a new list of tuples
zipped_list = list(zip(list1, list2, list3))
print(zipped_list)
# zip is only to create a tuple of lists provided, not meant for merging
merged_list = list1 + list2 + list3
print(merged_list)

##################################################

# in - keyword

# we already saw this in loops
# it is also used to check a element is present in a given list
print('x' in [1, 2, 3, 4])

# to check a string (list of chars) in a string
print('han' in 'mohanraj')

# to check a key is present in a dictionary
age_of_family_members = {"Mohan": 30, "Praveena": 29, "Dhanu": 3}
print("Dhanu" in age_of_family_members)
# on values / items
print(("Mohan", 30) in age_of_family_members.items())
print(3 in age_of_family_members.values())

###################################################

# min, max

list1 = list(range(10, 210, 10))
print(list1)

# min
print(min(list1))
# max
print(max(list1))

####################################################

# shuffle | module [from random import shuffle]

# shuffles a list on the list reference. Doesn't return anything
list1 = list(range(1, 10))
print(list1)
print(shuffle(list1))  # Output: None
print(list1)
shuffle(list1)
print(list1)

####################################################

# randint | module [from random import randint]
# it provides a random integer

print(randint(-10, 10))

####################################################

# input

# to get a value from the user

user_val = input('enter a number: ')
print(type(user_val))
print(user_val)

# type converting
user_val = int(input('enter a number: '))
print(type(user_val))
print(user_val)
