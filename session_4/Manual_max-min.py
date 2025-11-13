user_input = input("Please enter a set of numbers separated by spaces: ")
list = user_input.split()

numbers = [int(num) for num in list]
max_value = numbers[0]
min_value = numbers[0]

for num in numbers[1:]:
    if num > max_value:
        max_value = num


for num in numbers[1:]:
    if num < min_value:
        min_value = num

print(f"The maximum value is: {max_value}")
print(f"The minimum value is: {min_value}")