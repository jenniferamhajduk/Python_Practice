lottery_numbers = [1,25,12,60,33]
for number in lottery_numbers:
    if number % 8 == 0:
        #reject the list
        print("The numbers are unacceptable")
        break
    else:
        print("All those numbers are fine")