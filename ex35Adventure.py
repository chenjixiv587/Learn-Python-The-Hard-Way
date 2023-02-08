def start():
    print("You get into a door")
    print("Do you want to get into left or right")
    choice = input("> ")
    if choice == "left":
        bearRoom()
    elif choice == "right":
        goldRoom()
    else:
        dead("You should give a right choice")


def bearRoom():
    print("Welcome to the bear room")
    print("You choose give up or get in")
    bearMoved = False
    while True:
        choice = input("> ")
        if choice == "go in" and not bearMoved:
            print("The bear is go")
            bearMoved = True
        elif choice == "go in" and bearMoved:
            dead("U are dead")
        elif choice == "open door" and bearMoved:
            goldRoom()
        else:
            dead("What do you want?")


def goldRoom():
    print("You choose how much")
    choice = input("> ")
    if "0" in choice or "1" in choice:
        if int(choice) > 50:
            dead("U are so greedy")
        else:
            dead("You win!")
    else:
        dead("You lose")


def dead(why):
    print(why, "Good Job!")
    exit(0)


start()
