# Polymorphism

# 2 Operator Overloading:
# Inbuilt magic methods example: __add__(), __mul__(), etc.
# when '+' is written, in will invoke __add__() and this method does its work as per integer or string.
# If we had to had objects not int and str, we have to make our own with same name shown in example:

# Example:
class Student:
    def __init__(self, mark1, mark2):
        self.mark1 = mark1
        self.mark2 = mark2

    def __add__(self, otherArg):    # Args --> (s1, s2)
        m1 = self.mark1 + otherArg.mark1    # s1.mark1 + s2.mark1
        m2 = self.mark2 + otherArg.mark2
        s3 = Student(m1, m2)    # Constructor call to save m1 and m2
        return s3

    def __gt__(self, otherArg):
        m1 = self.mark1 + otherArg.mark1    # s1.mark1 + s2.mark1
        m2 = self.mark2 + otherArg.mark2
        if(m1 > m2):
            return True
        else:
            return False

    def __str__(self):
        # return self.mark1, self.mark2   # Returns in tupple.
        return '{} {}'.format(self.mark1, self.mark2)   # Returns in string for priting.
    

s1 = Student(50, 60)
s2 = Student(100, 60)

# Addnig two objects
s3 = s1 + s2    # Calls our custom defined __add__() with MRO rules.

# Under the hood calling process
# Student.__add__(s1, s2)   

print(s3.mark1, ' ', s3.mark2)

# Comparing two Objects (Another Example)
if s1 > s2:
    print('s1 is great.')
else:
    print('s2 is great.')

# getting value of object (another example)
# __str__() helps to produce value of a variable. like: myVariable.__str__()
# in object it is the same but instead value it prints address of object.
# to overload this we have to custom a __str__() funciton too.
print(s1)   # Now gives value instead of address.
