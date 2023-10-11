number = input()
numlst = []
for i in range(0, len(number)):
    numlst.append(number[i])
    i += 1
    
l = 0
lucky_digit_collector = 0
for l in range(0, len(numlst)):
    if numlst[l] == '4' or numlst[l] == '7':
        lucky_digit_collector += 1
        l += 1
    else:
        l += 1

if lucky_digit_collector == 4 or lucky_digit_collector == 7:
    print("YES")
else:
    print("NO")