# Map
'''
map(func, *iterables)
map(func, *iterables) --> map object

Make an iterator that computes the function using arguments from each of the iterables.
Stops when the shortest iterable is exhausted.
'''
# map can be ranged over.
# direct assignment of map(func,*iterables) will result in reference
# list(map(func,*iterables)) will provide a list of functions

# fucntion 2 to the power


def get_two_to_the_power(num):
    '''
    Description:
    To return the result of 2 to the power of given number
    2 to the power 0 is 1 hence we starting with two

    num:
    Input argument for 2 ^ (num)

    '''
    return 1 << num


num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(get_two_to_the_power, num_list))
print(list(zip(num_list, result)))

# the above example with List comprehension
result = [get_two_to_the_power(num) for num in num_list]
print(list(zip(num_list, result)))

# when function has 2 arguments


def concat_names(first, last):
    return f'Hello, {first} {last}!'


first_names = ['Mohanraj', 'Jawahar']
last_names = ['Palanisamy', 'Vignesh']
print(list(map(concat_names, first_names, last_names)))

# the above example with List comprehension
result = [concat_names(first, last)
          for first, last in zip(first_names, last_names)]
print(result)
