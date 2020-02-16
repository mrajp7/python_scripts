# Lambda is also known as anonymous function
# The main use of a Lambda is to define a function and where it can be used only once
# and not to occupy your script or project's space.

# Disclaimer - Always use regular function for better readability
#            - Use lambda if the operation is easy to read

# Let's create a function and reduce it to lambda function

# (1)


def square(num):
    result = num ** 2
    return result


print(f'square - {square(4)}')

# (2)


def square_reduced1(num):
    return num ** 2


print(f'square_reduced1 - {square_reduced1(4)}')

# (3)


def square_reduced2(num): return num ** 2


print(f'square_reduced2 - {square_reduced2(4)}')

# (4)


def square_reduced3(num): return num ** 2


print(f'square_reduced3 - {square_reduced3(4)}')


# (6) usage example on map
result = list(map(lambda num: num ** 2, [4, 5]))
r1, r2 = zip([4, 5], result)
print(f'Square using lambda - {r1}{r2}')

# (7) usage example on filter
result = list(filter(lambda num: not num & 1, list(range(1, 30))))
print(result)


# (8) usage example on getting First Name from string list
names = ['Mohanraj P', 'Praveena NJB', 'Dhanushvigaa M']
print(list(map(lambda n: n.split()[0], names)))

# (9) usage example on reversing each of the string in a list
print(list(map(lambda n: " ".join([rs[::-1] for rs in n.split()]), names)))

# - however the above function is not readable without lambda
# - let's write it in a readable way


def reverse_string(rs):
    result = []
    for s in rs.split():
        result.append(s[::-1])
    return " ".join(result)


result_list = list(map(reverse_string, names))
print(result_list)
