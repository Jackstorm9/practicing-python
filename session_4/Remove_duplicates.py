user_input = input("Please enter a list of items seperated by spaces: ")
list = user_input.split()
duplicates_removed = []

for item in list:
    if item not in duplicates_removed:
        duplicates_removed.append(item)
print(duplicates_removed)