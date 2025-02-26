#Originally Created on 2/12/2025
## Created as Super-Minesweep
### DO NOT COPY THIS PROJECT WITHOUT CREDITS TO BROCLLY

import time
import generate
import player
import os
import colorama

player_data = player.Player()
selection = 0
build_ver = "1.2"


def welcome(): # intro message
    print("~Hello! Welcome to Minesweeper!~")
    print(f"Build ver: {build_ver}\n")
    time.sleep(1.5)
    input("Press enter to start!")

def start_menu(): # basic start CLI
    while True:
        os.system('cls')
        print("Welcome! Pick your selection: ")
        print("1. Play!")
        print("2. How to Play (RECOMMENDED FOR NEW PLAYERS)")
        print("3. Quit.")
        selection = int(input("Pick an operation (enter the digit before)"))
        try:
            if selection < 3 or selection > 0:
                if selection == 1:
                    break
                elif selection == 2:
                    os.system('cls')
                    game_info()
                elif selection == 3:
                    print("See you soon!")
                    time.sleep(1.5)
                    quit()
            else:
                print("That selection value is not an option!")
        except TypeError or ValueError: # be careful, highly volatile
            print("That is not a valid option, please try again!")
            time.sleep(1.5)
            os.system('cls')
    gameplay()
        
def game_info(): # gives general info on how to play and special symbols
    print("Minesweeper works in a way where you guess spots that are safe, in order to find every possible safe spot.")
    print("This specfic version uses 10 plots, starting at 0, and ending at 9. If a bomb is next to the spot you guessed \nit will be represented by the number of bombs adjacent.")
    print("These are the basic rules of minesweeper!")
    print("However, this game uses special symbols, here are a list of them:")
    print("'*' = Bomb")
    print("(any integer) = Bombs adjacent to space")
    print("'/' = Would've been a bomb, but 1st turn immunity prevented it.")
    time.sleep(3)
    temp = input("\n\nReady to be sent back to the main menu? (y/n)")
    if temp == "y":
        os.system('cls')
        start_menu()
    else:
        print("Alright then!")
        time.sleep(4)
        os.system('cls')
        game_info()

def gameplay(): # gameplay loop
    generate.generate() # generates minefield
    while True:
        os.system('cls')
        generate.UI_elements("n") 
        try: # error
            column_select = int(input("Select a column number (0 is top, higher is lower on the grid): "))
            row_select = int(input("Select a plot number (0-9): "))
            selection = column_select, row_select
            status = generate.sweeper_check(*selection,player_data.turn)
            generate.field_update(*selection,status)
            player_data.turn += 1
        except: # handling
            print("This is not a valid location! Please follow the instructions on the inputs!")
            time.sleep(3)
        os.system('cls')
        generate.UI_elements("n")
        generate.EOR_check(player_data.turn)
        time.sleep(1)

welcome()
start_menu()