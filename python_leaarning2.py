# Dictionary

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))

# print(capitals.get("USA"))
# print(capitals.get("Japan"))

capitals.update({"Germany": "Berlin"})
# for capital in capitals:
#     print(capital)

# keys = capitals.keys()
#
# for key in capitals.keys():
#     print(key)
#
# values = capitals.values()
#
# for value in capitals.values():
#     print(value)

for key, value in capitals.items():
    print(f"{key}: {value}")