# python calculator

operation = input("Enter which operation u wanna use(+, -, x, ÷): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == "+":
    result = num1 +num2
    print(f"The sum of {num1} and {num2} is {result}")
elif operation == "-":
    result = num1-num2
    print(f"The difference of {num1} and {num2} is {result}")
elif operation == "x":
    result = num1*num2
    print(f"The product of {num1} and {num2} is {result}")
elif operation == "÷":
    if num2 == 0:
        print("error! division by zero is not defined")
    else:
        reslult = num1/num2
        print(f"The quotient of {num1} and {num2} is {result}")
else:
    print("Invalid operation")
        