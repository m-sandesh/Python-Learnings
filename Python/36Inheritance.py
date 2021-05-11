# Basic understanding example only:

class A:
    def useFeature1(self):
        print('Feature 1')

    def useFeature2(self):
        print('Feature 2')
    
class B(A): # Single level Inheritance using ( )
    def useFeature3(self):
        print('Feature 3')

    def useFeature4(self):
        print('Feature 4')

class C(B): # Multilevel inheritance as B already inherit A
    def useFeature5(self):
        print('Feature 5')

class D: 
    def useFeature6(self):
        print('Feature 6')

class E(A, D):  # Multiple inheritance in a class 
    def useFeature7(self):
        print('Feature 7')

# Creating Objects
A1 = A()
A1.useFeature1()

B1 = B()
B1.useFeature2()
B1.useFeature3()

C1 = C()
C1.useFeature4()
C1.useFeature5()

D1 = D()
D1.useFeature6()

E1 = E()
E1.useFeature1()
E1.useFeature6()
E1.useFeature7()



