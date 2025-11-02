import re 
age = input("how old are you?: ")
age_integers = re.findall(r'\d+', age)

if age_integers:
    age_num = int(age_integers[0])
    print(f"next year, you will be {age_num + 1}")
else:
    print("no numbers detected")