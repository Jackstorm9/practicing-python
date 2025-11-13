user_input = input("Please enter a set of numbers separated by spaces: ")
list = user_input.split()

numbers = [int(num) for num in list]

average = sum(numbers) / len(numbers)
print(f"The average is: {average}")
