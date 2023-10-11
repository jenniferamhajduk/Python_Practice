target = 9
pairs = []
list_of_nums = [2,6,3,9,11]
lon  = [num for num in list_of_nums if num <= target]
for i in range(len(lon)):
    for j in range(len(lon)):
        if lon[i] + lon[j] == target:
            pairs_list = []
            pairs_list.append(lon.index(lon[i]))
            pairs_list.append(lon.index(lon[j]))
            if pairs_list not in pairs:
                pairs.append(pairs_list)
            else:
                pass
            pairs_list = []
print(pairs)