#This is going to be the start of my own program
import time
print("Welcome to the mad house!")
time.sleep(2)
print("Tell us your name so that we may record it for our records.") #asks name for input
yourName = input() #Here they enter their name
print("Welcome to the mad house, " + yourName + "!") #Result is printed, yes the exclamation mark was necessary.
time.sleep(2)
print("Are you fully prepared for the horrors you'll see in here?")
time.sleep(2)
print("Well I sure hope so, there is no turning back now.")
time.sleep(2)
print("We currently have, " + str(len(yourName)) + " floors, but you are not allowed to leave your floor.")
time.sleep(2)
print("""You are escorted to your cell down a few twisting and narrow hallways before arriving at an empty cell.
The emptiness you feel is only matched by your uncertainty as you don't understand where you are or how you got here, 
only that you woke up and here you are...one thing is for certain, you aren't here to stay.
""")
time.sleep(5)
print("Do you want to attempt a breakout? (yes or no)") #Here the story takes off with a choice
answerChoiceOne = input()
if answerChoiceOne.lower() == "yes":
    print("A bold choice, if not the right one. Being stuck in here is not something you want, let's rectify it.")
    time.sleep(2)
    print("""You search your cell frantically looking for anything that could aids in your escape and to get around your
    first barrier, the locked cell door. After a few minutes of searching however you find a small hairpin left behind
    your toilet and it doesn't take you long before it's fashioned into a makeshift lockpick.""")
    time.sleep(2)
    print("click...")
    print("click...")
    print("click...CLICK!")
    print("""The lock gives way to you, you take your first steps to freedom. There is a chilly and eerie silence that
    fills the halls of this god forsaken place...it sends shivers up your spine. The only thought that fills your head
    is, the uncertainty of your decision, you pray you didn't just make a mistake.""")
else:
    print("Enjoy your time in the Madhouse! Good luck, you'll need it.")


