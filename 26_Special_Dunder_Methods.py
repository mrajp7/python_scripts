# Methods that uses double underscore method
# Example __init__,__str__
#


my_list = [1, 2, 3]

print(len(my_list))


class sample():
    pass


mysample = sample()

# this will fail.
# 'print(len(mysample))' # TypeError: object of type 'sample' has no len()


# print on any given object
# whenever print is called on an object it tries to print the string version of the object.
# if no string special method is not defined it prints default address location of the object
# on the above list example __str__ would have been declared for list class

print(mysample)  # print the object reference
print(len(my_list))

# Lets see an example for __str__ method in the below example


class Book():

    def __init__(self, category, title, author, pages):
        self.category = category
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"The book '{self.title}'' is written by '{self.author}''"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("The book is removed from the collection")


my_book = Book("Fantasy", "The Hobbit", "J.R.R Tolkien", 400)
print(my_book)
print(len(my_book))

# del method can act on any method.
# it simply removes the object from the memory.
# however if a class has to do some action upon del, then it has to implement __del__ speical method on the class defintion.
# if __del__ is not implemented, python simply removes the object from memory.
del my_book
