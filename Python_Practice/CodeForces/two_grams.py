num_of_letters = int(input())
letters = list(input())
pairs = []
for i in range(num_of_letters):
    if i + 1 < num_of_letters:
        pairs.append(letters[i] + letters[i + 1])
most_frequent = max(set(pairs), key=pairs.count)
print(most_frequent)
