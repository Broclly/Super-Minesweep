#Originally Created on 2/12/2025
## Created as Minesweeper 
### DO NOT COPY THIS PROJECT WITHOUT CREDITS TO BROCLLY

import time
import generate
import os

selection = 0
build_ver = 1.0

def welcome(): # intro message
    print("~Hello! Welcome to Minesweeper!~")
    print(f"Build ver: {build_ver}\n")
    time.sleep(1.5)
    input("Press enter to start!")

def gameplay(): # gameplay loop
    while True:
        os.system('cls')
        UI_elements("n") 
        try: # error
            selection = int(input("Select a plot number (1-10): "))
            status = generate.sweeper_check(selection)
            generate.field_update(selection,status)
        except: # handling.
            print("This is not a valid plot! Enter only numbers between 1 and 10 (inclusive)")
            time.sleep(3)
        os.system('cls')
        UI_elements("n")
        generate.EOR_check()
        time.sleep(1)

def UI_elements(type): # basic hud
    if type == "n": # displays current field
        print("===================") 
        print("Current Minefield:") 
        print(generate.cover_field) 
        print("===================\n")
    elif type == "sp": # displays final field
        print("===================") 
        print("Current Minefield:") 
        print(generate.minesweep_matrix) 
        print("===================\n")

welcome()
generate.generate_small()
gameplay()