
myText = 'This is San.'

print(myText)

# index of chars start with 0
print(myText[1])

# print only particular range of chars
print(myText[0:8])
print(myText[0:50])     # Not required to be actual length.

# length of string
print(len(myText))

# Skipping characters
print(myText[0:50:2])   # skipping 1 items between each index.
print(myText[:])    # print everything without limitations

# Characters in reverse
print(myText[-1:])    # in reverse index starts with -1
print(myText[-50:-1])
print(myText[::-1])      # completely inverse the string

# some other functions
print(myText.isalnum())
print(myText.isalpha())
print(myText.endswith("hey"))
print(myText.count("o"))
print(myText.capitalize())
print(myText.find("is"))



