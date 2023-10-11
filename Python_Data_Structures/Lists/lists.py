integers = [1,2,3,4]
stringList = ['Milk', 'Cheese', 'Butter']
#print(integers)
#print(stringList)
mixList = [1,1.5,'sample']
#print(mixList)

#nested list
nestedList = [1,2,3,5,[1,5,1.4], ['test']]
#print(nestedList)

#Accessing/Traversing a list
#same for accessing array
shopingList = ['Milk', 'Cheese', 'Butter']
#print(shopingList[0])
#print('Milk' in shopingList)

for i in range(len(shopingList)):
    shopingList[i] = shopingList[i]+'+'
    #print(shopingList[i])

myList = [1,2,3,4,5,6,7]
myListTwo = [8,9,10,11,12]

#print(myList)
#myList[2] = 33
#print(myList)

# myList.insert(0, 11)
# print(myList)
# myList.append(33)
# print(myList)
# myList.extend(myListTwo)
# print(myList)

numbers = []
while (True):
    entry = input("Enter a number: ")
    if entry == "done":
        break
    else:
        numbers.append(float(entry))
        average = sum(numbers)/len(numbers)
print("The average is: ", average)





