# Originally created on 07/13/2025
## Created as an asset for Super-Minesweep
### DO NOT COPY THIS PROJECT WITHOUT CREDITS TO BROCLLY

import random
import time
import os

shop_items = ["null","null","null"]

class Item():
    def __init__(self,name: str, desc: str, cost: int, id: int, uses : int): # items initalization
        self.name = name
        self.desc = desc
        self.cost = cost
        self.id = id
        self.uses = uses

def check_item(item): # checks a selected item, provides information
    os.system('cls')
    print(f"Name: {item.name}")
    print(f"Desc: {item.desc}")
    print(f"Price: {item.cost}")
    if item.uses != -1:
        print(f"Uses: {item.uses}")
    input("Press enter to return back to shop menu...")
    os.system('cls')

def buy_item(item,data): # handles shop purchases
    if data.coins - item.cost < 0:
        print("You don't have enough coins to purchase this item!")
        print(f"You need {item.cost - data.coins} more coins to purchase this.")
        time.sleep(1.25)
        os.system('cls')
    else:
        data.coins -= item.cost
        print(f"Your purchase of {item.name} was sucessful!")
        if item.id[0] == "T":
            data.talisman = item.name
    
        elif item.id[0] == "U":
            data.inventory.append([item.name,item.id])
            
        time.sleep(1)
        os.system('cls')

def randomize_shop(data): # randomizes the shop based off of current player data
    random_id = random.randint(0,4)
    shop_items[0] = talismans[random_id]
    for i in range(1,3):
        random_id = random.randint(0,(len(upgrades) - 1))
        shop_items[i] = upgrades[random_id]
    return

def shop(data): # runs main shop cycle
    while True:
        iterator = 0
        print(f"Welcome to the level {data.level + 1} shop!")
        print(f"Coins held: {data.coins}")
        print("====================")
        for item in shop_items:
            iterator += 1
            print(f"Item #{iterator} - {item.name}")
        print("\n1. Check item")
        print("2. Buy item")
        print("3. Continue onto the next level.")
        try:
            action = int(input("Select an action: "))
        except Exception as err:
            print(f"Error occured during processing: {err}")
        if action == 3:
            return
        else:
            iterator = 0
            os.system('cls')
            print("What item would you like to select?")
            for item in shop_items:
                iterator += 1
                print(f"Item #{iterator} - {item.name}")
            try:
                item = int(input("Select an item (enter the corresponding #): ")) - 1
                if item == 0:
                    if action == 1:
                        check_item(shop_items[item])
                    elif action == 2:
                        buy_item(shop_items[item],data)
                else:
                    if action == 1:
                        check_item(shop_items[item])
                    elif action == 2:
                        buy_item(shop_items[item],data)
            except Exception as err:
                print(f"An error occurred during processing: {err}")

# Talismans

RevAmu = Item("Revival Amulet","A golden amulet that shines with your sweeping power. If the user has a high streak, revives them.", 50, "T1", -1)
RetRing = Item("Retro Ring","A small ring too tight on a finger, it hurts the user. But hey, it looks cool. Deals damage to the user for 2x points (stacks).", 75, "T2", -1)
TimeAmu = Item("Timehold Amulet","A silver pocketwatch, with the sands of time flowing inbetween the gears. Heals the user every couple of rounds.", 100, "T3", -1)
PhasBrac = Item("Phaser Braclet", "A specialized bracelet, given to elite members of the Quantum Fighting Corps. Allows for one more turn of immunity per round.", 100, "T4", -1)
GildGaunt = Item("Gilded Gauntlet", "Speckled with gold, these gauntlets bend the will of the world to grant you monetary favor. Grants bonus coins at round end, scales with leveling.", 80, "T5", -1)

# Consumables

LifeInfu = Item("Lifeforce Infusion", "An injectable vial of purplish liquid, enhancing the user's vital systems. Increases user's hp by +10 (stacks).", 25, "U1", 1)
PartyTix = Item("Party Ticket", "A uniquely vibrant ticket, covered in glitter. Adds a .1x modifier to point scoring (stacks).", 25, "U2", 1)
MidasInj = Item("Midas Injection", "Beautiful gold liquid shimmers through it's vial, coating the heart harmlessly in gold. Adds a +10 bonus to gold earned at round end. (stacks)", 25, "U3", 1)
QntmCola = Item("Quantum Cola", "A dazzling drink that seems to shift colors depending on the way you view it. Bombs heal instead of damaging.", 100, "U4",1)
KybrBrry = Item("Kyber Berry", "An extremely unstable berry that's affected by temporal instability. Grants 3 KYBER energy, but if damage is taken on the next turn, death.") 



talismans = [RevAmu,RetRing,TimeAmu,PhasBrac,GildGaunt]
upgrades = [LifeInfu,PartyTix,MidasInj,QntmCola]