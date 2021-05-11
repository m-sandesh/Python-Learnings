# Polymorphism

# 3 Method Overloading:
# In python, same name of methods in a class is not possible so overloading is acheivec indirectly.
# Using nulls and conditionals.
# Example:
class loadCheck:

    def sumCheck(self, a = None, b = None, c = None):
        if a != None and b != None and c != None:
            sum = a + b + c
        elif a != None and b != None:
            sum = a + b
        else:
            sum = a
        
        return sum
    
load = loadCheck()
print(load.sumCheck(10, 10))

print('================')
# 4 Method Overriding:
# Overrriding a method using inheritance
# Example: Class A and B has same name of method. If B inherits A and Object of B calls that method, then method of B overrides method of A.

class A:
    def calc(self, a, b):
        print(a + b)

class B(A):
    def calc(self, a, b):
        print(a * b)

iamB = B()
iamB.calc(4, 4)