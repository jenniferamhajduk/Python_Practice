def is_palindrome(string):
    backwards = string[::-1]
    return backwards == string #return if the value is equal to original string

word = input("Please enter a word: ")
if is_palindrome(word.casefold()):
    print ("'{}' is a palindrome".format(word))
else:
    print ("'{}' is not a palindrome".format(word))
