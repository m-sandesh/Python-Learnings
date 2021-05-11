import array as arr
# from array import * # To remove use of 'arr' everytime.

studentMarks = arr.array('i', [2,30,45,50,90])  # i represnts datatype of array which is int here.

# accessing array
print(studentMarks[3])

studentMarks.append(95)

# using for loop
for i in studentMarks:
    print(i)

# using while loop
i = 0
while i < len(studentMarks):
    print(studentMarks[i]) 
    i += 1
