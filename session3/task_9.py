name = input("whats your name?: ")
greeting = input("what kind of greeting do you want? (formal,casual): ")

if greeting == "formal":
    print(f"Good day to you,{name}. I hope you are well.")
elif greeting == "casual":
    print(f"Hey {name},what's up?")