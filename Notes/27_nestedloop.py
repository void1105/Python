for x in range(3):
    for i in range(1, 10):
        print(i, end = "-")
    print()


# rectangle project

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of colums: "))
symbol = input("Enter symbol to use: ")

for a in range(rows):
    for b in range(columns):
        print(symbol, end = " ")
    print()

