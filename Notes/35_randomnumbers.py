import random

# we can use help and dir functions to check all methods

# to generate a random integer in a given range:

number_int = random.randint(1, 6)
print(number_int)

# can use variables too as long as the values are integers:

x = 504967

number_int_var = random.randint(1, x)
print(number_int_var)

if number_int_var < 100:
    print("GOAT")

# to generate a random flaot number between 0 and 1:

number_float = random.random()
print(number_float)

# to generate a random float number in a given range:
number_float_range = random.uniform(1, 5)
print(number_float_range)


# to generate a random choice from a list, set, tuple or dictionary:

options = ("rock", "paper", "scissors")

option = random.choice(options)
print(option)

# to shuffle a list randomly:

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)