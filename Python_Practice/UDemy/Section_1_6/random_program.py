import random

# if guess == answer:
#     print("YAY YOU GOT IT!")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guess correctly")


highest = 10
lowest = 0
answer = random.randint(lowest, highest)

print("Please guess a number between {0} and {1}: ".format(lowest, highest))
guess = int(input())
incorrect_guesses = 0
while guess != answer:
    if guess < answer:
        print("Please guess higher: ")
        incorrect_guesses +=1
        guess = int(input())
    else:
        print("Please guess lower: ")
        incorrect_guesses +=1
        guess = int(input())
print("Number of incorrect guesses is: {}".format(incorrect_guesses))
if guess == answer:
    print("You have guess the answer, {}, correctly!".format(answer))