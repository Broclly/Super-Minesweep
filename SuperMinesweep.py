# Originally Created on 2/12/2025
## Created as Super-Minesweep
### DO NOT COPY THIS PROJECT WITHOUT CREDITS TO BROCLLY

import time
from assets import minefield, player
import os
import math

player_data = minefield.player_data
selection = 0
build_ver = "1.4 (indev)"

def welcome(): # intro message
    print("~Hello! Welcome to Super Minesweeper!~")
    print(f"Build ver: {build_ver}\n")
    time.sleep(0.75)
    input("Press enter to start!")

def start_menu(): # basic start CLI
    while True:
        os.system('cls')
        print("Welcome! Pick your selection: ")
        print("1. Play!")
        print("2. How to Play (RECOMMENDED FOR NEW PLAYERS)")
        print("3. Quit.")
        try:
            selection = int(input("Pick an operation (enter the digit before)"))
            if selection < 3 or selection > 0:
                if selection == 1:
                    break
                elif selection == 2:
                    os.system('cls')
                    game_info()
                elif selection == 3:
                    print("See you soon!")
                    time.sleep(1.25)
                    quit()
            else:
                print("That selection value is not an option!")
        except TypeError or ValueError: # be careful, highly volatile
            print("That is not a valid option, please try again!")
            time.sleep(1.25)
            os.system('cls')
    game_setup()
        
def game_info(): # gives general info on how to play and special symbols
    print("===========")
    print("BASIC RULES:")
    print("===========")
    print("Minesweeper works in a way where you guess spots that are safe, in order to find every possible safe spot.")
    print("This specfic version uses 10 plots per row, starting at 0, and ending at 9. If a bomb is next to the spot you guessed \nit will be represented by the number of bombs adjacent.")
    print("These are the basic rules of minesweeper!\n")
    print("===========")
    print("SPECIAL SYMBOLS:")
    print("===========")
    print("In order to represent a minefield in a terminal, some different types of symbols (often found on your keyboard) are used.")
    print("Here are a list of them:")
    print("'*' = Bomb")
    print("(any integer) = Bombs adjacent to space")
    print("'/' = Would've been a bomb, but 1st turn immunity prevented it.")
    print("'+' = Flagged plot\n")
    print("===========")
    print("TALISMANS & ITEMS")
    print("===========")
    print("During certain waves, a shop will appear with various items. Buying these items will require 'coins' which can be obtain \nvia finishing waves, with higher waves rewarding more coins.")
    print("These talismans will give you powers, but be warned, only one can be equipped at a time, so buying another will replace \nyour current talisman!")
    print("As well, consumable power ups can be found in the shop too! Their effects vary per item, but can be used anytime during the main game!\n")
    time.sleep(3)
    temp = input("\n\nReady to be sent back to the main menu? (y/n)")
    if temp == "y":
        os.system('cls')
        start_menu()
    else:
        print("Alright then!")
        time.sleep(1.75)
        os.system('cls')
        game_info()

def game_setup(): # initalizes player values
    os.system('cls')
    print("Let's get started with the game setup for Super Minesweeper!")
    time.sleep(0.5)
    print("What is your name?")
    player_data.name = str(input("Enter name here: "))
    os.system('cls')
    while True:
        print("Pick a class: ")
        print("1. Tank: Reduces damage taken from bombs (Difficulty: Beginner)")
        print("2. Healer: Start at half health, and work your way up by sweeping mines (Difficulty: Advanced)")
        print("3. Soldier: Start with an increased amount of health, and flip a coin to stay alive on lethal hits (Difficulty: Moderate)")
        try: 
            class_select = int(input("Which class would you like to be? (#): "))
        except:
            print("That is not a number!")
        else:
            try: 
                init_health, class_id, class_abilities = player_data.attr_fetch(class_select) # fetches data about class
                player_data.health =  init_health# initalizes health values
                player_data.player_class = class_id # initalizes id
                player_data.abilities.append(class_abilities) # adds abilities
            except TypeError:
                print("That is not a valid selection, try again!")
                time.sleep(0.75)
                os.system('cls')
            gameplay()

def gameplay(): # gameplay loop
    minefield.generate() # generates minefield
    while player_data.health > 0:
        os.system('cls')
        minefield.UI_elements("debug") 
        print("1. Sweep plot")
        print("2. Flag plot")
        print("3. Open inventory")
        print(f"{player_data.points_multi}")
        try: # err
            action = int(input("Select an action (enter #): "))
            if action != 3:
                row_select = int(input("Select a row number (0 is top, higher is lower on the grid): "))
                column_select = int(input("Select a column number (0-9): "))
                selection = row_select, column_select
                if action == 1:
                    status = minefield.sweeper_check(*selection,player_data.turn)
                else:
                    status = "F"
                minefield.field_update(*selection,status)
                player_data.turn += 1
            elif action == 3:
                if len(player_data.inventory) > 0:
                    os.system('cls')
                    iterator = 0
                    for i in player_data.inventory:
                        print(f"Item #{iterator + 1}: {player_data.inventory[iterator][0]}")
                        iterator += 1
                    action = int(input("Select an item to use (#): "))
                    player_data.item_use(action - 1)
                else:
                    print("You dont have any items in your inventory! Buy some from the shop levels.")
                    time.sleep(2)
            else:
                print("That is not a valid action!")
                time.sleep(1.5)
                selection = None,None
        except Exception as err: # handling
            print(f"An error occured during processing! {err}")
            time.sleep(1.5)
            selection = None,None
        os.system('cls')
        minefield.UI_elements("debug")
        try:
            minefield.EOR_check(player_data.turn,*selection)
        except TypeError:
            pass
    player_data.points += math.floor(((50*player_data.bomb_streak_max) / 2) * player_data.points_multi)
    gameover()

def gameover(): # gameover screen

    os.system('cls')
    print(f"{player_data.name.upper()} has died! Game over!")
    print("=================")
    print("Statistics:")
    print(f"Level Reached: {player_data.level}")
    print(f"Points Obtained: {player_data.points}")
    print(f"Coin Balance: {player_data.coins}")
    print(f"Highest Bomb Streak: {player_data.bomb_streak_max}")
    print("=================")
    input("\nPress any key to continue...")
    print("Thanks for playing! You will now be sent back to the main menu!")
    time.sleep(1)
    start_menu()

welcome()
start_menu()