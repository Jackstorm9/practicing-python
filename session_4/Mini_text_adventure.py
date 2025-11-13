print("You wake up in a dark room: ")
key = False
while True:
    user_input = input("What do you do?\n(look, walk, sleep, open door): ")
    if user_input == "look":
        print("you look out the window. you can't see anything from the darkness")
    elif user_input == "walk":
        print("you step on something in the dark. it's a key!")
        key = True
    elif user_input == "sleep":
        print("a lingering feeling for escape doesn't let you sleep")
    elif user_input == "open door":
        if key == False:
            print("the door seems to be locked")
        else:
            print("The key fits! you escape succesfully.")
            break
    else:
        print("invalid action please try again")