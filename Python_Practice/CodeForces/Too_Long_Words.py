wordNumber = input()
counter = 0
while (counter < int(wordNumber)):
    word = input()
    if  0 < len(word) <= 10:
        print(word)
        counter = counter + 1
    elif len(word) > 10:
        middle = len(word) - 2
        newword = word[0] + str(middle) + word[-1]
        print(newword)
        counter = counter + 1
