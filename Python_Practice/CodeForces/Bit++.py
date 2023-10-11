number_of_operations = input()
x = 0
for operations in range(int(number_of_operations)):
    operation = input()
    if '++' in operation:
        x += 1
    else:
        x -= 1
print(x)
