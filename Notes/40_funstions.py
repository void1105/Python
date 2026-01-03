# function = a block of re usable code
# place () after the function name to invoke it

def happy():
    print("Happy bday to u")
    print("Happy bday to u")
    print("Happy bday to u")

happy()
happy()
happy()
happy()

# function with parameters(arguments) these are positional arguments

def happy_bday(name, age):
    print(f"Happy bday dear {name}")
    print(f"u r {age} years old")
    print("Happy bday to u")

happy_bday("Shweta", 20)
happy_bday("Anjali", 5)
happy_bday("Sonal", 56)



# another example

def display_invoice(username, amount, due_date):
    print(f"Invoice for {username}:")
    print(f"Amount Due: ₹{amount:.2f}")
    print(f"Due Date: {due_date}")

display_invoice("Aahan", 3421.53134, "30th June 2026")

# return statement:

def add(x, y):
    z = x + y
    return z

def sub(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

def modulus(x, y):
    z = x % y
    return z

print(sub(1, 2)) # it basically assign this the 1 and 2 to x and y and retuns the value of z
print(add(1, 2))
print(multiply(1, 2))
print(divide(1, 2))

# another example:


def name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = name("aahan", "gupta")
print(full_name)

