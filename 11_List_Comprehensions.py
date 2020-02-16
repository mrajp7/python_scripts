#  -- LIST COMPREHENSION in PYTHON --
# when you find yourself using a loop and <list>.append() together
# list comprehension are a good alternative

# disclaimer - usage of 'list comprehension' reduces the code redability
#            - it is not a 'clean code' practice. Use it in a relevant scenario

# example to create a list of character from a string
mylist = []
for c in 'hello':
    mylist.append(c)
print(mylist)

# (1) - usage of List comprehension
mylist = [c for c in 'hello']
print(mylist)

'''
(1) Output

['h', 'e', 'l', 'l', 'o']

'''

# (2) - another example for operation on elements
square_list = [num**2 for num in range(1, 11)]
print(square_list)

'''
(2) Output

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

'''

# (3) -using if condition
# to add a list of even numbers from a range
even_list = [num for num in range(1, 11) if not num & 1]
print(even_list)

'''
(3) Output

[2, 4, 6, 8, 10]

'''

# (4) - another complex examples
# to convert oz to ml
# 1 oz = 29.5735 ml
oz_list = [1, 0.25, 0.75, 20, 3]
ml_list = [(oz * 29.5735) for oz in oz_list]
for oz, ml in zip(oz_list, ml_list):
    print(f'{oz} ounce is {ml:0.0f} ml approx')

''' 
(4) Output

1 ounce is 30 ml approx
0.25 ounce is 7 ml approx
0.75 ounce is 22 ml approx
20 ounce is 591 ml approx
3 ounce is 89 ml approx

'''

# (5) - nested for example
#
# -------------------------
# for x in list1:
#   for y in list2:
#       list3.append(x*y)
# --------------------------
#
# the above nested loop can be written as
list1 = [1, 2, 3]
list2 = [10, 100, 1000]
list3 = [x*y for x in list1 for y in list2]
print(list3)

'''
(5) Output

[10, 100, 1000, 20, 200, 2000, 30, 300, 3000]

'''
