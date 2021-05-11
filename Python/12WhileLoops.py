i = 1

while i <= 5:
    j = 1
    print('I am printed for ' + str(i) + ' times.', end = "")
    while j <= 5:
        print(' I am its child one.', end="")
        j += 1

    print()
    i += 1
