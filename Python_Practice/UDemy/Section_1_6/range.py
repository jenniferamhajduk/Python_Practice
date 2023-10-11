# for i in range(1, 21):
#     print("i is now {}".format(i))

#Start value default to 0 if not specified

for i in range(0, 10, 2):
    print("i is now {}".format(i))

print('*' * 20)

for i in range(10, 0, -2):
    print("i is now {}".format(i))

print('*' * 20)

for i in range(0, 101, 7):
    print(i)

print('*' * 20 + " Nested For Loops " + "*" * 20)

for i in range(1, 13):
    for j in range(1, 13):
        print("{0} times {1} is {2}".format(j, i , i * j))
    print("-" * 20)

print('*' * 20 + " More Loops " + "*" * 20)

shopping_list = ["milk", "pasta", "eggs", "bread", "rice", "bubble water"]
# for item in shopping_list:
#     if item != "bubble water":
#         print("Buy " + item)

# for item in shopping_list:
#     if item == "bubble water":
#         continue
#     print("Buy " + item)

# for item in shopping_list:
#     if item == "eggs":
#         break
#     print("Buy " + item)

items_to_find = "eggs" #albatross
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == items_to_find:
#         found_at = index
#         break

if items_to_find in shopping_list:
    found_at = shopping_list.index(items_to_find)
if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(items_to_find))

print("*" * 20)

# for i in range(10):
#     print("i is now {}".format(i))

# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1
    
# available_exits = ["north", "south", "east", "west"]
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit.casefold() == "quit":
#         print("Game over")
#         break
# print("You made it out!!!")









