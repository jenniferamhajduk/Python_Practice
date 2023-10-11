number_of_problems = input()
problem_iteration = 0
outcome = 0
substring1 = "1 0 1"
substring2 = "1 1 0"
substring3 = "0 1 1"
substring4 = "1 1 1"

while problem_iteration < int(number_of_problems):
    vote_round = input()
    if substring1 in vote_round or substring2 in vote_round or substring3 in vote_round or substring4 in vote_round:
        outcome = outcome + 1
    else:
        pass
    
    problem_iteration = problem_iteration + 1

print(outcome)

