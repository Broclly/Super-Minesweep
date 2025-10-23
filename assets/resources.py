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

class Screen():
    def __init__(self):
        self.current_screen = None
        self.screen_objects = []
        self.first_render = True
        
    def main_menu(self,frame):
        if self.first_render == True:
            self.screen_objects = []
            self.first_render = False

        frame.fill([0,0,0])
        play_box = pygame.draw.rect(frame, [255,255,255], [300, 200, 150, 50])
        self.screen_objects.append([play_box, False, False])

        title_text = large_font.render("Welcome to Super Minesweeper!",False,[255,255,255])
        if self.screen_objects[0][2] == True:
            play_text = med_font.render("Play!", False, [255,0,0])
        elif self.screen_objects[0][1] == True:
            play_text = med_font.render("Play!", False, [100,100,100])
        else:
            play_text = med_font.render("Play!", False, [0,0,0])
        frame.blit(title_text,[150, 40, 50, 50])
        frame.blit(play_text,[350, 215, 50, 50])

    def play_field(self,frame):
        # rendered properly
        self.screen_objects = []
        test_text = large_font.render("", False,[255,255,255])
        frame.blit(test_text,[150, 40, 50, 50])
        