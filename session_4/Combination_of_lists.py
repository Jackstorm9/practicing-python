# at first i did it with the + method creating a seperate list with the combination
# then i searched to find a more effective method

user_input = input("Please enter a list of items seperated by spaces: ")
list = user_input.split()

user_input2 = input("Please enter a second list of items seperated by spaces: ")
list2 = user_input2.split()

list.extend(list2)

print(list)