numbers = (0, 1, 2, 3, 4, 5)
# print(numbers, sep=";")
# print(*numbers, sep=";") #unpacked values

def test_star(*args):
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)