# if elif else

if True:
    print("I enter if loop")


if False:
    print("I will be skipped")
else:
    print("I entered else")


if False:
    print("First block")
elif False:
    print("Second block")
elif True:
    print("elif I am printed on third block")
else:
    print("i will be skipped")

# for loops
# iterable

for c in "Mohanraj":
    print(c)

# Print even numbers
for num in range(1, 10):
    # Bitwise and with 1 always gives 0 if even number. 2(10) & 1(01) = (00)
    if not num & 1:
        print(num)
name = "MOhanraj"

# for on List
my_list = ["List: Name", 1, "Mohan", 2, "raj"]
for obj in my_list:
    print(obj)

# for on tuple
my_tup = ("Tuple: Name", 1, "Mohan", 2, "raj")
for obj in my_tup:
    print(obj)

# tuple unpacking
age_list = [("Mohan", 30), ("Praveena", 29), ("Dhanu", 3)]
for (Name, Age) in age_list:
    print("Age of {0} is {1}".format(Name, Age))

# for on sets
my_set = set('Mohanraj')
print(type(my_set))
for val in my_set:
    print(val)

# for on Dictionary
dict_ = {"Mohan": 30, "Praveena": 29}
for k in dict_:
    print(dict_[k])

for k in dict_.keys():
    print(dict_[k])

for val in dict_.values():
    print(val)

for items in dict_.items():
    print(items)

for Name, Age in dict_.items():
    print("Age of {0} is {1}".format(Name, Age))


# while
a = 10
while a >= 0:
    print(a)
    a -= 1
else:
    print(f"the loop exited because 'a' has {a}")


# break, continue, pass

# doesn't do anythin | Place holder
for c in "aeiou":
    pass

# breaks the for loop when if blocks executes
# hence prints nothing
for c in "aeiou":
    if 'a' == c:
        break
    print(c)

# continue skips a step in the for loop when if block executes
# it prints e, i, o, u
for c in "aeiou":
    if 'a' == c:
        continue
    print(c)
