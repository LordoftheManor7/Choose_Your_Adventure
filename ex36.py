from sys import exit

first_choice = ['door 1', 'door 2', 'door 3']
choice_rm_1 = ['push the door up', 'search for another way out', 'leave quick']
choice_rm_2 = ['use the plank', 'swing the rope', 'jump for it']
choice_rm_3 = ['fight the ogre', 'tickle the ogre', 'try the other door']

def rm_1():
    print("""
The door opens upward.
As you enter you notice that the room is empty.
You take one more step into the center of the room.
All of the sudden the room starts to shake
and the door begins to quickly shut.
What do you do?\n
""")
    escaped_rm_1 = False

    for choice in choice_rm_1:
        print(f"I choose to: {choice}")

    while True:
        choice = input("> ")

        if choice == "push the door up":
            dead("\nThe door is too heavy for you and crushes you.")
        elif choice == "search for another way out":
            dead("\nThere is no other way out. The door has closed. You are trapped forever.")
        elif choice == "leave quick" and not escaped_rm_1:
            print("""
\nYou make a rush for the door.
Just like Indiana Jones you barely make it through!\n
""")
            escaped_rm_1 = True
            print("Now that you're back at the start do you want to try a different door?\n")
            print("1. Yes")
            print("2. No")
        elif choice == "yes" and escaped_rm_1:
            start()
        else:
            print("I don't understand.")

def rm_1_1():
    print("""
You've been falling now for what feels like a day,
then magically you softly land on the ground of a dark tomb.
You have no way out. Your only hope is to pray for freedom or wish for freedom.\n
Do you wish or do you pray?
""")

    choice = input("> ")

    if "pray" in choice:
        dead("\nPray? Who can hear you down here?")
    elif "wish" in choice:
        print("\nYour wish comes true! Welcome back!")
        start()
    else:
        dead("Not a believer? Enjoy eternity.")

def rm_2():
    print("""
You enter a very large room with a huge cavern seperating you and the door to freedom.
You have three options to get across, but only one is the right choice:\n
* The cavern isn't that large, with a running start you could jump to the other side.
* Or you look up and see a rope hanging from the ceiling, maybe you can swing across?
* Or there's an old wooden plank next to you, you could make a bridge to the other side.
""")
    escaped_rm_2 = False

    for choice in choice_rm_2:
        print(f"I choose to: {choice}")

    while True:
        choice = input("> ")

        if choice == "use the plank" and not escaped_rm_2:
            print("""
You grab the old wooden plank and carefully lean it over the cavern.
To your surprise it extends to the other end.
As you step on the plank you can hear the old wood creak.
You pick up the pace and safely make it to the other side.
""")
            win("\nYou open the door and...")
            escaped_rm_2 = True
        elif choice == "swing the rope":
            print("""
You leap for the rope which immediately snaps!\n
You fall... and fall... and fall... and keep falling...\n
...it seems never ending...
""")
            rm_1_1()
        elif choice == "jump for it":
            print("""
\nYou take a running start and jump... and barely get half way.\n
You fall... and fall... and fall... and keep falling...\n
...it seems never ending...
""")
            rm_1_1()
        else:
            print("You have to decide!\n")

def rm_3():
    print("""
\nGood choice! There is a way to freedom in this room
but you have to deal with the giant ogre standing in front of you first.\n
You see a big stick, you could fight the ogre.\n
You also learned in school that ogre's are very ticklish.\n
You see a third door you could go through and avoid the orge all together!\n
What do you choose?
""")

    for choice in choice_rm_3:
        print(f"I'm going to: {choice}")

    choice = input("> ")

    if choice == "fight the ogre":
        dead("\nThat's a joke right? Fight an ogre? He squashes you like a bug.")
    elif choice == "tickle the ogre":
        win("""
\nYou approach the ogre, fingers stretched out.
He screams and cries with laughter as you tickle him.
Soon the ogre cannot take the tickling anymore and falls asleep.
You open the door behind him.\n
""")
    elif choice == "try the other door":
        dead("""
\nYou open the other door thinking it will lead around the ogre.
But standing in front of you is the ogre's wife.
She grabs your head and squashes it like a bug.\n
""")
    else:
        dead("Too slow. The ogre eats you for dinner.")


def win(why):
    print(why, "You did it! You are out of the castle and free! You win!\n")
    exit(0)

def dead(why):
    print(why, "Game Over!\n")
    exit(0)

def start():
    print("""
You have been trapped in a castle for days.
Before you are three doors that could lead to freedom,
or could mean your doom...
Which one do you take?\n
""")
    pick_door = False

    for choice in first_choice:
        print(f"I choose: {choice}")

    while True:

        choice = input("> ")

        if choice == "door 1":
            rm_1()
            pick_door = True
        elif choice == "door 2":
            rm_2()
            pick_door = True
        elif choice == "door 3":
            rm_3()
            pick_door = True
        else:
            print("Hello? Pick a door!")


start()
