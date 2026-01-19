# Originally Created on 2/25/2025
## Created as an asset for Super-Minesweep
### DO NOT COPY THIS PROJECT WITHOUT CREDITS TO BROCLLY

import time
import random

class Player():
    def __init__(self):
        self.level = 1
        self.turn = 0
        self.points = 0
        self.points_multi = 1.0
        self.coins = 0
        self.coins_bonus = 0
        self.talisman = "Phaser Braclet"
        self.bomb_streak = 0
        self.bomb_streak_max = 0
        self.health = 100
        self.name = "ERROR"
        self.player_class = "ERROR"
        self.turn_immunities = 1
        self.abilities = []
        self.inventory = []
    
    def attr_fetch(self,selected_class):
        index = 0
        for i in player_classes:
            index += 1
            if index == selected_class:
                return player_classes[(index - 1)]["health"], player_classes[(index - 1)]["id"], player_classes[(index - 1)]["abilities"]
    
    def player_reset(self): # back to the default settings 
        self.level = 1
        self.turn = 0
        self.points = 0
        self.points_multi = 1.0
        self.coins = 0
        self.coins_bonus = 0
        self.talisman = "Phaser Braclet"
        self.bomb_streak = 0
        self.bomb_streak_max = 0
        self.health = 100
        self.name = "ERROR"
        self.player_class = "ERROR"
        self.turn_immunities = 1
        self.abilities = []
        self.inventory = []
            
    def item_use(self, item): # manages the use of items
        item_id = self.inventory[item][1]
        print("")
        if item_id == "U1":
            self.health += 10
        elif item_id == "U2":
            self.points_multi += .1
        elif item_id == "U3":
            self.coins_bonus += 10
        elif item_id == "U4":
            temp = 0
            for x in self.abilities:
                if x == "Quantum Infliction":
                    self.abilities.pop(temp)
                temp += 1
            self.abilities.append("Quantum Infliction")
        self.inventory.pop(item)

    def EOR_ability_check(self, player, damage): # checks abilities at the end of the game
        if self.talisman == "Retro Ring":
            self.health -= 2
            if self.points_multi < 2.0:
                self.points_multi += 1.0
        elif self.talisman == "Revival Amulet":
            if self.health <= 0 and self.bomb_streak >= 5:
                print("The Revival Amulet glows golden, pulsating life back into your body!")
                self.health += damage
        for i in player.abilities:
            if i == "DMG REDUCT":
                try:
                    player.health += (damage/2)
                    print(f"{player.name} tanked {(damage/2)} damage!")
                    time.sleep(1)
                except:
                    pass
            elif i == "SWEEP HEAL":
                if player.bomb_streak % 5 == 0 and player.bomb_streak != 0:
                    player.health += 20
                    print("Cherry blossoms swirl around...")
                    print(f"{player.name} healed for 20 health!")
                    time.sleep(1) 
            elif i == "HARD 2 KILL":
                if player.health <= 0:
                    temp = random.randint(0,1)
                    print(temp)
                    if temp == 0:
                        player.health += damage
                        print("HEADS! NOT DEAD YET!")
                        print(f"{player.name} healed for {damage} health!")
                        time.sleep(1)
                    else:
                        print("TAILS, YOU LOSE!")
                        time.sleep(1)

player_classes = [{"name" : "Tank", "health": 100, "max_health" : 100, "id" : "T", "abilities" : "DMG REDUCT"}, {"name" : "Healer", "health" : 50, "max_health" : 80, "id" : "H", "abilities" : "SWEEP HEAL"}, {"name" : "Soldier", "health" : 110, "max_health" : 120, "id" : "S", "abilities" : "HARD 2 KILL"}, {"name" : "DEV", "health" : 10, "max_health" : 10, "id" : "D", "abilities" : "NONE"},{"name" : "DEV2", "health" : 10, "max_health" : 10, "id" : "D2", "abilities" : "INSTA-WIN"}]