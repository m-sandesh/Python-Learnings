# Decorators
# Helps to modify an inaccessible function

# Suppose this func is not accessible and we need to check if a < b within the function.
def minusFunc(a, b):
    print(a - b)

# To add statements within the fucntion, decorators are used.

def decoratedMinusFunc(decFunc):
    def innerFunc(a, b):
        if a < b:
            a, b = b, a
        return decFunc(a, b)
    return innerFunc

# Calling minusFunc indirectly using decorated function
# Creating newMinus function.
newMinus = decoratedMinusFunc(minusFunc)

newMinus(10, 15)

