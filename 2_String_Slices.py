# Arithmetic operators

print((((2 ** 6) // 3) % 2 * 50) / 2 + 100 - 25)

# ** - Exponential
# % mod
# // quotient only

# string operations

sample = "This is a sample string"

print(sample)

# Escape sequences
print("hello \nworld")

# Length of a string
l = len(sample)
print(l)

# Indexes on a string
print("printing same with indexing")

# T h i s   i s   a . . .
# 0 1 2 3 4 5 6 7 8 . . .

print(sample[2])

# Negative indexes on a string

sample = 'hello'
# h  e  l  l  o
# 0 -4 -3 -2 -1

print(sample[-1], sample[-4])

# Slice of a string
# to fetch a subset of a string

# syntax [start:stop:step]
# `start` - starting index
# `stop` - upto index (but not include)
# `step` - is the size of the jump you take from start to stop

s = "hello_world"

print(len(s))

print(s[1:])

print(s[:3])

print(s[1:11])

print(s[1:11:1])

print(s[1:11:2])

print(s[1:11:3])

print(s[::2])

# To print in reverse order
print(s[::-1])

# String Properties and Methods

# strings are Immutable

name = 'Sam'
# name[0] = P - will not work

name = 'P' + name[1:]

print(name)

name = name * 10

print(name)


#################################
# string methods

print(name.upper())

print(name.split())  # default is space

f = "the {} {} {}"
print(f.format('fox', 'brown', 'quick'))

f = "the {0} {0} {0}"
print(f.format('fox', 'brown', 'quick'))

f = "the {q} {b} {f}"
f = f.format(b='brown', f='fox', n='nothing', q='quick')
print(f)


# Float formmating
# {value:width.precision f}

val = 123.123456
print('the result is {0:1.4f}'.format(val))
print('the result is {v:10.4f}'.format(v=val))  # width simply add/hold spaces

# f string $ from python 3.6

print(f'the result is {val:1.5f}')
name = 'mohan'
print(f'the name is {name}')
