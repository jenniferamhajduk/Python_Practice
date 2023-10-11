def pairSum(myList, sum):
    pair_list = []
    for i in range(len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] + myList[j] == sum and str(myList[i]) + '+' + str(myList[j]) not in pair_list:
                pair_list.append(str(myList[i]) +"+"+ str(myList[j]))
    return pair_list

print(pairSum([2,4,3,5,6.-2,4,7,8,9], 7))

def pairSum(myList, sum):
    result = []
    for i in range(len(myList)):
        for j in range(i+1,len(myList)):
            if myList[i] + myList[j] == sum:
                result.append(str(myList[i]) +"+"+ str(myList[j]))
    return result