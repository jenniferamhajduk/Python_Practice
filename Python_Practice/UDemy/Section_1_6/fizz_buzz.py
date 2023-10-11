def fizz_buzz(number: str) -> str:
    """
    This function takes one parameter `number` and determines if it is either divisible by 3, 5, or both. If it is divisible by three, the function returns `fizz`, if it is divisible by 5 it returns `buzz`,
    and if it is divisible by both it returns `fizz buzz`. Otherwise it just returns

    :param number: The next number in the sequence
    :returns: Returns either `fizz`, `buzz`, `fizz buzz`, or the number entered
    """
    integer_number = int(number)
    if integer_number % 5 == 0 and integer_number % 3 == 0:
        return "fizz buzz"
    elif integer_number % 5 == 0:
        return "buzz"
    elif integer_number % 3 == 0:
        return "fizz"
    else:
       return str(number)


# for i in range(1, 101):
#     print(fizz_buzz(i))
i = 1
while i in range(1, 101):
    print("The computer's choice is: {0}".format(i))
    print("The computer's answer is: {0}".format(fizz_buzz(i)))
    i += 1
    players_answer = input("Please input the next item in the sequence: ")
    if int(players_answer) != i:
        print("You have not entered the correct item in the sequence. You have entered {0}. The Game is OVER!".format(players_answer))
        raise ValueError
    elif int(players_answer) == 100:
        print("You have completed the game. WELL DONE!", fizz_buzz(i))
        break
    print("Your choice was {0} and your answer is {1}".format(i, fizz_buzz(i)))
    i += 1