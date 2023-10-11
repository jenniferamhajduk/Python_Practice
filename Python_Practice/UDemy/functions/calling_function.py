def multiply(x, y):
    result = x * y
    return result

answer = multiply(10.5, 4) #Must assign output of multiply() to a variable
print(answer)

for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)

