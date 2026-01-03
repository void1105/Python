# default arguments = A default value for certain parameter
                      # default is used  when that argument is omitted
                    #   make your function more flexible, reduces number of arguments
                    # 1. positional 2. DEFAULT 3. keyword 4. arbitrary

def net_price(list_price, discount = 0, tax = 0.05):  # if discount and tax are not given, it will take default values 
  return list_price * (1 - discount) * (1 + tax)

print(net_price(500))  # in this case discount and tax will take default values
print(net_price(1000, 0.1)) # in this case tax will take default value
print(net_price(1500, 0.2, 0.12)) # in this case no default values will be taken   


# count up timer:

import time

def count(end, start = 0):
  for x in range(start, end + 1):
    print(x)
    time.sleep(1)
  print("Done!")

count(5)

def count(end, start = 0):
  for x in range(start, end + 1):
    print(x)
    time.sleep(1)
  print("Done!")

count(30, 15)
