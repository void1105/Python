# CONCESSION STAND PROGRAM

menu = {"pizza" : 300, "popcorn" : 150, "coke" : 50, "ice-cream" : 100, "fries" : 90, "chips" : 80, "burger" : 200, "water" : 20}


cart = []

total = 0

items = menu.items()
print("--------- MENU ---------")
for key, values in items:
    print(f"{key:10} : ₹{values:.2f}")

print("------------------------")

while True:
    item = input("What food item would you like to buy?(q to quit): ").lower()
    if item == "q":
        break
    elif item in menu:
        cart.append(item)
        
        
    else:
        print("Item not found in menu. Please choose another item.")
# or :

# while True:
#     item = input("What food item would you like to buy?(q to quit): ").lower()
#     if item == "q":
#         break
#     elif menu.get(item) is not None:
#         cart.append(item)

for food in cart:
    total += menu.get(food)
    print(food, end = ", ")

print()
print(f"Your total bill is: ₹{total:.2f}")