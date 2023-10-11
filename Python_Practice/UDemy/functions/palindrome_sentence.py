def is_palindrome(string: str) -> bool:
    backwards = string[::-1]
    return backwards == string #return if the value is equal to original string

word = input("Please enter a word: ")
if is_palindrome(word.casefold()):
    print ("'{}' is a palindrome".format(word))
else:
    print ("'{}' is not a palindrome".format(word))


def is_palindrome_sentence(new_sentence: str) -> bool:
    backwards = new_sentence[::-1]
    return backwards == new_sentence #return if the value is equal to original string

sentence = input("Please enter a sentence: ")
new_sentence = []
for char in sentence:
    if char.isalpha():
        new_sentence.append(char.casefold())
print(new_sentence)
print(new_sentence[::-1])
    

if is_palindrome_sentence(new_sentence):
    print("The sentence is a palindrome")
else:
    print("The sentence is not a palindrome")


