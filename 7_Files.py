# simple i/o with basic.txt

# To open a file
myfile = open("basic.txt")

# Filepaths notation
# Windows - "C:\\Users\\SomeUser\\file.extension"
# Mac/Linux - "/Users/SomeUser/file.extension"

# read()
print(myfile.read()) # reads till the end of file

# read() - again on the same reader doesn't work
# because the reader has parsed until the eof on the previous step
print(myfile.read()) # Output - ''

# seek() - to rest the reader on any position of the reader
myfile.seek(0)
print(myfile.read()) # Output - '<< content of the file >>'

myfile.seek(0)
contents = myfile.read() # to assign a read content

# readlines()
# returns a list of each lines
myfile.seek(0)
print(myfile.readlines())
myfile.seek(0)
print(myfile.readline()) # read only a line

# close()
# if a file is opened it has to be closed at the end, so we dont cause errors for accessing the file from other resource
myfile.close()

# A file can also be opened with a limited lifetime within a given block of statements 
# no longer need to worry about closing a file
contents = None
with open("basic.txt") as file1:
    contents = file1.readlines()
print(contents)

# open file with mode 'r' | r - read, w - write (create new file, if doesn't exist), a - append, r+ - read and write, w+ - write and read (creates new file doens't exist)
with open("basic.txt", mode='r') as file1:
    contents = file1.readlines()

# over writes
with open("sample.txt", mode='w') as file1:
    file1.write("Sample data\nfirst line\nsecond line")

# append
with open("sample.txt", mode='a') as file1:
    file1.write("\nthird line")
