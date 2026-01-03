# process of convering 1 data type to another data type is called typecasting in python
name = "Aahan"
age = 13
gpa = 3.8
student = True

# to check the datatpye of a variable, we use the type() function
print(type(gpa))

# to convert a int to a float or a float to an int, we use the int() and float() functions
age = float(age)
print(age)
gpa = int(gpa)
print(gpa)

# to convert a int or a float to a string, we use the str() function
age = str(age)
print(type(age))

# srt to bool
name = bool(name)# if the string is empty, it will be converted to False, otherwise it will be True
print(name)
