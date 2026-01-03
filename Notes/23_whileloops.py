# while loops are loops which are executed till the condition is true


name = input("Enter your name: ")

while name == "":
    print("You did not enter your name.")
    name = input("Enter your name: ")
print(f"Hello {name}.")