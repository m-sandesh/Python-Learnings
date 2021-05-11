# Functions without names are lambda or anonymouse functions
# only used for functions that have only one statement.

# Normal Function
def squareMe(a):   # two lines used for one statement.
    return a * a


print(squareMe(5))


# lambda Functions
squareMeFunc = lambda a : a * a     # reduced to one line


print(squareMeFunc(5))

# Lamba Functions with multiple args


addMe = lambda a, b : a + b


print(addMe(5, 5))
