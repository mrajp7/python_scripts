# Sets are unordered collection of unique objects
# i.e., there can be only one representative for of the same object
# Note: Lists are ordered, Tuples are ordered, Dictionaries are unordered

# declaration

myset = set([1, 2])

print(myset)  # Output - {1, 2}

# add a new element
myset.add(3)
print(myset)  # Output - {1, 2, 3}

# add the same element
# since the element has to be unique it simple replaces/does do any operation
print(myset)  # Output - {1, 2, 3}


# dicard()
# remove a member of the set if persent
myset.remove(3)
print(myset)  # Output - {1, 2}

# remove the same element
# myset.remove(3) - raises a key error
print(myset)  # Output - {1, 2}

# clear() the set
myset.clear()
print(myset)  # Output - set()

# copy - Direct assignment (shallow copy)
set1 = set([2, 'a'])
set2 = set1  # direct assignmet - child/elements references are shared
print(set1)  # Output - {2, 'a'}
print(set2)  # Output - {2, 'a'}
set1.remove('a')
print(set1)  # Output - {2}
print(set2)  # Output - {2}

# copy() - Deep copy for sets
set1 = set([1, 2, 3])
set2 = set1.copy()
print(set1)  # Output - {1, 2, 3}
print(set2)  # Output - {1, 2, 3}
set1.add(4)
set2.remove(2)
print(set1)  # Output - {1, 2, 3, 4}
print(set2)  # Output - {1, 3}

# difference() of two sets.
# it returns a new set and not updates the current set
original_set = set([1, 2, 3, 4, 5])
print(original_set.difference([3, 4, 5, 6, 7, 8, 9]))  # Output - {1, 2}
print(original_set)                             # Output - {1, 2, 3, 4, 5}

# difference_update()
# it updates the original set with the difference between two sets
# does not return anything
original_set = set([1, 2, 3, 4, 5])
print(original_set.difference_update([3, 4, 5, 6, 7, 8, 9]))  # Output - None
print(original_set)                                    # Output - {1, 2}

# intersection() (common) of two sets.
# it returns a new set and not updates the current set
original_set = set([1, 2, 3, 4, 5])
print(original_set.intersection([3, 4, 5, 6, 7, 8, 9]))  # Output - {3, 4, 5}
print(original_set)                               # Output - {1, 2, 3, 4, 5}

# isdisjoint() - returns true if null intersection
print(original_set.isdisjoint(set([6, 7, 8, 9, 10])))  # Output - True
print(original_set.isdisjoint(set([6, 7, 2, 9, 1])))  # Output - False

# issubset() - returns true if the given set contains the original set
print(original_set.issubset(set([6, 7, 8, 1, 2, 10])))   # Output - False
print(original_set.issubset(set([3, 7, 2, 9, 1, 4, 5])))  # Output - True

# issuperset() - returns true if the given set is subset of the original set
print(original_set.issuperset(set([1, 2])))        # Output - True
print(original_set.issuperset(set([3, 7, 2, 9, 5])))  # Output - False


# cast list to set to get unique vales of a list
# however, the values will be unordered
my_list = [1, 1, 1, 1, 4, 4, 4, 4, 2, 2, 2, 2, 4, 4, 5, 6, 7, 7, 7]
myset = set(my_list)
print(myset)  # Output - {1, 2, 4, 5, 6, 7}

print(set('Mississippi'))  # Output - {'M', 'i', 's', 'p'}
