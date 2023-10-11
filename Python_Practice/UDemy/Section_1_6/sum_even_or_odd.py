def sum_eo(n, t):
    num_list = list(range(0, n))
    new_num_list = []
    print(num_list)
    if t == 'e':
        for num in num_list:
            if num % 2 == 0:
                new_num_list.append(num)
        print(new_num_list)
        return sum(new_num_list)
    elif t == 'o':
        for num in num_list:
            if num % 2 != 0:
                new_num_list.append(num)
        print(new_num_list)
        return sum(new_num_list)
    else:
        return -1
    

answer = sum_eo(10, 'e')
print(answer)
answer_2 = sum_eo(7, 'o')
print(answer_2)
answer_3 = sum_eo(11, 'spam')
print(answer_3)