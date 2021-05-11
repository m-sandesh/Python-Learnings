# Type of variables in OOP
class Car:
    wheels = 4  # <-- Class variables under class namespace.

    def __init__(self, name, wheels):
        self.name = name    # <-- Instance Variables under instance namespace.
        self.wheels = wheels

        print('Company Name: {} of {} wheels.'.format(self.name, self. wheels))

Car.wheels = 6  # Can only be changed with its own namespace ie. class variable.

# Creating object
companyBMW = Car('BMW', Car.wheels)
companyAudi = Car('Audi', Car.wheels)




