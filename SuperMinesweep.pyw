# Created on 2025/09/29
## Created as project Super Minesweeper
### DO NOT COPY WITHOUT CREDITS

# initalizing stuff

import pygame, assets.resources as resources, assets.player as player
user_data = player.Player()
screen_data = resources.Screen()
pygame.init()

# variable setup

game_active = True
screen_data.current_screen = "Title"
screen = pygame.display.set_mode([750,550])

# run loop

while game_active:
    if screen_data.current_screen == "Title":
        screen_data.main_menu(screen)
    elif screen_data.current_screen == "Play Field":
        screen_data.play_field(screen)
    elif screen_data.current_screen == "Game Over":
        pass

    user_data.update_data()
    user_data.curs_collision_check(screen_data.screen_objects)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False   
pygame.quit()