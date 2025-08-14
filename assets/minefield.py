# Originally Created on 2/12/2025
## Created as an asset for Super-Minesweep
### DO NOT COPY THIS PROJECT WITHOUT CREDITS TO BROCLLY

import random
import time
import os
import assets.player as player
import subprocess
import sys
import math
import assets.shop as shop

minesweep_matrix = [[]]
cover_field = [[]]
type_field = [[]]
mine_count = 0
player_data = player.Player()
total_x = 0


try: # checks if colorama is installed
    import colorama
except ImportError:
    print("You do not own the 'Colorama' package, which is required to run this program.")
    print("You can install this package via the pip command, or allow this script to install it for you.")
    time.sleep(1/2)
    auto_install = input("Would you like this script to auto install it for you? (respond with either y/n)")
    if auto_install == "y":
        subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
        os.system('cls')
    else:
        print("Please load up this script once colorama has been installed. Thank you! :)")
        time.sleep(1.25)
        quit()

def generate(): # generates a new field based on multiple parameters
    global mine_count
    mine_count = 0
    for x in range(player_data.level + 1): # generates 1 row, plus 1 for every level completed
        minesweep_matrix.insert(x,["o","o","o","o","o","o","o","o","o","o"])
        cover_field.insert(x,["x","x","x","x","x","x","x","x","x","x"])
        type_field.insert(x,["n","n","n","n","n","n","n","n","n","n"])

        for i in range(4): # random assignment for bomb placement, runs 4 times multiplied by the amount of levels completed plus one
            plot_replace = random.randint(0,9)
            bomb_type = type_generate()
            type_field[x].pop(plot_replace)
            type_field[x].insert(plot_replace,bomb_type)
            minesweep_matrix[x].pop(plot_replace)
            minesweep_matrix[x].insert(plot_replace,"*")

    for x in range(player_data.level  + 1): # counts bombs that are in every single row
        mine_count = mine_count + minesweep_matrix[x].count("*")

def type_generate(): # generates type of bomb per bomb generated
    try:
        roll = random.randint(0, int((9*player_data.level)/((player_data.level^player_data.level)*1.8)))
        if roll >= 10:
            return "cr"
        else:
            return "ba"
    except ZeroDivisionError:
        return "ba"

def sweeper_check(row_select,column_select,turn): # checks plot selected
    if minesweep_matrix[row_select][column_select] == "*" and turn > 0: # returns if bomb stepped on
        return "1A"
    elif minesweep_matrix[row_select][column_select] == "*" and player_data.turn_immunities > 0: # returns if turn immunity is applied
        return "1B"
    else: # checks every single possible area where a bomb could be in relation to plot selection
        temp = 0
        try:
            if minesweep_matrix[row_select][(column_select + 1)]  == "*" and column_select != 9:
                temp += 1
        except:
            pass
        try:
            if minesweep_matrix[row_select][(column_select - 1)]  == "*" and column_select != 0:
                temp += 1
        except:
            pass
        try:
            if minesweep_matrix[(row_select + 1)][column_select] == "*" and row_select != 0:
                temp += 1
        except:
            pass
        try:
            if minesweep_matrix[(row_select - 1)][column_select] == "*" and row_select != player_data.level:
                temp += 1
        except:
            pass
        return temp

def field_update(row_select,column_select,bomb): # updates field graphic
    if bomb != "F":
        cover_field[row_select].pop(column_select) # gets rid of selected slot
    if bomb == "1A": # replaces area with bomb
        cover_field[row_select].insert((column_select),"*")
    elif bomb == "1B": # replaces area with 1st turn immunity
        global mine_count
        cover_field[row_select].insert((column_select),"/")
        mine_count = mine_count - 1
    elif bomb == "F": # points to the flag manager
        field_flag(row_select,column_select)
    else:
        if bomb == 0: # replaces with integer
            cover_field[row_select].insert((column_select),"0")
        else:
            cover_field[row_select].insert((column_select),str(bomb))

def field_flag(row_select,column_select): # toggles a flag on a specified plot
    if cover_field[row_select][column_select] == "+": # checks if flag exists on the plot
        print("\nWarning!")
        print("This plot already has a flag on it! Toggling this will remove the flag!")
        action = input("Continue? (y/n)")
        if action == "y":
            cover_field[row_select].pop(column_select)
            cover_field[row_select].insert((column_select),"x")
            print("Flag removed!")
            time.sleep(0.8)
        else:
            return
    elif cover_field[row_select][column_select] != "+" and cover_field[row_select][column_select] != "x": # checks if a plots value is already known
        print("This has a non-flagable symbol on it. Please only flag on plots with a 'x' on it!")
        time.sleep(1.5)
    elif cover_field[row_select][column_select]: # adds flag if all other requirements are met
        cover_field[row_select].pop(column_select)
        cover_field[row_select].insert((column_select),"+")

