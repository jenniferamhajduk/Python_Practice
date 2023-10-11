n, k = map(int, input().split())
l = list(map(int, input().split()))

total = 0
if all(ll == 0 for ll in l):
    total = 0
elif all(ll == l[0] for ll in l):
    total = n
else:
    for i in l:
        if i > k:
            total += 1
print(total)