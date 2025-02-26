#Originally Created on 2/12/2025
## Created as an asset for Super-Minesweep
### DO NOT COPY THIS PROJECT WITHOUT CREDITS TO BROCLLY

import random
import time
import os 
import colorama
import player

minesweep_matrix = [[]]
cover_field = [[]]
mine_count = 0
player_data = player.Player() 
level = player_data.level
total_x = 0


def generate(): # geneerates a new field based on multiple parameters
    global mine_count
    mine_count = 0
    for x in range(level + 1): # generates 1 row, plus 1 for every level completed
        minesweep_matrix.insert(x,["o","o","o","o","o","o","o","o","o","o"])
        cover_field.insert(x,["x","x","x","x","x","x","x","x","x","x"])
        for i in range(4): # random assignment for bomb placement, runs 4 times multiplied by the amount of levels completed plus one
            temp = random.randint(0,9)
            minesweep_matrix[x].pop((temp))
            minesweep_matrix[x].insert((temp),"*")
    for x in range(level  + 1): # counts bombs that are in every single row
        mine_count = mine_count + minesweep_matrix[x].count("*")

def sweeper_check(column_select,row_select,turn): # checks plot selected
    if minesweep_matrix[column_select][row_select] == "*" and turn > 0: # returns if bomb stepped on
        return "1A"
    elif minesweep_matrix[column_select][row_select] == "*" and turn == 0: # returns if 1st turn immunity is applied
        return "1B"
    else: # checks every single possible area where a bomb could be
        temp = 0
        try:
            if minesweep_matrix[column_select][(row_select + 1)]  == "*":
                temp += 1
        except:
            pass
        try:
            if minesweep_matrix[column_select][(row_select - 1)]  == "*":
                temp += 1
        except:
            pass
        try:
            if minesweep_matrix[(column_select + 1)][row_select] == "*":
                temp += 1
        except:
            pass
        try:
            if minesweep_matrix[(column_select - 1)][row_select] == "*":
                temp += 1
        except:
            pass
        return temp
        

def field_update(column_select,row_select,bomb):
    cover_field[column_select].pop(row_select) # gets rid of selected slot
    if bomb == "1A": # replaces area with bomb
        cover_field[column_select].insert((row_select),"*")
    elif bomb == "1B": # replaces area with 1st turn immunity
        global mine_count
        cover_field[column_select].insert((row_select),"/")
        mine_count = mine_count - 1
    else:
        if bomb == 0: # replaces with integer
            cover_field[column_select].insert((row_select),"0")
        else:
            cover_field[column_select].insert((row_select),str(bomb))

def EOR_check(turn): # Checks if you've won or lost
    global total_x
    total_x = 0
    for x in range(level + 1): # checks if any fields have bombs active
        if cover_field[x].count("*") > 0 and turn > 0:
            print("You landed on a " + colorama.Fore.RED +  "bomb" + colorama.Style.RESET_ALL + "!! You lose!")
            time.sleep(4)
            quit()
    for x in range(level + 1): # find the total amount of x's left on any turn
        total_x += cover_field[x].count("x")
    if total_x == mine_count: # checks if amount of x's left matches total amount of mines 
        os.system('cls')
        UI_elements("sp")
        print("You win! Congratulations!")
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

def regenerate(): # runs task to restart game
    os.system('cls')
    global cover_field
    global minesweep_matrix
    global level
    cover_field = [["x","x","x","x","x","x","x","x","x","x"] * level]  # resets cover field
    minesweep_matrix = [[]] # resets minesweep matrix when restarting
    level += 1
    generate() 

def UI_elements(type): # basic hud
    if type == "n": # displays current field
        print("===================") 
        print(f"Mines: {mine_count}")
        print("Level: " + str(level))
        print("Current Minefield:") 
        for i in range((level + 1)):
            print(cover_field[i])
        print("===================\n")
    elif type == "sp": # displays final field
        print("===================") 
        print(f"Mines: {mine_count}")
        print("Level: " + str(level))
        print("Current Minefield:") 
        for i in range((level + 1)):
            print(minesweep_matrix[i]) 
        print("===================\n")