# Functions
# Normal Functions
def greetMe():
    print('Hello')


def add(a, b):
    print(a+b)


greetMe()

# Return Type Functions


def addReturn(a, b):
    return a+b


add(5, 5)
print(addReturn(5, 5))

# Multiple returns

def addSub(a, b):
    return a+b, a-b

addValue, subValue = addSub(5, 5)
print(addValue)
print(subValue)
