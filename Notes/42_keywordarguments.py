# keyword argument = An argument preceded by an indentifier
#                    helps with readability
#                    allows us to pass arguments in any order
#                    1. positional 2. default 3. KEYWORD 4. arbitrary


def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello(title = "Mr.", first = "Aahan", last = "Gupta", greeting = "Hello")# the order of arguments can be changed while using keyword arguments
# if we want to use positional arguments and keyword arguments together, positional arguments should be given first


# a built in keyword argument example:
# for x in range:
#     print(x, end = " ")  # here end is a keyword argument which changes the default behaviour of print function to print in new line after each print statement to printing in same line with space in between

# another one is:
# the separate(sep) keyword argument in print function which changes the default behaviour of print function to separate the values with sep value instead of space
print("1", "2", "3", sep = " < ")

# phone number exercise:

def number(country_code, first5, last5):
    return f"+{country_code} {first5}-{last5}"

print(number(country_code = 91, last5 = 80939, first5 = 85956))