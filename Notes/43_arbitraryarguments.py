# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments (key-value pair)
#            * unpacking operator
#                    1. positional 2. default 3. keyword 4. ARBITRARY


def add(*args): # you can name args anything but by convention it is named args
    total = 0
    for x in args:
        total += x
    return total

print(add(1, 2, 3, 4.5, 5, 3, 2, 5, 67, 67, 67, 67, 67, 67, 67, 67, 67))

# example for **kwargs:

def address(**kwargs):
    for x, y in kwargs.items():
        print(f"{x} : {y}")

address(street = "123 fake st", 
        city = "New York", 
        state = "NY", 
        zip = "10001")


# exercise with both *args and **kwargs:

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()
    # we can use .get method:
    print(f"{kwargs.get('street')}")
    if "apt" in kwargs:
        print(f"{kwargs.get('apt')} {kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")
    else:
        print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")
shipping_label("Dr.", "Aahan", "Gupta", "IV",
               street = "123 Fake St",
               
               city = "Detroit",
               state = "MI",
               zip = "48221",
               apt = "100")