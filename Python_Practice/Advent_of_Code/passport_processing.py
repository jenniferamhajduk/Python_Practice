import re
file = open("day3input.txt", "r")
credentials = file.read().replace('\n\n', ',').replace('\n', ' ')
credentials_list = credentials.split(',')
credentials_needing_validation = []

credentials_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_passports = 0
for credential in credentials_list:
    if all(elem in credential for elem in credentials_fields):
        valid_passports += 1
        credentials_needing_validation.append(credential)
print(valid_passports)
# print(credentials_needing_validation[0].split())
# formatted_credential = credentials_needing_validation[0].split()
# print(len(formatted_credential))

validated_credentials = 0
for credential_needing_validation in credentials_needing_validation:
    category_count = 0
    formatted_credential = credential_needing_validation.split()
    print(formatted_credential)
    print("Checking {0}".format(formatted_credential[category_count]))
    while category_count < len(formatted_credential):
        if formatted_credential[category_count][0:4] == 'byr':
            result_1 = int(formatted_credential[category_count][4:]) in range(1920, 2002)
        elif formatted_credential[category_count][0:4] == 'iyr':
            result_2 = int(formatted_credential[category_count][4:]) in range(2010, 2020)
        elif formatted_credential[category_count][0:4] == 'eyr':
            result_3 = int(formatted_credential[category_count][4:]) in range(2020, 2030)
        elif formatted_credential[category_count][0:4] == 'hgt':
            if formatted_credential[category_count][-1:-3] == 'in':
                result_4 = int(formatted_credential[category_count][0:3]) in range(59, 193)
            elif formatted_credential[category_count][-1:-3] == 'cm':
                result_4 = int(formatted_credential[category_count][0:3] in range(150, 193))
        # elif formatted_credential[category_count][0:4] == 'hcl':
        #     if formatted_credential[category_count][0] == '#' and int(formatted_credential[category_count][1:4]) in range(000, 999) and formatted_credential[category_count][4:]:
        #         result_5 = True
        #     else:
        #         result_5 = False 
        elif formatted_credential[category_count][0:4] == 'ecl':
            result_6 = formatted_credential[category_count][4:] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        elif formatted_credential[category_count][0:4] == 'pid':
            result_7 = int(formatted_credential[category_count][4:]) in range(000000000, 999999999)
        category_count += 1
        # if result_1 and result_2  and result_3  and result_4  and result_5  and result_6  and result_7:
        #     validated_credentials += 1
print(validated_credentials)