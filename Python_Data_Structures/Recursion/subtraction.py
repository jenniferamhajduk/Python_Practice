def subtraction(num):
    assert num >= 0 and int(num) == num, 'The number must be an interger and more than zero'
    if num == 0:
        return num
    else:
        print(num)
        return subtraction(num-1)
print(subtraction(20))