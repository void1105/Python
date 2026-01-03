name = input("What is your name?")

# len method - gives length of string

result_len = len(name)
print(result_len)

# .find method - finds the first occurrence of a substring in a string

result_find = name.find("h")
print(result_find)  

# .rfind method - finds the last occurrence of a substring in a string

result_rfind = name.rfind("a")
print(result_rfind)

# if the substring is not found, it returns -1

# capitalize method - capitalizes the first letter of the string
result_capitalize = name.capitalize()
print(result_capitalize)


# upper method - converts the string to uppercase
result_upper = name.upper()
print(result_upper)

# lower method - converts the string to lowercase
result_lower = name.lower()
print(result_lower)

# isdigit method - checks if all characters in the string are digits
result_isdigit = name.isdigit()
print(result_isdigit)

# isalpha method - checks if all characters in the string are alphabets
result_isalpha = name.isalpha()
print(result_isalpha)

# .count method - counts the number of occurrences of a substring in a string

phone = input("Enter your phone number: ")
result_count = phone.count("9")
print(result_count)

# .replace method - replaces a substring with another substring in a string
result_replace = name.replace("a", "@")
print(result_replace)


# .strip method - removes leading and trailing whitespaces from a string
greeting = "   Hello, World!   "
result_strip = greeting.strip()
print(result_strip)

# .startswith method - checks if the string starts with a specified substring
result_startswith = name.startswith("A")
print(result_startswith)

# .endswith method - checks if the string ends with a specified substring
result_endswith = name.endswith("n")
print(result_endswith)

# .split method - splits the string into a list of substrings based on a specified delimiter
sentence = "Hello world, welcome to Python programming."
result_split = sentence.split(",")
print(result_split)

# .join method - joins a list of strings into a single string with a specified delimiter
words = ["Hello", "world", "welcome", "to", "Python"]
result_join = " ".join(words)
print(result_join)

# to check all strings, use:
print(help(str))

