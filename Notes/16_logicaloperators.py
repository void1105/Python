# LOGICAL OPERATORS : 3 types- 1. or 2. and 3. not
# 1. or operator: returns True if at least one condition is True    
# 2. and operator: returns True only if both conditions are True
# 3. not operator: reverses the result, returns False if the result is True

#OR OPERATOR

temp = 25
is_raining = True

if temp>35 or temp<0 or is_raining:
    print("The outdoor event is cancelled.")
else:
    print("The outdoor event is on!")

# AND OPERATOR

temp = 28
is_sunny = True

if temp >=28 and is_sunny:
    print("it is hot and sunny outside.")
elif temp<=0 and is_sunny:
    print("it is cold and sunny outside.")
elif 28 > temp > 0 and is_sunny:
    print("It is warm and sunny outside.")
elif temp >=28 and not is_sunny:
    print("It is hot but not sunny outside.")
elif temp <=0 and not is_sunny:
    print("It is cold and not sunny outside.")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm but not sunny outside.")

   