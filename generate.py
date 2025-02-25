#Originally Created on 2/12/2025
## Created as an asset for Super-Minesweep
### DO NOT COPY THIS PROJECT WITHOUT CREDITS TO BROCLLY

import random
import time
import os 
import colorama
import player

minesweep_matrix = ["o","o","o","o","o","o","o","o","o","o",]
cover_field = ["x","x","x","x","x","x","x","x","x","x"]
mine_count = 0
player_data = player.Player()

def generate():
    for i in range(4):
        temp = random.randint(0,9)
        minesweep_matrix.pop((temp))
        minesweep_matrix.insert((temp),"*")
    global mine_count
    mine_count = minesweep_matrix.count("*")
def sweeper_check(plot,turn):
    if minesweep_matrix[(plot)] == "*" and turn > 0:
        return "1A"
    else:
        temp = 0
        try:
            if minesweep_matrix[(plot + 1)] == "*":
                temp += 1
        except:
            return temp
        try:
            if minesweep_matrix[(plot - 1)] == "*":
                temp += 1
            return temp
        except:
            return temp


def field_update(plot,bomb):
    cover_field.pop(plot)
    if bomb == "1A":
        cover_field.insert((plot),"*")
    else:
        if bomb == 0:
            cover_field.insert((plot),"0")
        else:
            cover_field.insert((plot),str(bomb))

def EOR_check(turn): # Checks if you've won or lost
    if cover_field.count("*") > 0 and turn > 0:
        print("You landed on a " + colorama.Fore.RED +  "bomb" + colorama.Style.RESET_ALL + "!! You lose!")
        time.sleep(4)
        quit()
    if cover_field.count("x") == mine_count: 
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
    cover_field = ["x","x","x","x","x","x","x","x","x","x"]
    minesweep_matrix = ["o","o","o","o","o","o","o","o","o","o",]
    generate()

def UI_elements(type): # basic hud
    if type == "n": # displays current field
        print("===================") 
        print("Current Minefield:") 
        print(cover_field) 
        print("===================\n")
    elif type == "sp": # displays final field
        print("===================") 
        print("Current Minefield:") 
        print(minesweep_matrix) 
        print("===================\n")