def EOR_check(turn,row_select, column_select): # checks status of player
    global total_x
    total_x = 0
    if cover_field[row_select][column_select] == "*" and player_data.turn_immunities <= 0: # checks if directly selected plot has a bomb
        mine_type, dmg = bomb_type_check(type_field[row_select][column_select]) # checks type of bomb on plot
        player_data.health = player_data.health - dmg # changes health to match damage
        player_data.points -= 10 # deduct points
        player_data.EOR_ability_check(player_data, dmg) # checks current abilities, applies effects
        print(f"{player_data.name.upper()} landed on a " + colorama.Fore.RED + f"{mine_type.upper()}" + " bomb" + colorama.Style.RESET_ALL + f"! {player_data.name.upper()} has {player_data.health} health left!!") # front end stuffs

        if player_data.bomb_streak_max < player_data.bomb_streak: # bomb streak related stuff
            player_data.bomb_streak_max = player_data.bomb_streak
        print("Sweep streak reset!")
        player_data.bomb_streak = 0 

        time.sleep(2)
    else:
        player_data.bomb_streak += 1
        player_data.EOR_ability_check(player_data, 0)
        player_data.turn_immunities -= 1

    for x in range(player_data.level + 1): # find the total amount of x's left on any turn
        total_x += cover_field[x].count("x")

    if total_x == mine_count or player_data.player_class == "D2": # checks if amount of x's left matches total amount of mines 
        os.system('cls')
        UI_elements("sp")
        print(f"{player_data.name.upper()} win! Congratulations!")
        player_data.points += math.floor((((1.79 ** player_data.level) + 125) * player_data.points_multi))
        player_data.coins += math.floor(((((1.3*player_data.level) ** 1/2) * 10) / (3 ** 1/player_data.level)) + 50 + player_data.coins_bonus) 
        if player_data.talisman == "Gilded Gaunlet":
            player_data.coins += math.floor(5 * (1/2 * player_data.level))
        input("Press any key to continue to the next level...")
        time.sleep(2)
        if (player_data.level + 1) % 2 == 0 and player_data.talisman == "Timehold Amulet":
            player_data.health += 15
        if (player_data.level + 1) % 3 == 0:
            shop.randomize_shop(player_data)
            shop.shop(player_data)
            player_data.level += 1
            regenerate()
        else:
            regenerate()

        
def bomb_type_check(bomb): # returns useful information in exchange for bomb prefix
    if bomb == "cr":
        return "corrupted", 50
    elif bomb == "ba":
        return "basic", 20

def regenerate(): # runs task to restart game
    os.system('cls')
    global cover_field
    global minesweep_matrix
    cover_field = [["x","x","x","x","x","x","x","x","x","x"] * player_data.level]  # resets cover field
    minesweep_matrix = [[]] # resets minesweep matrix when restarting
    player_data.level += 1
    player_data.turn = 0
    player_data.turn_immunities = 1
    generate()
    if player_data.talisman == "Phaser Braclet":
        player_data.turn_immunities = 1


def UI_elements(type): # basic hud
    if type == "n": # displays current field
        print("===================") 
        print(f"Mines: {mine_count}")
        print("Level: " + str(player_data.level))
        print(f"Health: {str(player_data.health)}")
        print(f"Points Multi: {player_data.points_multi}")
        print("Current Minefield:")

        for i in range((player_data.level + 1)):
            print(cover_field[i], i)
        print("  0    1    2    3    4    5    6    7    8    9")
        print("===================")

    elif type == "sp": # displays final field
        print("===================") 
        print(f"Mines: {mine_count}")
        print("Level: " + str(player_data.level))
        print(f"Health: {str(player_data.health)}")
        print(f"Points Multi: {player_data.points_multi}")
        print("Current Minefield:")

        for i in range((player_data.level + 1)):
            print(minesweep_matrix[i], i)
        print("  0    1    2    3    4    5    6    7    8    9  ")
        print("===================")

    elif type =="debug": # displays debug field, used for testing
        print("===================") 
        print(f"Mines: {mine_count}")
        print("Level: " + str(player_data.level))
        print(f"Health: {str(player_data.health)}")
        print(f"Points Multi: {player_data.points_multi}")
        print("Current Minefield:")         
        
        for i in range((player_data.level + 1)):
            print(cover_field[i], i) 
        print("  0    1    2    3    4    5    6    7    8    9  ")

        print("Current Matrix:")

        for i in range((player_data.level + 1)):
            print(minesweep_matrix[i])
        print("Current Type Field:")

        for i in range((player_data.level + 1)):
            print(type_field[i])
        print("===================")