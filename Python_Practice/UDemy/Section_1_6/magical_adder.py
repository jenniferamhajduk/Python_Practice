integers = input("Please input three comma separated numbers: ").split(",")
integer_list = [int(integer) for integer in integers]
sum_of_integer_list = integer_list[0] + integer_list[1] - integer_list[2]
print(sum_of_integer_list)
