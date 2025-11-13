import random

word = input("Please enter a word: ")
letters = []
temp = []

for i in word:
    letters.append(i)

while letters:
    random_slice = random.randint(0,len(letters) - 1)
    temp.append(letters[random_slice])
    letters.pop(random_slice)

scrambled_word = "".join(temp)
print(scrambled_word)