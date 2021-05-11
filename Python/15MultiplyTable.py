# Multiplication Table

numberInp = int(input('Multiplication of number: '))
uptoInp = int(input('Produce table upto: '))

for i in range(1, uptoInp + 1):
    print('{} x {} = {}'.format(numberInp, i, numberInp*i))
    
