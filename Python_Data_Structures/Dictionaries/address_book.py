myDict = {'name': 'Jennifer', 'age': 32, 'address': 'Portland'}
def traverseDict(dict):
    for key in dict:
        print(key, myDict[key])
traverseDict(myDict)

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'The value does not exist'
print(searchDict(myDict, 32))

myDict.pop('name')
print(myDict)