#===============================================================================
# Sean Corrigan 2017
# ICS 3U1
# Temp Checker
#===============================================================================

# import libraries
import os  # Needed for clearing the terminal in a clear manner
import time # Needed to sleep the system
#########
os.system("clear")
#########
def ask():
    os.system("clear")
    question = input("Enter a Command: ")
    question = question.lower()
    
    if "time" in question:
        os.system("clear")
        print("The time is:")
        os.system("date \"+%H:%M\"")
        time.sleep(3)
        ask()
    if 'date' in question:
        os.system("clear")
        print("The date is:")
        os.system("date \"+%d/%m/%y\"")
        time.sleep(3)
        ask()
    if 'game' in question:
        os.system("clear")
        print("You wanna play a game!")
        time.sleep(3)        
        ask()
    if 'old' in question:
        os.system("clear")
        print("Who\'s asking?")
        time.sleep(3)        
        print("Yeah its a solid like 24 hours")
        time.sleep(3)
        ask()

    print("I cannot find an answer to your question")
ask()
    
