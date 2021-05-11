import functools as ft   # import reqired for reduce functions

# Functions with lambdas
myNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Filters
# Filter - Long procedure
def getEven(n):
    n % 2 == 0

print(list(filter(getEven, myNums)))

# Filter - with lambdas
print(list(filter(lambda n : n % 2 == 0, myNums)))

# 2. Maps
# Long procedure is similar to filters
# Maps with lambdas: 
print(list(map(lambda n : n * 2, myNums)))

# 3. Rdeuce
# long procedure is similar to filters and maps
# Requires import from functools
# Reduce with lambdas:
print(ft.reduce(lambda a,b : a + b, myNums))
