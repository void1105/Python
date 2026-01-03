# DICTIONARIES:  a collection of {key: value} pairs
# ordered, changeable, indexed, no duplicate keys allowed
# can use dir and help functions to check all methods

capitals = {"India" : "New Delhi", "USA" : "Washington D.C.", "France" : "Paris"}
print(capitals)

# to geta value, use the key:
print(capitals.get("India"))
# if the key is not found, it returns None instead of error
print(capitals.get("Germany"))

if capitals.get("Japan"):
    print("this capital is found")
else:
    print("not found")


if capitals.get("USA"):
    print("this capital is found")
else:
    print("not found")

# to add a key-value pair:

capitals.update({"Germany" : "Berlin"})
print(capitals)

# to change a value of a key:
capitals.update({"India" : "Dehli"})

print(capitals)

# to remove a key-value pair:
print(capitals.pop("France"))
print(capitals)

# to remove the last inserted key-value pair:
capitals.popitem()
print(capitals)

# to print only keys:
keys = capitals.keys()
print(keys)

for x in keys:
    print(x, end = "\n")

# to print only values:
values = capitals.values()
print(values)

for i in values:
    print(i, end = "\n")


items = capitals.items()
print(items)

for a, b in items:
    print(f"{a} : {b}")

#to clear the dictionary:
capitals.clear()
print(capitals)

