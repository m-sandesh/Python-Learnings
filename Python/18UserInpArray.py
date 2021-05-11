from array import array

userArray = array('i',[])

userArrayLen = int(input('Enter length of array: '))

i = 0
for i in range(userArrayLen):
    arrayVal = int(input('Enter the value for ' + str(i) + ' : ' ))
    userArray.append(arrayVal)
    i += 1

indexOfVal = int(input('Find index of ? : '))

i = 0
for i in range(len(userArray)):
    if(userArray[i] == indexOfVal):
        print('Index number is: ', i)
        break
else:
    print('Index not found.')

# find index with function
print(userArray.index(indexOfVal))

