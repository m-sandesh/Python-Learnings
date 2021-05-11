# A program takes start, stop and end listing values

startInp = int(input('Enter Starting Value: '))
endInp = int(input('Enter Ending Value: '))
jumpInp = int(input('Enter Jumping Value: '))

print('Integers\t' + 'Squares\t\t' + 'Cubes')
for i in range(startInp, endInp, jumpInp):
    print('{}\t\t{}\t\t{}'.format(i, i**2, i**3))


