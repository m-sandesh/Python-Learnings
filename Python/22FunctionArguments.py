# Actual Arguments
# During Function creation
    # Postion Driven
def name(first, last):
    print(first , last)

    # Keyword Driven
def nameKeyword(first, last):
    print(first , last)

    # Default Value Assigning -> Assigns default value
def person(name, age = 18):
    print(name, age)

    # Variable Length Arguments -> when no. of arguments is not fixed
def add(a, *b):#  if arguments are more than 2 then b is assigned with values as tuple
    for i in b:
        a = a+i
    print(a)

    # Keyword Varaible Length Args -> when no. of args is not fixed and args are also not clear enough.
def personKeyVar(name, **personData): # double * is the difference from varaible length args
    print(name)
    for i, j in personData.items():
        print(i, j)


# Formal Arguments
# During function calling
    # Position Driven->Position is strictly to be followed
name('San', 'Mhj')

    # Keyword Driven -> If position is not known, keyword can be used
nameKeyword(last='Mhj', first='San')

    # Default Value Assigning
person('San')

    # Variable Length Arguments
# add(5,5)
add(5,5,5,5)

    # Keyworded Variable length arguments
personKeyVar('San', age = 20, addr = 'KTM', phone = 9841)

