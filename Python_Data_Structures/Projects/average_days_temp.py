from array import *
high_count = 0
num_days = array("i")
days = input("Enter the number of days for the temp readings: ")
print(type(days))
for i in range(int(days)):
    num = input("Enter the temp for day " + str(i + 1) + " :")
    num_days.append(int(num))
avg_temp = sum(num_days)/len(num_days)
for nd in num_days:
    if nd > avg_temp:
        high_count += 1
    else:
        pass
print("Average: " + str(avg_temp) + "\n" + "Number of days above average: " + str(high_count))