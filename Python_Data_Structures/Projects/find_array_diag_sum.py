#Calculate the sum of the diagonals of given arrays
def sumDiagonal(a):
    sum = 0
    length_of_elements = len(a[0])
    for i in range(length_of_elements):
        sum += a[i][i]
    return sum