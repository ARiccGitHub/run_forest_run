"""
                               Midterm Project: Dance and Run Forest! 
            
        
    Alex Ricciardi
    Professor: Dr. Beatty
    COSC 2409.500, Laramie County Community College
    03/10/2022

    Assignment: Midterm Project  
    Due on March 13th, 2022, at 11:59 PM

        - Create, and save, a file in the .py format - 10 pts
        - Import the import os at the top of your code - 10 pts
        - Create three str vars - 2 pts
        - Create three int vars - 2 pts
        - Create one Bool var - 2 pts
        - Create at least one line with a display of a str or int var - 4 pts
        - Create one IF condition and have said condition display via a print() - 15 pts
        - Create one non-endless While loop and have said condition of the loop display via a print() - 15 pts

    Last semester I coded in java a small animation called Run, Forest Run!
    and earlier this semester I created, in python, a similar animation called Dance, Forest Dance!
    For this assignment I created a similar animation merging the previous one call:
    
                                                Run Forest, Run! Mix 
		                             Based on the Forest Gump movie.

   Create a small animation, using keyboard characters,
   of Forest Gump dancing and running on the console screen. With sound effects.



run_forest_run.wav file:
https://www.myinstants.com/instant/run-forest-run/

dance_music.wav file: Melodic Techno #03 Extended Version - Moogify by Zen Man
https://pixabay.com/music/techno-trance-background-loop-melodic-techno-03-2691/

"""

# Libraries
import os
import winsound
import sys
import time
import pygame

# --- String vars ---

# Run Body Frame-1
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
         *                       Run Forest, Run! Mix                   *
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

counter = 0
counter_start = 3
counter_cls = 0

# --- Bool var ---

dance = True

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
        print(dance_body_1)
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


        
                    
# ---- Start

banner()

# Using pygame to run music in background
# This allows synchronously to also play another sound with wind.playsound
pygame.mixer.init()
pygame.mixer.music.load("dance_music.wav")
pygame.mixer.music.play()


# Displays countdown 
while counter_start > 0:
    print(" " * 40 + str(counter_start))
    time.sleep(1)
    counter_start -=1

# --- Animation

while counter < 3:
 
    if counter == 1 or counter == 2:
        run_forest()
             
    dance_forest()
    
    counter += 1
    
    



