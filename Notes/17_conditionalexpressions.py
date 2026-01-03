# conditional expressions is basically ternary operator in java

# example:

num = -6
print("postive" if num > 0 else "negative or zero")


# it can also be ssigned to a variable:

number = 76
result = "even" if number % 2 == 0 else "odd"
print(result)

# another example:

a = 5
b = 8

max_num = a if a > b else b
print(max_num)