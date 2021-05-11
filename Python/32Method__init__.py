class Computer:

    def __init__(self, name, cpu, ram):
        self.name = name
        self.cpu = cpu
        self.ram = ram

    # Example of methods vary as per the data from objects.
    def getConfig(self):
        print('{} has {} CPU and {} GB of RAM.'.format(self.name, self.cpu, self.ram))

    # Adding other methods
    def updateComputer(self, newName, newCpu, newRam):
        self.name = newName
        self.cpu = newCpu
        self.ram = newRam

    def compareComputer(self, anotherComputer):
        if self.cpu == anotherComputer.cpu and self.ram == anotherComputer.ram:
            return print('Configs Match.')
        else:
            return print('Configs NO Match.')

# Creating objects
com1 = Computer('Computer 1', 'i7', '16')   # Calling same construtor with different data.
com2 = Computer('Computer 2', 'i5', '8')


# Accessing methods with different object data
com1.getConfig()   # Calling same methods and outputs as per data from objects.
com2.getConfig()

com1.compareComputer(com2)

com2.updateComputer('Computer 2 NEW', 'i7', '16')
com2.getConfig()

com1.compareComputer(com2)
        

