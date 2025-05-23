# Originally Created on 2/12/2025
## Created as an asset for Super-Minesweep
### DO NOT COPY THIS PROJECT WITHOUT CREDITS TO BROCLLY

import random
import time
import os 
import colorama
import player

minesweep_matrix = [[]]
cover_field = [[]]
type_field = [[]]
mine_count = 0
player_data = player.Player() 
level = player_data.level
total_x = 0


def generate(): # generates a new field based on multiple parameters
    global mine_count
    mine_count = 0
    for x in range(level + 1): # generates 1 row, plus 1 for every level completed
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

    for x in range(level  + 1): # counts bombs that are in every single row
        mine_count = mine_count + minesweep_matrix[x].count("*")

def type_generate(): # generates type of bomb per bomb generated
    try:
        roll = random.randint(0, int((9*level)/((level^level)*1.8)))
        if roll >= 10:
            return "cr"
        else:
            return "ba"
    except ZeroDivisionError:
        return "ba"


def sweeper_check(row_select,column_select,turn): # checks plot selected
    if minesweep_matrix[row_select][column_select] == "*" and turn > 0: # returns if bomb stepped on
        return "1A"
    elif minesweep_matrix[row_select][column_select] == "*" and turn == 0: # returns if 1st turn immunity is applied
        return "1B"
    else: # checks every single possible area where a bomb could be in relation to plot selection
        temp = 0
        try:
            if minesweep_matrix[row_select][(column_select + 1)]  == "*":
                temp += 1
        except:
            pass
        try:
            if minesweep_matrix[row_select][(column_select - 1)]  == "*":
                temp += 1
        except:
            pass
        try:
            if minesweep_matrix[(row_select + 1)][column_select] == "*":
                temp += 1
        except:
            pass
        try:
            if minesweep_matrix[(row_select - 1)][column_select] == "*":
                temp += 1
        except:
            pass
        return temp
        

def field_update(row_select,column_select,bomb):
    cover_field[row_select].pop(column_select) # gets rid of selected slot
    if bomb == "1A": # replaces area with bomb
        cover_field[row_select].insert((column_select),"*")
    elif bomb == "1B": # replaces area with 1st turn immunity
        global mine_count
        cover_field[row_select].insert((column_select),"/")
        mine_count = mine_count - 1
    else:
        if bomb == 0: # replaces with integer
            cover_field[row_select].insert((column_select),"0")
        else:
            cover_field[row_select].insert((column_select),str(bomb))

def EOR_check(turn,row_select, column_select): # checks status of player
    global total_x
    total_x = 0
    if cover_field[row_select][column_select] == "*" and turn > 0: # checks if directly selected plot has a bomb
        mine_type, dmg = bomb_type_check(type_field[row_select][column_select]) # checks type of bomb on plot
        player_data.health = player_data.health - dmg # changes health to match damage
        player_data.EOR_ability_check(player_data, dmg) # checks current abilities, applies effects
        print(f"{player_data.name.upper()} landed on a " + colorama.Fore.RED + f"{mine_type.upper()}" + " bomb" + colorama.Style.RESET_ALL + f"! {player_data.name.upper()} has {player_data.health} health left!!") # front end stuffs
        print("Sweep streak reset!")
        player_data.bomb_streak = 0 # resets sweep streak
        time.sleep(2)
    else:
        player_data.bomb_streak += 1
        player_data.EOR_ability_check(player_data, 0)

    if player_data.health <= 0:
        print(f"{player_data.name.upper()} died! Game over!")
        time.sleep(4)
        quit()

    for x in range(level + 1): # find the total amount of x's left on any turn
        total_x += cover_field[x].count("x")

    if total_x == mine_count: # checks if amount of x's left matches total amount of mines 
        os.system('cls')
        UI_elements("sp")
        print(f"{player_data.name.upper()} win! Congratulations!")
        while True:
            cont = input("Play again? (y/n)")
            if cont == "y":
                regenerate()
                break
            elif cont == "n":
                print("See you later!")
                time.sleep(4)
                quit()
            else:
                print("Invalid answer!")  

def bomb_type_check(bomb): # returns useful information in exchange for bomb prefix
    if bomb == "cr":
        return "corrupted", 50
    elif bomb == "ba":
        return "basic", 20

def regenerate(): # runs task to restart game
    os.system('cls')
    global cover_field
    global minesweep_matrix
    global level
    global turn
    cover_field = [["x","x","x","x","x","x","x","x","x","x"] * level]  # resets cover field
    minesweep_matrix = [[]] # resets minesweep matrix when restarting
    level += 1
    player_data.turn = 0
    generate() 

def UI_elements(type): # basic hud
    if type == "n": # displays current field
        print("===================") 
        print(f"Mines: {mine_count}")
        print("Level: " + str(level))
        print(f"Health: {str(player_data.health)}")
        print("Current Minefield:") 

        for i in range((level + 1)):
            print(cover_field[i], i)
        print("  0    1    2    3    4    5    6    7    8    9  ")
        print("===================")

    elif type == "sp": # displays final field
        print("===================") 
        print(f"Mines: {mine_count}")
        print("Level: " + str(level))
        print(f"Health: {str(player_data.health)}")
        print("Current Minefield:") 

        for i in range((level + 1)):
            print(minesweep_matrix[i], i)
        print("  0    1    2    3    4    5    6    7    8    9  ")
        print("===================")

    elif type =="debug": # displays debug field, used for testing
        print("===================") 
        print(f"Mines: {mine_count}")
        print("Level: " + str(level))
        print(f"Health: {str(player_data.health)}")
        print("Current Minefield:") 

        for i in range((level + 1)):
            print(cover_field[i], i) 
        print("  0    1    2    3    4    5    6    7    8    9  ")

        print("Current Matrix:")

        for i in range((level + 1)):
            print(minesweep_matrix[i])
        print("Current Type Field:")

        for i in range((level + 1)):
            print(type_field[i])
        print("===================")