def removeDuplicates(myList):
    removed_duplicates = []
    for i in myList:
        if i not in removed_duplicates:
            removed_duplicates.append(i)
    return removed_duplicates