summans = input().split('+')
summans.sort()
number_of_summans = len(summans)
operand = '+'
summans_operand = operand.join(summans)
print(summans_operand)

