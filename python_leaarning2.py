# 2D Numpad

# fruits = ["apples", "banana", "coconut"]
# vegetable = ["celery", "carrots", "potatoes"]
# meats = ["chicken","fish","turkey"]
#
# groceries = [fruits, vegetable, meats]
#
# for collection in groceries:
#     for food in collection:
#       print(food, end= " ")
#     print()

numpad_1 = [1, 2, 3]
numpad_2 = [4, 5, 6]
numpad_3 = [7, 8, 9]
numpad_4 = ["*", "0", "#"]

calculator = [numpad_1, numpad_2, numpad_3, numpad_4]

for num in calculator:
    for row in num:
     print(row,  end=" ")
    print()