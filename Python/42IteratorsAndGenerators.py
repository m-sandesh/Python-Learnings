# Iterators:
# Iterates value with help of inbuilt functions iter() and next()
num = [1, 2, 3, 4, 5]

iterates = iter(num)

print(iterates.__next__())  # these both outputs works same. these remember their previous value and itterates.
print(next(iterates))

for i in iterates:  # print all values.
    print(i)


print('========')
# Generators:
# Generates values like iterators but more automation and simplicity in generators.
# Used in DB to fetch data slowly without harming ram resources.
def square():
    n = 1

    while n <= 10:
        sq = n * n
        yield sq    # instead of return yeild is used to convert function to a generator.
                    # yeild doesnt break immediately like return after returning values.

        n += 1

squareValues = square()

for i in squareValues:
    print(i)