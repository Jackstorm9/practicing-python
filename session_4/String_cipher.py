word = input("Please enter a word: ")
shifted_list = []

for i in word:
    shifted_list.append(chr(ord(i) + 3))

shifted_word = "".join(shifted_list)
print(f"Your shifted word: {shifted_word}")