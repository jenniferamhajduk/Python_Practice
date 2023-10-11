def firstSecond(givenList):
    sorted_list = givenList
    sorted_list.sort(reverse=True)
    return sorted_list[0], sorted_list[1]