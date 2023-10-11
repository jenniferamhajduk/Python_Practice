numbers = "3,494,302,201,393,223,909"
numbers_list = numbers.split(",")
print(numbers_list)

num_list = [int(number) for number in numbers_list]
print(num_list)