import math


# short-hand arithmetic operations
friends = 0
friends += 1  # friends = friends + 1
print(friends)
# same can be used for addition, subratction, multiplication, division, exponents and modulus
# an example for modulus:
cookies = 10
children = 3
cookies %= children  # cookies = cookies % children
print(cookies)  # prints 1 because 10 divided by 3 leaves a remainder of 1

# example for exponent:
pizza = 2
pizza **= 4
print(pizza)  # prints 16 because 2 to the power of 4 is 16


# BUILT IN MATH FUNCTIONS

x = 3.14
y = -4
z  =10
a = 343.323242

#1. round function:
rouded = round(x)
print(rouded)  

#2. absolute value function:
absolute = abs(y)
print(absolute)

#3. power function:
power = pow(z, 3)
print(power)

# 4. maximum function:
maximum = max(x, y, z)
print(maximum)

# 5. minimum function:
minimum = min(x, y, z)
print(minimum)


# 6. math module functions:
# to print pi:
print(math.pi)

# to print e:  
print(math.e)
# to print square root:
squareroot = math.sqrt(x)
print(squareroot)

# to print ceiling value:(rounds up to nearest largest integer)
ceiling = math.ceil(a)
print(ceiling)
# to print floor value:(rounds down to nearest smallest integer)
floor = math.floor(a)
print(floor)
