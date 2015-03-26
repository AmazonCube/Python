# imports for the file
from math import *
import random


# variables for the battle functions
# health variables
health = 500
game_over = 0


# attacks for player
mele = 25
magic = 75
block = 50
heal = 100


# this is the function for the first battle level
def first_battle():

    # main prompt for the introduction
    print ("""This is the introduction to the main battle phase.
    You have 500 health points once you hit 0 you will
    recieve a message saying Game Over. If the computers
    health hits 0 you will move on to the next level.""")
    print ()
    print ("""You may choose from one of four attacks and the
    computer will respond. To attack type in your choice
    as shown. ex: block""")


    # the function that allows you to start the game after pressing enter
    def press_start():
        print()
        print (input ("Press enter to start:"))


        #this is the main function for the battle phase
        def main_battle():


            # this is the user prompt that gives an overview of your action choices
            def user_prompt():
                print ("""You may begin your turn choose your attack
                be for you can continue.""")
                print()
                print("""You may choose any one of the following.
                >>> mele - 25 Hit Points
                >>> magic - 75 Hit Points
                >>> block - Protects up to 50 hit points. Any attack stronger then 50 results in player damage.
                >>> heal - Heal up to 100 life points.
                >>> help - Any time you need to look at the attacks type ex: help""")


                # this function defines the help command for the game showing the intro prompt and attacks.
            user_prompt()

        main_battle()

    press_start()

first_battle()
