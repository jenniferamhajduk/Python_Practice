fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime" : "a sour, green, citrus fruit"
}

# print(fruit)
# print(fruit["lemon"]) #lemon is the key
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# fruit["pear"] = "great with tequila"
# print(fruit)
# del fruit["lemon"]
# print(fruit)
# # fruit.clear()
# # print(fruit)
# # print(fruit["tomato])


# bike = {"make": "Honda",
#         "model": "250 dream",
#         "colour": "red",
#         "engine_size": 250}

# print(bike["engine_size"])
# print(bike["colour"])

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We dont have a: " + dict_key)
#     print(description)
#     # if dict_key in fruit:
#     #     description = fruit.get(dict_key)
#     #     print(description)
#     # else:
#     #     print("we dont have a key: ", dict_key)

# for snack in fruit:
#     print(fruit[snack])

# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#         print('-' * 40)

#_________________________________________

#ordered keys, not necessary in python 3

#Convert to list then sort the list
#_________________________________________
# ordered_key = list(fruit.keys())
# ordered_key.sort()
# ordered_key = sorted(list(fruit.keys()))
# for f in ordered_key:
#     print(f + " - " + fruit[f])

# fruit_keys = fruit.keys()
# print(fruit_keys)

# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)
#_________________________________________


# #Create Tuple from dictionary
#_________________________________________
# print(fruit)
# print(fruit.items())
# f_tuple = tuple(fruit.items())
# print(f_tuple)

# for snack in f_tuple:
#     item, description = snack
#     print(item + " is " + description)
#_________________________________________


# #Create dictionary from tuple
#_________________________________________
# print(dict(f_tuple))
#_________________________________________
