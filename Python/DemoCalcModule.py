# This is a example of self made module.
# This will be imported in others as demo module.

if(__name__ == '__main__'): # Only prints if it the main running file.
    print('I am from demo module: ', __name__)  # Prints __main__ if it is main running file, else filename is printed.

def addMe(x, y):
    print(x + y)

def subMe(x, y):
    print(x - y)

def mulMe(x, y):
    print(x * y)

def divMe(x, y):
    print(x / y)

