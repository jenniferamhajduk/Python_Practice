import numpy as np
num_array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
number = int(input("Enter a number: "))

def find_a_number(array, num):
    if num in array:
        for i in range(len(array)):
            if array[i] == num:
                print(i)
    else:
        print(str(num) + " is not in the array ")

find_a_number(num_array, number)