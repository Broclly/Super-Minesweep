# Created on 2025/09/29
## Created as project Super Minesweeper
### DO NOT COPY WITHOUT CREDITS
import pygame

pygame.init()

class Player():
    def __init__(self):
        self.cursor_position = [0,0]
        self.char_sprite = None
    def update_data(self):
        self.cursor_position = pygame.mouse.get_pos()
    def curs_collision_check(self, screen_objects):
        iterator = 0
        mouse1, mouse2, mouse3 = pygame.mouse.get_pressed()
        for obj in screen_objects:
            x = obj[0]
            collision = x.collidepoint(*self.cursor_position)
            screen_objects[iterator][1] = collision
            if mouse1 == True and screen_objects[iterator][1] == True:
                screen_objects[iterator][2]
            iterator += 1
        print(screen_objects)