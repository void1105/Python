# iterables = An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop.
# lists are iterable:
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number, end = " ")
print()
# to print the same thing reversed:
for number in reversed(numbers):
    print(number)

# tuples are also iterable:

numbers_tuple = (10, 20, 30, 40, 50)

for number in numbers_tuple:
    print(number, end = " ")
print()
# sets are also iterable:    sets cannot be reversed as they are unordered collections
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)

# strings are also iterable:

name = "Aahan Gupta"
for char in name:
    print(char, end = " ")
print()

# dictionaries are also iterable: by default it iterates over keys:

my_dict = {
    "A" : 1,
    "B" : 2,
    "C" : 3
}

for key in my_dict:
    print(key, end = " ")
print()
    # to print values:

for values in my_dict.values():
    print(values, end = " ")
print()

    # to print key-value pairs:

for x, y in my_dict.items():
    print(f"{x} : {y}")