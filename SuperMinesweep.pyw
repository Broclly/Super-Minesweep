# Created on 2025/09/29
## Created as project Super Minesweeper
### DO NOT COPY WITHOUT CREDITS

# initalizing stuff

import pygame, assets.resources as resources, assets.player as player
user_data = player.Player()
pygame.init()

# variable setup

game_active = True
user_data.current_screen = "Title"
screen = pygame.display.set_mode([750,550])

# run loop

while game_active:
    if user_data.current_screen == "Title":
        resources.main_menu(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False
    pygame.display.flip()
pygame.quit()
