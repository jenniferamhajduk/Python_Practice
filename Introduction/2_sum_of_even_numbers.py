#Calculate the sum of all even numbers from 0 to n, inclusive
#Thinking about the problem...
#0 + 2 = 2
#2 + 2 = 4
#2 + 4 = 6
#4 + 4 = 8
#4 + 6 = 10
#6 + 6 = 12
#6 + 8 = 14
#8 + 8 = 16
stopping_number = input("Enter an even number:")
print("You entered: " + stopping_number)
stopping_number = int(stopping_number)

assert stopping_number % 2 == 0

total = 0
for i in range(0, stopping_number, 2):
    total += i
total += stopping_number
print("The sum is: {0}".format(total))


#Exercise: Do the same, but for the sum of negative numbers