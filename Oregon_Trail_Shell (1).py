# *********************************************************************************************************************************
#
#                                                       PROJECT 1: OREGON TRAIL
#
# 
#   Author(s)
#       { Angelica Idoko }
#
#   -------------------------------------------
#   Project Description / Specification
#   -------------------------------------------
#   We will be recreating Oregon Trail! The goal is to travel from NYC to Oregon (2000 miles) by Dec 31st.
#   However, the trail is arduous.  Each day costs you food and health.
#   You can hunt and rest, but you have to get there before winter!
#
#       1) The Player starts in NYC on 03/01 with 2,000 miles to go, 500lbs of food, and 5 health.
#       2) The player must get to Oregon by 12/31
#       3) At the beginning of the game, user is asked their name.
#	4) The player's health randomly decreases 2 times during the month.
#	5) The player eats 5lbs of food a day.
#	6) Each turn, the player is asked what action they choose,
#          where the player can type in the following: travel , rest , hunt , status , help , quit 
#	        > travel    :   moves you randomly between 30-60 miles and takes 3-7 days (random). 
#	        > rest      :   increases health 1 level (up to 5 maximum) and takes 2-5 days (random). 
#	        > hunt      :   adds 100 lbs of food and takes 2-5 days (random). 
#	        > status    :   lists food, health, distance traveled, and day. 
#	        > help      :   lists all the commands. 
#	        > quit      :   will end the game.
#
#
#   -------------------------------------------
#   Deliverables
#   -------------------------------------------
#       You must use turn in the file proj01.py (source code solution); 
#       be sure to include your names, the project number and comments describing your code. 
#
#   -------------------------------------------
#   Change Log
#   -------------------------------------------
#       09.19.2018  PO  Initial Programming 
#
# *********************************************************************************************************************************

#-----------------------------------------------------------#
#   GLOBAL VARIABLES                                        #
#-----------------------------------------------------------#  

origString = ""
validChoices = ['T','R','H','S','?','Q']                                        # There are several choices available, checking them individually can create excessive code

#
#   ______ FUNCTION
#       LOGIC -
#           Step 1 - 
#

def function1():
    origString = input("Which option: ")

    while keyFound != "Y" and keyFound != "X":   
        print("the function will do something here")

#-----------------------------------------------------------#
#   MAIN ...                                                #
#-----------------------------------------------------------#  

print("Oregon Trail")
print("  [T]ravel")
print("  [R]est")
print("  [H]unt")
print("  [S]tatus")
print("  [?] for help")
print("  [Q]uit" + "\n")

#global userChoice
userChoice = "X"                                                                    # The value is assigned at this particular spot so the user interface is cleaner looking

#
#   The Player can type in the following:
#       travel , rest , hunt , status , help , quit
#

while userChoice != "Q":                                                            #   The while loop will terminate when the user enters "Q"uit
    userChoice = input("T/R/H/S/?/Q: ")                                                   #   Accept input from user and format it as 
    userChoice = userChoice.upper()                                                 #       UPPER CASE for cleaner handling
     
    if userChoice == "T":                                                           #   User wants to travel
        print("User chose travel, you will do someting here")

    if userChoice == "R":                                                           #   User wants to ___
        print("call the function for rest ...")

    if userChoice == "Q":
        print("Thank you for travelling on the Oregon Trail!")
        
####  SEE NOTE ABOVE -->  if userChoice != "T" and userChoice != "R" and userChoice != "H" and userChoice != "S" and userChoice != "S" and userChoice != "?" and userChoice !="Q":
    if userChoice not in validChoices:
       print("That is an invalid choice" + "\n")
#_______________________________________________________________________________________________________

#///Game will start here!!!!
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def Travel(distanceTravelled,Date,Time,Mileage):
    
#How many days travelled. 
#How long/ what distance you have travelled.
#Displays date...time..etc.
#Where you are.

distanceTravelled = (random.choice(mileage))
mileage = (random.choice(0,10))





