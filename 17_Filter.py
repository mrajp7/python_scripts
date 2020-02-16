# Filter

'''
filter(functionorNone, iterable)
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item) is true. 
If function is None, return the items that are true.

'''


def check_even(num: int):
    '''
    Description:
    to check whether a number is even or odd

    num:
    number to act on
    '''
    return not num & 1


nums = list(range(1, 20))
result = list(filter(check_even, nums))
print(result)

# the above example in List comprehension
result = [num for num in nums if check_even(num)]
print(result)

# example for filter without function
# to skip the False value
result = list(filter(None, [0, 2, 4, 0, 4, 1, 5, 0, 7, -1, -5]))
print(result)
# the above example in List comprehension
print([val for val in [0, 2, 4, 0, 4, 1, 5, 0, 7, -1, -5] if val])

# to skip an empty string
result = list(filter(None, ['', 'a', 'c', '', ' ', '    ', 'd']))
print(result)

# the above example in List comprehension
print([val for val in ['', 'a', 'c', '', ' ', '    ', 'd'] if val])
