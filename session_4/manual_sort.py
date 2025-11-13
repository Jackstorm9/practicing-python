user_input = input("Please enter a set of numbers separated by spaces: ")
list = user_input.split()
numbers = [int(num) for num in list]

current_bigger_number = 0

for num in range(len(numbers) - 1):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            current_bigger_number = numbers[i]
            numbers[i] = numbers[i + 1]
            numbers[i + 1] = current_bigger_number
print(numbers)  