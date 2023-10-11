length_of_queue_and_time = input().split()
int_length_of_queue = int(length_of_queue_and_time[0])
int_seconds = int(length_of_queue_and_time[1])
lst = []
queue = str(input())
print(queue)

i = 0
for i in range(0, len(queue)):
    lst.append(queue[i])
    i =+ 1
print(lst)


def swap_positions(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst
t = 1
l = 1
#for t in range(1, int_seconds):
for l in range(1, int_length_of_queue):
    index_of_current_B = lst.index('B')
    print(index_of_current_B)
    index_of_possible_G = index_of_current_B + 1
    print(index_of_possible_G)
    if lst[index_of_possible_G] == 'G':
        swap_positions(lst, index_of_current_B, index_of_possible_G)
    else:
        pass
print(lst)
