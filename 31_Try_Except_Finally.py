# just like any other language try_except_finally is used for error handlin
# try: any statements to get executed
# except: any error is occurred in try will be handled here
# finally: whether or not any errors, the statements under finally will executed

while True:
    try:
        result = int(input("enter a number"))
        break
    except ValueError:
        print("Oops! i asked you a number")
    finally:
        print("Thank you!")

try:
    file1 = open("dfsdfds", 'r')
    file1.write("asdsad")
except FileNotFoundError:
    print("the operation cannot be done")
else:
    # this gets executes if there is no error
    print("I was able to write to the file")
