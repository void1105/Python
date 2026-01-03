# collectipns: list, sets, tuple
# list = ordered collection of items which is mutable (can be changed)
# sets = unordered collection of unique items
# tuple = ordered collection of items which is immutable (cannot be changed)

# list:

fruits = ["apple", "banana", "cherry", "mango", "mango"]

for fruit in fruits:
    print(fruit)

# to check all list mwthods, use:
# print(dir(fruits))
# print(help(fruits))

# to check lenght of list:
print(len(fruits))


# to check if a item is in the list:
print("apple" in fruits) 
# or:
if "apple" in fruits:
    print("Yes, apple is in the list.")

# to change an item in the list:

fruits[0] = "pineapple"

print(fruits[0])

# to add an item to the list:

fruits.append("straw-berry")
print(fruits[-1])

# to remove an item from the list:
# fruits.remove(fruits[0])
# or
fruits.remove("pineapple")
print(fruits)


# to insert an item at a specific index:

fruits.insert(2, "kiwi")
print(fruits)

# to count occurrences of an item in the list:
print(fruits.count("mango"))

# to sort the list:
fruits.sort()
print(fruits)

# to reverse the list:
fruits.reverse()
print(fruits)
# to print the index of an item in the list:
print(fruits.index("kiwi"))

# to clear the list:

fruits.clear()
print(fruits)

# to pop(remove the last from it):
# fruits.pop()
print(fruits)


# SET:

numbers = {"1", "2", "3", "4", "5"}
print(numbers)
# can use dir and help functions to check all set methods

# to check lenght of set:
print(len(numbers))

# to check if an item is in the set:
print("3" in numbers)

# to add a item in a set:

numbers.add("6")
print(numbers)


# to remove a item from the set:

numbers.remove("1")
print(numbers)

# to pop(removes random):
numbers.pop()
print(numbers)


# to clear a set:
fruits.clear()


# TUPLE:

colours = ("violet", "indigo", "blue", "green", "yellow", "orange", "red", "blue")

# can use dir and help for this too

# to check length:
print(len(colours))

# to check if a intem is in a tuple:

print("orange" in colours)


# to check the index:

print(colours.index("red"))

# to check the no. of an item in a tuple:

print(colours.count("blue"))


# LISTS- ORDERED AND CHANGABLE, DUPLICATE OK
# SETS- UNORDERED AND IMMUTABLE, ADD/REMOVE OK, NO DUPLICATE
# TUPLE- ORDERED UNCHANGEABLE. DUPLICATES OK. FASTER