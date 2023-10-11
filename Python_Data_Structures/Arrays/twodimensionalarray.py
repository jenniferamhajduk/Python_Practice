import numpy as np
twoArray = np.array([[11,12,13], [10,14,11], [35,22,9]])
#print(twoArray)

newTwoArray = np.insert(twoArray, 0, [[1,2,3]], axis=0)
# print(newTwoArray)

newTwoArray = np.append(twoArray, [[1,2,3]], axis=0)
# print(newTwoArray)

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])

#accessElements(twoArray, 2, 2)

def traverseArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

#traverseArray(twoArray)

def searchArray(array, value):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] == value:
                return 'The value is located at index '+ str(i) + " " + str(j)
    return 'The element is not found'

#print(searchArray(twoArray, 14))

print(twoArray)
#delFirstRow = np.delete(twoArray, 0, axis = 0)
delFirstCol = np.delete(twoArray, 0, axis = 1)
#print(delFirstRow)
print(delFirstCol)


