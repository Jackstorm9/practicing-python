number1 = int(input("number1: "))
number2 = int(input("number2: ")) 
user_choice = input("what mathematical equation do you wanna prefrom (Addition, Subtraction, Multplication, Exponentiation): ")

cap_user_choice = user_choice.capitalize()

if cap_user_choice == "Addition":
    print(f"Addition {number1 + number2}")
elif cap_user_choice == "Subtraction":
    print(f"Subtraction {number1 - number2}")
elif cap_user_choice == "Multplication":
    print(f"Multplication {number1 * number2}")
elif cap_user_choice == "Exponentiation":
    print(f"Exponentiation {number1 ** number2}")
else:
    print("ivaild equation")