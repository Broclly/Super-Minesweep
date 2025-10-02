# Created on 2025/09/29
## Created for project Super Minesweeper
### DO NOT COPY WITHOUT CREDITS
import pygame

pygame.init()

# prefabricated objects for gui

small_font = pygame.font.Font(None, 15)
med_font = pygame.font.Font(None, 25)
large_font = pygame.font.Font(None, 40)


# screens (easy fun managing)
def main_menu(frame):
    title_text = large_font.render("Welcome to Super Minesweeper!",False,[255,255,255])
    play_text = med_font.render("Play!", False, [0,0,0])

    frame.fill([0,0,0])
    frame.blit(title_text,[150, 40, 50, 50])
    pygame.draw.rect(frame, [255,255,255], [300, 200, 150, 50])
    frame.blit(play_text,[350, 215, 50, 50])

def play_field(frame):
    pass
