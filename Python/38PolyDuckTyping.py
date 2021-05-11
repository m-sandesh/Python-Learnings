# Polymorphism
# Multiple forms of an object.

# Types:
# 1 Duck Typing (Similar to interface in Java)
# 2 Operator Overload
# 3 Method Overload
# 4 Method Override

# 1 Duck Typing:
# Named duck typing because, if a bird can walk and swim them its a duck.
# To acheive duck typing, classes to be executed must have same function names.

class Laptop:
    def useMe(self):
        print('Laptop Unit')
        print('External Compenents')

class Computer:
    def useMe(self):
        print('CPU Unit')
        print('Monitor')
        print('Keyboard')
        print('Mouse')
        print('External Components')

class PC:
    def whatPC(self, device):
        device.useMe()

useDevice = Computer()  # useDevice defines which class to use to execute whatPC().

myPC = PC()
myPC.whatPC(useDevice)  # Stable call. Only useDevice would change the situation.