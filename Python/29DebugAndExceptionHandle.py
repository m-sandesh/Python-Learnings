# Debuggiing using Print
# To only check if values are in going in right path.

a, b = 5, 10

print(a, b)  # This is Debug line.


# Exception Handling
# Use TRY and EXCEPT
# Not let an error to stop the program

# Division Example:

def divideRule():
    divisibleInp = int(input('Enter a number to divide: '))
    divisorInp = int(input('Enter number to divide: '))

    try:
        # Just an example if used with DB Connection where open/close is required.
        print('resource open')
        print('Result: ', (divisibleInp/divisorInp))

    except ZeroDivisionError as ex:  # Being error specific
        print('Error: Divisor cannot be 0. Try again.')

    except Exception as ex: # if unknown errors might occur.
        print('Error: ', ex)
        
    finally:
        print('resource close')
        divideRule()

divideRule()
