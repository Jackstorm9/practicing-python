user_input = input("Please enter a list of numbers seperated by spaces: ")
my_list = user_input.split()
numbers = [int(num) for num in my_list]

steps = int(input("please enter the number which the list should shift by: "))

temp = numbers[:steps]
numbers = numbers[steps:]
numbers.extend(temp)

print(numbers)