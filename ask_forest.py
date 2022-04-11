"""
                               User Inputs, Adding, and Subtracting 
            
        
    Alex Ricciardi
    Professor: Dr. Beatty
    COSC 2409.500, Laramie County Community College
    04/10/2022

    Assignment: Midterm Project  
    Due on April 10th, 2022, at 11:59 PM

        - Create, and save, a file in the .py format - 10 pts
        - Import the import os at the top of your code - 10 pts
        - Create three str vars - 2 pts
        - Create three int vars - 2 pts
        - Create one Bool var - 2 pts
        - Create at least one line with a display of a str or int var - 4 pts
        - Create one IF condition and have said condition display via a print() - 15 pts
        - Create one non-endless While loop and have said condition of the loop display via a print() - 15 pts
        - At least one print statement that will derive from user input - 10 pts
        - One syntax with int vars being added and another with the in vars being subtracted - 10 pts

"""
# Libraries
import os # Import the import os at the top of your code - 10 pts
import winsound
import sys
import time
import pygame

# --- String vars ---

# Run Body Frame-1 Create three str vars - 2 pts
run_body1_head = " O"
run_body1_arms = "/||"
run_body1_legs = "/|"
		
# Run Body Frame-2
run_body2_head = " O"
run_body2_arms = "/|\\"
run_body2_legs = "/\\"
		
# Run Body Frame-3
run_body3_head = " O"
run_body3_arms = "||\\"
run_body3_legs = " |\\"
		
banner_txt = """


         ****************************************************************
         *                                                              *
         *                       Run Forest, Run!                       *
         *                                                              *
         ****************************************************************         """

# Dance Body		
dance_body_1 = """       Dance Forest, Dance!  
                                         O
                                        /||
                                        /|
"""

dance_body_2 = """       Dance Forest, Dance!  
                                         O
                                        ||\\
                                         |\\
""" 

# --- Integer vars ---

counter = 0 # Create three int vars - 2 pts
counter_start = 3
counter_cls = 0

# --- Bool var ---

dance_bool = True # Create one Bool var - 2 pts

# --- Functions ---

def banner():

    # Clear screen
    # It is for MacOS and Linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # It is for Windows platfrom
        _ = os.system('cls')

    print(banner_txt)
    print("\n" * 2)

def dance_forest():
    
    for i in range(8):
        banner()
        print(dance_body_1) # Create at least one line with a display of a str or int var - 4 pts
        time.sleep(.3)
        
        banner()
        print(dance_body_2)
        time.sleep(.3)
        
def run_animation(run_d, body_h, body_a, body_l):
    banner()
    print(run_d + body_h)
    print(run_d + body_a)
    print(run_d + body_l)
    time.sleep(.3)

    return run_d

def counter():
    # Displays countdown 
    while counter_start > 0: # Create one non-endless While loop and have said condition of the loop display via a print() - 15 pts
        print(" " * 40 + str(counter_start))
        time.sleep(1)
        counter_start -= 1 # One syntax with int vars being added and another with the in vars being subtracted - 10 
        couter += 1  # to get credit for int vars being added and another with the in vars being subtracted - 10  
        
def run_forest():
    
    # Distance ran 
    run_dis = "    "
    
    winsound.PlaySound("run_forest_run.wav", winsound.SND_ASYNC)

    # Running Animation
    for i in range(6):

        if i == 3 : winsound.PlaySound("run_forest_run.wav", winsound.SND_ASYNC) 
        
        run_dis = run_animation(run_dis,            
                                run_body1_head,
                                run_body1_arms,
                                run_body1_legs) + "    "
        run_dis = run_animation(run_dis,
                                run_body2_head,
                                run_body2_arms,
                                run_body2_legs) + "    "
        run_dis = run_animation(run_dis,
                                run_body3_head,
                                run_body3_arms,
                                run_body3_legs) + "    "

# Asking to see Forest run
def input_run():
    
    banner()

    while True:
        in_run = input(" Do you want to see Forest Gump run? Type yes or no: ").lower()
        if in_run != "yes" and in_run != "no":
            print("\nI do not undestand? Wrong input entered, maybe?\n")
        else:
            break
                    
    if in_run == "yes":
        
        run_forest()
        # Asking again to see Forest run?
        while True:

            again_run = input(" Do you want to see Forest Gump run Again? Type yes or no: ").lower()


            if again_run != "yes" and again_run != "no": # Create one IF condition and have said condition display via a print() - 15 pts
                print("\nI do not undestand? Wrong input entered, maybe?\n")
            elif again_run == "yes":
                run_forest()
            elif again_run == "no":
                break

# Asking to see Forest dance   
def input_dance():
    
    banner()

    # Asking to see Forest dance
    while True:
        in_dance = input(" Do you want to see Forest Gump dance? Type yes or no: ").lower()
        if in_dance != "yes" and in_dance != "no":
            print("\n I do not undestand? Wrong input entered, maybe?\n")
        else:
            break
                    
    if in_dance == "yes":
        
        dance_forest()
        # Asking again to see Forest dance?
        while True:

            again_dance = input(" Do you want to see Forest Gump dance Again? Type yes or no: ").lower()


            if again_dance != "yes" and again_dance != "no":
                print("\n I do not undestand? Wrong input entered, maybe?\n")
            elif again_dance == "yes": 
                dance_forest()
            elif again_dance == "no":
                break
        
                    
# ---- Start

banner()

# Using pygame to run music in background
# This allows synchronously to also play another sound with wind.playsound
pygame.mixer.init()
pygame.mixer.music.load("dance_music.wav")
pygame.mixer.music.play(loops = -1)  


banner()

print("""
                    Hello there welcome to the Forest Gump Similation!

   In this simulation, you will ask Forest Gump to run and dance, for your enjoyment...

""")

name = input("   What is your first name? ")
if type(name) != type("a string"):
    name = str(name)


bully = input("\n   Can I call you " + name + " Gump? type yes or no: ") # At least one print statement that will derive from user input - 10 pts
bully_name = name + " Gump" 

if bully != "yes":
    print("\n   Whatever! I will call you " + bully_name + " anyway!")
else:
    print("\n   Ok so " + bully_name + " it is!")
          
input("\n Press enter to continue")

input_run()      
        
input_dance()

banner()

print("\n Thank you for using the Forest Gump simulation, " + name + "!")
time.sleep(2)
print("\n Sorry, that was a slip of the tongue, I mean " + bully_name + "!")
input("\n Press enter to end")





