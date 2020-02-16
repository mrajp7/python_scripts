# Similar to lists, however tuples are immutable
# Tuples uses (1,2,3) paranthesis instead of []

t = (1,2,3)

my_list = [1,2,3]

print(type(t))
print(type(my_list))

print(t)
print(my_list)


# Just like lists indexing and slicing are allowed on Tuples
print(t[-1])
print(t[::-1])

# 2 basics method for tuples
print(t.count(3))
print(t.index(3))

my_list[1] = 10 # this is allowed
# t[1] = 10     # this is not allowed

# Pros
# 1. Used in places where data integrity matters.
#    For instance: passing value as arguments in method and the data should not be allowed to modify