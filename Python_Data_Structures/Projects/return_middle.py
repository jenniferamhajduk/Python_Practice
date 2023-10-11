#return the middle elememts of an array/list
def middle(lst):
    new_list = [ele for ele in lst if ele != lst[0] and ele != lst[-1]]
    return new_list