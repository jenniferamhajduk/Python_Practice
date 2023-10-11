declaration = 'Norwegian Blue'
#Return Blue
print(declaration[10:])

#Slicing with negative numbers
print(declaration[-4:-2]) #Bl
print(declaration[-4:12]) #Bl

#Using a step in a slice - Beginning, up to but not including, steps of
print(declaration[0:6:2])
print(declaration[0:6:3])

number = '3,593,293,675,471,304'
print(number[1::4]) #starts with comma, no end, every fourth

#Reverse slicing
letters = 'abcdefghijklmnopqrstuvwxyz'
backwards = letters[25::-1]
backwards = letters[::-1] #Python Idiom
print(backwards)

#Challenge
qpo = letters[16:13:-1]
print(qpo)
edcba = letters[4::-1]
print(edcba)
last_8_in_reverse = letters[25:-9:-1]
print(last_8_in_reverse)

#Idioms
#return last 4 items
print(letters[-4:])
#return last item
print(letters[-1:])
#return first character
print(letters[:1])
#return at index position zero
print(letters[0])
