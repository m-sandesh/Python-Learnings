# passing list as arguments

numberList = [15, 11, 23, 432, 44, 56, 78]


def seperateEvenOdd(argList):
    evenCount = 0
    oddCount = 0

    for i in argList:
        if i % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1

    return evenCount, oddCount


even, odd = seperateEvenOdd(numberList) # two varaibles catching two returns

print('Total Evens: {} Total Odds: {}'.format(even, odd))   # Some string formatting tricks




# Seperate names by character counts

# nameList = ['Ram', 'Shyam', 'Hari']
nameList = []

userInpListSize = int(input('Enter number of names: '))

for i in range(0,userInpListSize):
    userInpListValue = str(input('Enter Name for serial {}: '.format(i + 1)))
    nameList.append(userInpListValue)

def countChars(argList):
    charCounter = 0

    for i in argList:
        charCounter = len(i)
        print('Character Count of {} is {}.'.format(i, charCounter))

countChars(nameList)

    