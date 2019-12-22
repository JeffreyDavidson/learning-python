#
# Examples of working with functions
#

# Defining a basic function
def functionOne():
    print("I am a function")

# Functions can take arguments
def functionTwo(arg1, arg2):
    print(arg1, " ", arg2)

# Functions that return a value
def cube(x):
    return x*x*x

# Functions can have a default value for arguments
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# Functions can have variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

# functionOne()
# print (functionOne())
# print (functionOne)
# functionTwo(10, 20)
# print (functionTwo(10, 20))
# print (cube(3))
# print (power(2))
# print (power(2, 3))
# print (power(x=3, num=2))
# print (multi_add(4, 5, 10, 4))
