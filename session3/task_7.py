import re
fav_food = input("what's your favorite food?: ")

food_in_a_week = input(f"how many times a week do you eat {fav_food}?: ")

if food_in_a_week:
    food_int = re.findall(r"\d+",food_in_a_week)
    food_num = int(food_int[0])
    print(f"you eat {fav_food} {food_num} times a week? that's alot!")
else:
    print("no numbers detected")