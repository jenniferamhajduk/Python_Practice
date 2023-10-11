# empty_list = []
# even = [2,4,6,8]
# odd = [1,3,5,7,9]

# numbers = even + odd
# # print(numbers)

# # sorted_numbers = sorted(numbers)
# # print(sorted_numbers)

# # digits = sorted("3836429")
# # print(digits)


# #more_numbers = numbers.copy()
# #even_more_numbers = numbers[:]

# #print(more_numbers)
# #print(even_more_numbers)

# #numbers[3] = 10
# #print(numbers[3:])




# # even.extend(odd)
# # print(even)

# # another_even = even
# # print(another_even)
# # even.sort()
# # print(even)

# # even.sort(reverse=True)
# # print(even)
# # print(another_even)

# # pangram = "The big brown fox jumps over the lazy dog"
# # letter = sorted(pangram)
# # print(letter)

# # numbers = [2.3, 4.5, 8.7, 1.6]
# # sorted_numbers = sorted(numbers)
# # print(sorted_numbers)

# # missing_letter = sorted("The quick brown fox jumped ove the lazy dog", key=str.casefold)
# # print(missing_letter)

# # names = ["Graham", "john", "Terry"]
# # names.sort(key=str.casefold)
# # print(names)

data = [4, 5, 104, 105, 110, 130, 130, 150, 160, 170, 183, 187, 188, 191, 350, 360]
#del data[0:2]
print(data)
min_valid = 100
max_valid = 200
#Careful as indexes will change as you change the size of the list
# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
#Remove data from a list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print(stop)
del data[:stop]
print(data)

start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        start = index + 1
        break
print(start)
del data[start:]
print(data)



