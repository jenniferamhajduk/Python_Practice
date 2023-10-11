# ship = "Norwegian Blue"
# for character in ship:
#     print(character)


# number = "9.248:44287,23 84.335967:;442"
# separators = ""

# for char in number:
#     if not char.isnumeric():
#         separators += char
# print(separators)

# values = "".join(char if char not in separators else " " for char in number).split()
# print([int(val) for val in values])



number = input("Please enter a series of numbers, using any separators: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators += char
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
print(sum([int(val) for val in values]))


