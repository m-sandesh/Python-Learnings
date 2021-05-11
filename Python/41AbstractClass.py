# Abstract Class and Methods:
# A declared method with no body is abstract method and a class having it is a abstract class.
# An abstract class must have an abstract method.
# Python doesnt support by default so, ABC needs to be imported.
# ABC stands for Abstract Base Classes.
# Cannot create objects of abstract class.

from abc import ABC, abstractmethod

class Computer(ABC):    # ABC needs to be inheritted by class.

    @abstractmethod     # decorators are must to to declare absract method.
    def config(self):
        pass

class Laptop(Computer):
    def config(self):
        pass

# Simple syntax example
# NOT UNDERSTOOD INDEPTH. TO BE CONTINUED.
