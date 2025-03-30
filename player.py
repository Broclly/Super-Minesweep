#Originally Created on 2/25/2025
## Created as an asset for Super-Minesweep
### DO NOT COPY THIS PROJECT WITHOUT CREDITS TO BROCLLY

import time
import random
class Player():
    def __init__(self):
        self.level = 1
        self.turn = 0
        self.bomb_streak = 0
        self.health = 100
        self.name = "ERROR"
        self.player_class = "ERROR"
        self.is_corrupted = False
        self.turn_immunities = 1
        self.abilities = []
    
    def attr_fetch(self,selected_class):
        index = 0
        for i in player_classes:
            index += 1
            time.sleep(1)
            if index == selected_class:
                return player_classes[(index - 1)]["health"], player_classes[(index - 1)]["id"], player_classes[(index - 1)]["abilities"]
    
    def EOR_ability_check(self, player, damage):
        for i in player.abilities:
            if i == "DMG REDUCT":
                try:
                    player.health += (damage/2)
                    print(f"{player.name} tanked {(damage/2)} damage!")
                    time.sleep(1)
                except:
                    pass
            elif i == "SWEEP HEAL":
                if player.bomb_streak == 5:
                    player.health += 20
                    player.bomb_streak = 0
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



player_classes = [{"name" : "Tank", "health": 100, "max_health" : 100, "id" : "T", "abilities" : "DMG REDUCT"}, {"name" : "Healer", "health" : 50, "max_health" : 80, "id" : "H", "abilities" : "SWEEP HEAL"}, {"name" : "Soldier", "health" : 110, "max_health" : 120, "id" : "S", "abilities" : "HARD 2 KILL"}]