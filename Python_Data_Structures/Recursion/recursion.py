def recursive_method(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursive_method(n-1)
        print(n)

print(recursive_method(10))