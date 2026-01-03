# 2D collections


fruits =     ["apple", "orange", "banana", "coconut"]

vegetables = ["celery", "carrots", "potatoes"]

meat =       ["chicken", "fish", "turkey"]


food = [fruits, vegetables, meat]

print(food[1][-1])
# it is like co-ordinates


# instead of declaring a list for a 2d list, we can just do this

["blue", "red", "yellow"]
["boat", "bike", "car"]
["burger", "pizza", "pasta"]


boom = [["blue", "red", "yellow"], ["boat", "bike", "car"], ["burger", "pizza", "pasta"]]
groceries = [["apple", "orange", "banana", "coconut"], ["celery", "carrots", "potatoes"], ["chicken", "fish", "turkey"]]
for collection in groceries:
    for food in collection:
        print(food, end = " ")
    print()
print(boom[1][2])




