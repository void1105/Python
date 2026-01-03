import time

# time module:
#           time.sleep(secs)  --> It is used to delay execution for a given number of seconds.
#          time.time()      --> It returns the current time in seconds since the epoch (January 1, 1970).

time.sleep(3)
print("hello")



my_time = int(input("Enter time in seconds for countdown: "))

for x in (range(my_time, -1, -1)):
    seconds = x % 60
    minutes = (x // 60) % 60
    hours = x // 3600
    print(f"{hours}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!")