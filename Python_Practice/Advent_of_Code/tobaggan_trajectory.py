file = open("day2input.txt", "r")
lines = file.readlines()
lines =[line.replace('\n', '') for line in lines]
print(lines)

right_increment = 1
down_increment = 2

position_index = right_increment
tree_count = 0

def tree_counter_function(position_index, right_increment, down_increment, tree_count):
    if down_increment > 1:
        for index, line in enumerate(lines):
            if index > 1 and index % 2 == 0:
                print("I am on line {} and position {}".format(index, position_index))
                if list(line)[position_index] == "#":
                    tree_count += 1
                position_index += right_increment
                if position_index >= len(line):
                    position_index = position_index - len(line)

    else:
        for index, line in enumerate(lines):
            if index > 0:
                print("I am on line {} and position {}".format(index, position_index))
                if list(line)[position_index] == "#":
                    tree_count += 1
                position_index += right_increment
                if position_index >= len(line):
                    position_index = position_index - len(line)
    return tree_count

number_of_trees_hit = tree_counter_function(position_index, right_increment, down_increment, tree_count)
print(number_of_trees_hit)


