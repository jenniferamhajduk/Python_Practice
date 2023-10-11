newTuple = ('a',)
print(newTuple)
newTuple = 'a', 'b', 'c'
print(newTuple)


for i in range(len(newTuple)):
    print(newTuple[i])

print('a' in newTuple)
print(newTuple.__len__())