import math
ints = input()
numbers = list(map(int, input().split()))
perf_squares = []
for num in numbers:
    if int(math.sqrt(abs(num)) + .5) ** 2 != num:
        perf_squares.append(num)
print(max(perf_squares))

