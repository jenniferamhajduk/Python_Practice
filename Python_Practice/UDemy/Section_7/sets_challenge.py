#Create a program that takes some text and returns a list of
#all the characters in the text that are not vowels, sorted in 
#alphabetical order.
#You can either enter the text from the keyboard or
#initialize a string variable with the string

vowels = frozenset("aeiou")
text = input("Please enter some text: ")
final_set = set(text).difference(vowels)
print(sorted(final_set))

