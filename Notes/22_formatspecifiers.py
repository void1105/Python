# format specifiers = {value:flags} format a value based on what flags are inserted

#  .(number)f = round to that many decimal places(fixed point)
#  :(number) = allocate to that many spaces
#  :03 = allocate and zero pad that many spaces
#  :< = left justify
#  :> = right justify
#  :^ = center align
#  :+ = use a plus sign to indicate positive numbers
#  := = place the sign to the leftmost position
#  :  = insert a space before positive numbers
#  :, = comma separator for thousands


# basic syntax:

num1 = 5
num2 = -4
num3 = 3

print(f"num1 is {num1:+010,.2f}")
print(f"num2 is {num2:+010,.2f}")
print(f"num3 is {num3:+010,.2f}")


# order of flags: {value : [fill][align][sign][#][0][width][,][.precision][type]}
