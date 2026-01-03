# indexing is used to access individual characters in a string
# syntax: [ start : end : step]

cardnumber = input("Enter your card number with dashes: ")
print(cardnumber[0])
print(cardnumber[1:4])
print(cardnumber[-1])

# using step:

print(cardnumber[::3])

# reversing a string using indexing
print(cardnumber[::-1])

name = "Aahan"
print(name[::-1])