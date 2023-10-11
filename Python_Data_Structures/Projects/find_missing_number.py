def missingNumber(myList, totalCount):
    expected_sum = (totalCount * (totalCount + 1))/2
    actual_sum = sum(myList)
    missing_number = expected_sum - actual_sum
    return missing_number