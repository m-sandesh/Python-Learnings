# Types of Methods in OOP
class Student:

    schoolName = 'SMCS'

    def __init__(self, name, grade, roll, school):  # Instance Method: self is compulsary
        self.name = name
        self.grade = grade
        self.roll = roll
        self.school = school
    
    def getName(self):    # Instance Method: self is compulsary
        return self.name

    def setName(self, name):    # Instance Method: self is compulsary
        self.name = name

    @classmethod
    def getSchoolName(cls):     # Class Method: @classmethod and cls as args are compulsary.
        print('School name is: ', Student.schoolName)   

    @staticmethod
    def getInfo():  # Static Method: normal function but @ staticmethod is compulsary
        print('This is from Student Class from a Module.')

# Creating objects
Ram = Student('Ram', '10', '1', Student.schoolName)
Hari = Student('Hari', '9', '1', Student.schoolName)

# Access of types of methods
# Instance Methods
print(Ram.getName())
Ram.setName('RamRai')
print(Ram.getName())

# Class Methods
Student.getSchoolName()

# Static Methods
Student.getInfo()
Ram.getInfo()

