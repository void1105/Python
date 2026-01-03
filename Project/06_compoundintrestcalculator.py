principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter the principal amopunt :"))
    if principal < 0:
        print("Principal amount cant be less than 0.")
    else:
        break

while True:
    rate = float(input("Enter the intrest rate :"))
    if rate < 0:
        print("Intrest rate cant be less than 0.")
    else:
        break

while True:
    time = int(input("Enter the time in years:"))
    if time < 0:
        print("Time cant be less than 0.")
    else:
        break

total = principal * pow((1 + rate / 100), time)
print(total)
