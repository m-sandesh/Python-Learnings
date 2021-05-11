# Lists
# Index starts with 0

myList = ['Hello', 'I', 'am', 'San']
print(myList)
print(myList[2])

myNumbers = [9,8,1,3,8,0,4,1,5]
print(myNumbers)

# some list functions
myNumbers.sort()
print(myNumbers)

myNumbers.reverse()
print(myNumbers)

# mixed lists
myMix = ['Hello', 2, 'I']
print(myMix)

# Types of list
# Mutable --> Can be changed. Ex. Array, lists
# Non Mutable --> Cannot be changed. Ex. tuples
# Difference: List-->[], Tupple-->(), Set-->{}, Dictionary-->{key:value}

# Tuples
myTuple = (1, 2, 3)
print(myTuple)
print(myTuple[1])
# myTuple[1] = 5      # cannot be changed example.

myTupleAnother = (1, )     # Comma is necessary if tuple has single element.
print(myTupleAnother)

# Sets
# Sets are mutable but only outputs unique values which are not repeated within a set.
# these are mutable and can use functions push pop functions similar to lists.

# Dictionary
# A key value pair.
HusbandsWife = {'Ram':'Sita','Hari':['Gita','Rita'],'Gopal':{'Sami':'Rohan','Mina':'Ravi'}} # 2 wifes of hari using LIST and gopal wifes and their childrens.

# Accessing the value using pairs.
print(HusbandsWife)
print(HusbandsWife['Hari'])
print(HusbandsWife['Hari'][1])   # second wife of hari
print(HusbandsWife['Gopal']['Sami'])   # child of 1st wife


