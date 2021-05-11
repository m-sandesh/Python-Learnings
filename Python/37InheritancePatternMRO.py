# MRO means Method Resolution Order which defines which method to call first if two method name is same during inheritance.
# MRO follows left to right pattern in inheritance as well as methods.
# Example:

class  A:
    def __init__(self):
        print('INIT A')

    def feature1(self):
        print('Feature 1A')

class  B(A):
    def __init__(self): # tries to call own constructor first, if found it will stop, if not found it looks for inherited class's constructor.
        print('INIT B')

    def feature2(self):
        print('Feature 2')

class C():
    def __init__(self):
        print('INIT C')
    
    def feature1(self):
        print('Feature 1C')

class D(A, C):
    def __init__(self):
        super().__init__()    # MRO defines to call constructor of A as it follows left to right order.
        print('INIT D')
    
    def feature1(self):     # Here top MRO is applicable and calls feature1 of class D.
        print('Feature 1D')
    
a1 = D()
a1.feature1()