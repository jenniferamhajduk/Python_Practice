from array import *
arr1 = array('i', [1,2,3,4,5,6])
def searchInArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "The element does not exist in this array"

#print(searchInArray(arr1, 6))
#arr1.remove(1)
#print(arr1)

for i in arr1:
    print(i)
#add array from list
tempList = [20,21,22]
arr1.fromlist(tempList)
print(arr1)


