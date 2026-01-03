# membership operators : used to test whether a value or variable is found in a sequence    
#                        (string, list, tuple, set, dictionary)
#                         1. in
#                         2. not in
# STRINGS:
word = "APPLE"

letter = input("Enter a letter: ").upper()

if letter in word:
    print(f"{letter} is present in {word}")
else:
    print(f"{letter} is not present in {word}")

# same thing using not in:

if letter not in word:
    print(f"{letter} is not present in {word}")
else:
    print(f"{letter} is present in {word}")

# LISTS, TUPLES, SETS:

students = {"Aahan", "Shweta", "Rohan", "Priya"}

student = input("Enter student name: ").title()

if student in students:   # not in can also be used here
    print(f"{student} is present in the class")
else:
    print(f"{student} is not present in the class")

# DICTIONARIES: by default it checks for keys


grades = {
    "Aahan" : 95,
    "Shweta" : 98,
    "Rohan" : 88,
    "Priya" : 92
}
name = input("Enter student name: ").title()

if name in grades:
    print(f"{name} is there in this class and has received {grades[name]}")
else:
    print(f"{name} was not found!!!!!!!!")

# another example for dictionaries:

email = "aahan.agrim@gmail.com"

if "@" in email and "." in email:
    print(f"{email} is valid!")
else:
    print(f"{email} is invalid!")