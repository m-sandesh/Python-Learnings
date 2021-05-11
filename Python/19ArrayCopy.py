import numpy as n

arr1 = n.array([1,2,3])
arr2 = n.array([3,2,1])

# Concatinate arrays
concatArr = n.concatenate([arr1,arr2])
print(concatArr)


# Copying array

# Shallow copy - Changes both
copyArr = arr1
print(copyArr)

# Deep copy - Changes only one
deepCopyArr = arr1.copy()
arr1[0] = 5
print(arr1)
print(deepCopyArr)  # Doesnt change value even change in another.

