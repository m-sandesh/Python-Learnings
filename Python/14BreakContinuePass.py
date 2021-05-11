# Break: Candy Machine
# Breaks entire loop

candyLeft = 10
userInp = int(input('How many candies you need?'))

i = 0
while i < userInp:
    if(i > candyLeft):
        print('Candies out of stock. Candies out: ', i-1)
        break
    print('CandyOut')
    i += 1


# Continue: Remove divisible by 3 and 5 only
# Continues loop skipping a statement next

for i in range(0, 100, 1):
    if(i % 5) == 0 or (i % 3) == 0:
        continue
    else:
        print(i)

# Pass
# pass is just used to say the code that the block is empty.
# Example:
if 0:
    pass

