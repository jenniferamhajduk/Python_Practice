menu = """Please select an option from the menu: \n1: Red \n2: Blue \n3: Yellow \n4: Orange \n5: Pink \n6: Purple \n7: Fuschia \n8: Navy Blue \n0: Exit"""
print(menu)

option = int(input())
options = [1, 2, 3, 4, 5, 6, 7, 8]
while option != 0:
    if option in options:
        print("You have selected option: {}".format(option))
    elif option == 0:
        break
    else:
        print(menu)
    option = int(input())
        


