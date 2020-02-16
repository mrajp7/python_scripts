# Unordered lists
# key-value pair unlike lists which are indexed and ordered objects
# uses {} and : to separat key and values
# Dictionaries cannot be sorted
# no indexing, slicing allowed here


price_lookup = {'lemon':30, 'orange':60, 'grape':50, 'watermelon':30, 'watermelon mint':40, 'lemon mint':40}
print(price_lookup)

print(price_lookup['lemon mint'])

# dictionaries can hold various object types in value
dict_ = {1:'abc',2:23, 3:4.123, 4:[1,'b', 3], 5:price_lookup}
print(dict_)

for k,v in dict_.items():
    print(v)


print(dict_[5]['watermelon'])

# add key,value to dictionary
dict_[6] = 'newly added'

print(dict_)

# Modify existing value
dict_[6] = 'modified'
print(dict_)

# Get all keys
print(dict_.keys())

# Get all values
print(dict_.values())

# Get a tuples of all items in the dictionary
print(dict_.items())

