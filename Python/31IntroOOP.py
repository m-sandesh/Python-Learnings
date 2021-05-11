class Computer:

    def config(self):   # Self is auto generated taking object called by as a parameter.
        print('i9, 16GB, SSD1TB')

# Creating Objects
com1 = Computer()
com2 = Computer()

# Accessing methods with objects.
# Methods behave according to the object data.
# 1
Computer.config(com1)   # This is under the hood process of access of # 2 way.
Computer.config(com2)

# 2 BEST WAY
com1.config() # Here the object itself is passed as parameter which is denoting 'Self' in methods.
com2.config()
