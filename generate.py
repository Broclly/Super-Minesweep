#Originally Created on 2/12/2025
## Created as an asset for Minesweeper
### DO NOT COPY THIS PROJECT WITHOUT CREDITS TO BROCLLY

import random
import time
import os 

minesweep_matrix = ["o","o","o","o","o","o","o","o","o","o",]
cover_field = ["x","x","x","x","x","x","x","x","x","x"]

def generate_small():
    for i in range(4):
        temp = random.randint(1,10)
        minesweep_matrix.pop((temp-1))
        minesweep_matrix.insert((temp-1),"*")

def sweeper_check(plot):
    if minesweep_matrix[(plot - 1)] == "o":
        return 0
    else:
        return 1

def field_update(plot,bomb):
    cover_field.pop(plot-1)
    if bomb == 1:
        cover_field.insert((plot-1),"*")
    else:
        cover_field.insert((plot-1),"o")

def EOR_check(): 
    if minesweep_matrix.count("o") == cover_field.count("o"):
        os.system('cls')
        print("You win! Congratulations!")
        time.sleep(4)
        quit()
    
    if cover_field.count("*") > 0:
        print("You landed on a bomb!! You lose!")
        time.sleep(4)
        quit()
