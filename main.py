#Originally Created on 2/12/2025
## Created as Minesweeper 
### DO NOT COPY THIS PROJECT WITHOUT CREDITS TO BROCLLY

import time
import generate
import os

selection = 0
build_ver = "1.1"

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
        print("2. How to Play")
        print("3. Quit.")
        selection = int(input("Pick an operation (enter the digit before)"))
        try:
            if selection < 3 or selection > 0:
                if selection == 1:
                    gameplay()
                    return 0
                elif selection == 2:
                    os.system('cls')
                    game_info()
                elif selection == 3:
                    print("See you soon!")
                    time.sleep(1.5)
                    quit()
            else:
                print("That selection value is not an option!")
        except TypeError: # be careful, highly volatile
            print("That is not a valid option, please try again!")
            time.sleep(1.5)
            os.system('cls')

        
def game_info():
    print("Minesweeper works in a way where you guess spots that are safe, in order to find every possible safe spot.")
    print("This specfic version uses 10 plots, starting at 0, and ending at 9. If a bomb is next to the spot you guessed \n it will be represented by the number of bombs adjacent.")
    print("These are the basic rules of minesweeper!")
    time.sleep(3)
    temp = input("Ready to be sent back to the main menu? (y/n)")
    if temp == "y":
        os.system('cls')
        start_menu()
    else:
        print("Alright then!")
        time.sleep(4)
        os.system('cls')
        game_info()
def gameplay(): # gameplay loop
    generate.generate_small() # generates minefield

    while True:
        os.system('cls')
        generate.UI_elements("n") 
        try: # error
            selection = int(input("Select a plot number (0-9): "))
            status = generate.sweeper_check(selection)
            generate.field_update(selection,status)
        except: # handling.
            print("This is not a valid plot! Enter only numbers between 1 and 10 (inclusive)")
            time.sleep(3)
        os.system('cls')
        generate.UI_elements("n")
        generate.EOR_check()
        time.sleep(1)





welcome()
start_menu()