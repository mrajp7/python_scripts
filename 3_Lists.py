my_list = [1,'mohan',2,'raj']

print(len(my_list))

print(my_list[1])

print(my_list[1:])
print(my_list[1:4:2])
print(my_list[::1])


# Lists are mutable

my_list[1] = 'm'

print(my_list)

# Concat on lists
my_list = my_list + [3,'pravee']
print(my_list)

# Methods on List
my_list.append(4) # adds to the list permanently
my_list.append('Dhanu')

print(my_list)

my_list.reverse() # modifies the list permanently
print(my_list)

my_list.insert(0,'not a valid data') # index, value, modifies the list permanently
print(my_list)

print(my_list.pop()) # deletes the value at the last index and returns the removed value
# also pass the index as argument to pop to remove the value at the index
# ex my_list.pop(1) ot the item at index 1
print(my_list)

my_list.remove('not a valid data')
print(my_list)

num_list = [2,44,23,12,4,100]
print(num_list)

num_list.sort() # doesn't return anything. None. Modifies the list permanently
print(num_list)

mixed_list = [23, 43, 'mod', 'a', 1]
#mixed_list.sort() # cannot perform this since the objects in the list are not of same types
#print(mixed_list)