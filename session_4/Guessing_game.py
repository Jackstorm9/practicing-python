import random
random_number = random.randint(1,100)

def math_game():
    for i in range(100): 
        user_input = int(input("Please enter a number: "))
        if user_input > random_number:
            print("Number too high!")
        elif user_input < random_number:
            print("Number too low!")
        elif user_input == random_number:
            
            print("You got it right!")
            print(f"Number of atempts {i}")
            break

math_game()