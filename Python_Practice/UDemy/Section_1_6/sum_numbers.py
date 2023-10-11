def sum_numbers(*nums: float) -> float:
    """
    This functions returns the sum of all numerical arguments passed into it
    :param nums(float(s)): The numerical argument(s) that will be summed
    :return sum (float): The sum of the numerical arguments
    """
    sum = 0
    for i in nums:
        sum += i
    return sum

print(sum_numbers(1,2,3,4,45))