user_input = input("Please enter a list of items seperated by spaces: ")

list = user_input.split()
print(list)

word_to_find = input("enter the item you are searching for: ")
count = list.count(word_to_find)

print(f"The word '{word_to_find}' appears {count} times in the list: ")