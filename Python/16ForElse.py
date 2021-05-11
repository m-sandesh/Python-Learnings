# Requires a condition with 'break' inside a for loop

# Example: Search for divisibles by 5
x = [1, 2, 3, 4]

for i in x:
    if i % 5 == 0:
        print(i)
        break
    # else:   # Remove comment to see difference.
    #     print('No divisbles found.')
else:
    print('No Divisibles found.')

