class Employee:

    def __init__(self, id, name, dept):
        self.id = id
        self.name = name
        self.dept = dept
    
    def getEmp(self):
        print('Employee Name: ', self.name, 'Department: ', self.dept)
    
    class LaptopAssign():
        def __init__(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram
        
        def getEmpLaptop(self):
            print('Brand: ', self.brand, 'CPU: ', self.cpu, 'RAM: ', self.ram)
        
# Creating Objects
ram = Employee('001',  'Ram', 'IT')
ram.getEmp()
ram = Employee.LaptopAssign('Dell', 'i9', '16GB')
ram.getEmpLaptop()

hari = Employee('002',  'Hari', 'Accounts')
hari.getEmp()
hari = Employee.LaptopAssign('Dell', 'i3', '2GB')
hari.getEmpLaptop()

