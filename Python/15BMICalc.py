# BMI Calculator

lowRange = 18.5
highRange = 24.9

userName = str(input('Enter your Name: '))
print('Enter Your Height: ')
userHeightFeet = int(input('Enter Feet : '))
userHeightInch = int(input('Enter Inch : '))
userWeight = float(input('Enter your weight(kg): '))

# Start Calc
meterHeight = float((userHeightFeet/3.281) + (userHeightInch/39.37))

bmiValue = userWeight/meterHeight**2

if bmiValue >= 18.5 and bmiValue <= 24.9:
    print('You scored ' + str(bmiValue) + '. You are average.')
else:
    print('YOU ARE OVERWEIGHT. You scored ', bmiValue)

