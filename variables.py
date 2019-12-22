#
# Learning about variables
#

# Declare a variable and initialize it
f=0
print(f)

# Redefining variables is possible with separate types
f="abc"
print(f)

# ERROR: variables of different types cannot be combined
print("this is a string " + 123)

# WORKS: values can be transformed into a string 
print("this is a string " + str(123))

# Global vs local variables in functions
def functionOne():
    global f
    f="def"
    print(f)

# Shows local f value
functionOne()

# Shows global f value 
print(f)

# Throws global name error as variable is undefined
del f
print(f)
