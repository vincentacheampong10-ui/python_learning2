# 2D Collections

fruits = ["apples", "banana", "coconut"]
vegetable = ["celery", "carrots", "potatoes"]
meats = ["chicken","fish","turkey"]

groceries = [fruits, vegetable, meats]

for collection in groceries:
    for food in collection:
      print(food, end= " ")
    print()