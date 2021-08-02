#Adventure Game


# Variables = Options
number = "number"
police = "police"

left_side = "left"
right_side = "right"

yellow_door = "yellow"
red_door = "red"
violet_door = "violet"

running = "running"
crawling = "crawling"

chair = "chair"
window = "window"

ladder = "ladder"
tube = "tube"

# This works when someone types incorrectly
again = "\nPlease enter you answer again."

print()
# Introduction starts here
def introduction():
    print("\nYou wake up in a room, not recognizing where you are."
    " You are laying in a bed and you decide to get up to explore.\n"
    "You see a window covered on the outside and a door that appears to be locked.\n"
    "\nAfter a few minutes, you notice that there's a phone with a piece of paper attached that has a number written down.\n"
    "What do you decide to do? Do you call the written NUMBER or do you call the POLICE?")

    choice = input('\nNUMBER or POLICE? >>> ')
    if choice.lower() == number:
        option_number()
    elif choice.lower() == police:
        option_police()
    else:
        print(again)
        print()
        introduction()
# Introduction ends here.

# Option number starts here
def option_number():
    print()
    print("You call the number written down with a little fear since you don’t understand what is happening.\n"
    "Suddenly the call is cut off, but you listen that the door opens.\n"
    "When you leave the room, you notice there are two paths, the LEFT side and the RIGHT side. "
    "Which one do you decide to take?")   

    choice = input('\nLEFT or RIGHT >>> ')
    if choice.lower() == left_side:
        option_left()
    elif choice.lower() == right_side:
        option_right()
    else:
        print(again)
        print()
        option_number()
# Option number ends here

# Option left starts here
def option_left():
    print()
    print("Apparently, you took the dead-end road. On the wall, there is a phrase written in red that says\n"
    '"You must make better decisions." The red phrase is ... blood.\n'
    "\nThe kidnapper shows up and locks you in the room forever."
    "\nNow there is no way out, you lost.\n")
    play_again()
# Option left ends here

# Option right starts here
def option_right():
    print()
    print("Five minutes passed since you started walking and you come across a sign that says "
    '"Red is not, yellow is not. And then what is it?\n'
    "Next to a YELLOW door, a RED door, and a VIOLET door.\nWhich one do you enter?")

    choice = input('\nYELLOW, RED or VIOLET? >>> ')
    if choice.lower() == yellow_door:
        option_yellow()
    elif choice.lower() == red_door:
        option_red()
    elif choice.lower() == violet_door:
        option_violet()
    else:
        print(again)
        print()
        option_right()
# Option right ends here

# Option yellow starts here
def option_yellow():
    print()
    print("You enter a dark room and the door immediately closed. "
    "You put your hands on the wall until you find the light switch.\nWow! The room is full of bees."
    "\nYou must decide between RUNNING or CRAWLING to the door you see at the end of the room.")

    choice = input('\nRUNNING or CRAWLING? >>> ')
    if choice.lower() == running:
        option_running()
    elif choice.lower() == crawling:
        option_crawling()
    else:
        print(again)
        print()
        option_yellow()
# Option yellow ends here.


# Option running starts here
def option_running():
    print()
    print("The bees sting you all over your body, but you made it to the door. "
    "There's just one problem ... It's closed.\n"
    "\nYou die.\n")
    play_again()
# Option running ends here.

# Option crawling starts here
def option_crawling():
    print()
    print("When you start to crawl on the floor you realize that it is full of something that looks like syrup.\n"
    "It is very sticky and now you cannot move.\n"
    "\nThis was not the right room.\n")
    play_again()
# Option crawling ends here.

# Option red starts here
def option_red():
    print()
    print("You walk into the room and the door immediately closed."
    " There is a CHAIR in the middle of the room illuminated by a red light.\nThere is also a WINDOW that could be open.\n"
    "What do you decide to do?")

    choice = input('\nCHAIR or WINDOW? >>> ')
    if choice.lower() == chair:
        option_chair()
    elif choice.lower() == window:
        option_window()
    else:
        print(again)
        print()
        option_red()
# Option red ends here.

# Option chair starts here
def option_chair():
    print()
    print("You sit in the chair; your hands and feet are caught.\n"
    'A voice in the distance says "You should have read the sign"\n'
    "\nThere is no way out.\n")
    play_again()
# Option chair ends here.

# Option window starts here
def option_window():
    print()
    print("You go to the window because you thought it was open, but this can't be that easy.\n"
    "You put your hand inside the window and it automatically gives you an electric shock that leaves you paralyzed.\n"
    "\nNow there's nothing you can do.\n")
    play_again()
# Option window ends here.

# Option violet starts here
def option_violet():
    print()
    print("You enter a room that has purple walls,\n"
    "a LADDER in the middle of the room that leads to what appears to be an attic, and a TUBE that leads to a floor below."
    "\nWhat object are you going to use? ")

    choice = input('\nLADDER or TUBE? >>> ')
    if choice.lower() == ladder:
        option_ladder()
    elif choice.lower() == tube:
        option_tube()
    else:
        print(again)
        print()
        option_violet()
# Option violet ends here.

# Option ladder starts here
def option_ladder():
    print()
    print("You go to the attic. "
    "When you enter you find a person sitting in front of a monitor that shows cameras in all the rooms that you were in.\n"
    'The person turns around and says "I was waiting for you."\n'
    "\nThe End.\n")
    play_again()
# Option ladder ends here.

# Option tube starts here
def option_tube():
    print()
    print("When you go to the room below you see an open door and you cannot believe that since this torment began you have finally found a way out.\n"
    'You keep wondering, "Was this all I had to do?" And with a little scared, you start running.\n'
    "\nYou escape.\n")
    play_again()
# Option tube ends here.


# Option police starts here.
def option_police():
    print()
    print("When you tried to call the police, the phone cut the call and now it doesn't work. "
    'You just have to wait.\n\nA voice that seems to come from a speaker says "You should have called the number I left" and\n'
    "suddenly you feel a strange smell entering the room. It was a lethal gas.\n"
    "\nYou died, I'm sorry.\n")
    play_again()
# Option police ends here.

def play_again():
    print("Do you want to play again? Y / N ")

    choice = input('\nY / N >>> ')
    if choice.lower() == "y":
        introduction()
    else:
        exit()
    
introduction()      
