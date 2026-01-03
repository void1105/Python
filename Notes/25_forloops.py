# for loop = a statement that will iterate over items of a collection or sequence
#            (like a string, tuple, list, or range)
# example: 
# the range function = generates a sequence of numbers,
for x in range(1, 101):
    print(x)

# to reverse it:
for i in reversed(range(1, 11)):
    print(i)

# we can also use step in range function


for y in range(1, 11 ,2):
    print(y)

credit_card = "1234-5678-9012-3456"

for z in credit_card:
    print(z)

# using contiue and break statements in for loops

for a in range(1, 21):
    if a == 14:
        continue
    else:
        print(a)

for b in range(1, 21):
    if b == 14:
        break
    else:
        print(b)