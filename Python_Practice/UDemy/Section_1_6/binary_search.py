#Binary search - when you have ordered data, you can split in half repeatedly
low = 1
high = 1000
print("\tPlease think of a number between {} and {}".format(low, high))
input("Press enter to start: ")
guess = 1
guesses = 1
while low != high:
    print("Printing in the range of {} and {}".format(low, high))
    guess = low + (high - low) // 2 #this is the binary chop
    high_low = input("My guess is: {}. Should I guess higher or lower? "
                     "Enter h or l, or c if my guess is correct: "
                     .format(guess).casefold())
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesse(s)!".format(guesses))
        break
    guesses += 1
else:
    print("You thought of the number {}".format(low))
    print("Please enter h, l, or c")
