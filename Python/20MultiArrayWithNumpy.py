import numpy as n


# Multideminsional Array
# without Numpy Mutli Array is not supported.

myMarks = n.array([
                    [1,2,3],
                    [3,2,1],
                    [3,6,9]
                ])


print(myMarks)
flatMarks = myMarks.flatten()   # Combine all arrays in one big array
print(flatMarks)

# reMarks = flatMarks.reshape(2,2,3)   # Combine all arrays in one big array
# print(reMarks)

myMatrix = n.matrix('1 2 3 ; 4 5 6 ; 7 8 9')
myMatrix2 = n.matrix('1 2 3 ; 4 5 6 ; 7 8 9')
print(myMatrix)

print(myMatrix + myMatrix2)


